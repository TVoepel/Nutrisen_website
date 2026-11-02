#!/usr/bin/env python3
"""Add the blog (index + articles) and a "Blog" entry to the main menu of every page.
Run after add_fertilizer_calc.py and BEFORE i18n.py. Content: tools/blog_content.py (English + German).
Usage: python3 tools/add_blog.py <site root>"""
import os, re, sys, html, posixpath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blog_content as BC
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
if os.path.exists(os.path.join(ROOT, 'blog', 'index.html')): sys.exit('already applied')
PAGES = ['', 'medical', 'agriculture', 'agriculture/how-does-it-work', 'agriculture/use-cases', 'agriculture/calculator',
         'agriculture/test-your-field', 'agriculture/from-lab-to-field', 'impressum', 'datenschutzerklarung']
MED, NEW = 'f3e12237-6aaa-44c9-90b4-bbb05118cc8a', 'e91b6c4d-52a7-4f0e-b3d8-7c1a9f2e4b66'
ITEM = r'<div data-page-id="%s"[^>]*>' % MED + r'<div><a href="[^"]*" data-navigation-anchor="true"><span>Medical </span></a></div></div>'
WRAP = '<div class="navigation-menu-item-wrapper">'
def new_item(m_open, page_dir):
    href = posixpath.relpath('blog', page_dir or '.') + '/'
    return m_open.replace(MED, NEW).replace(' navigation-selected', '') + '<div><a href="%s" data-navigation-anchor="true"><span>Blog </span></a></div></div>' % href
def add_nav(t, d):
    def wrapped(m):
        item = m.group(2); op = re.match(r'<div data-page-id="[^"]*"[^>]*>', item).group(0)
        return m.group(1) + item + '</div>' + WRAP + new_item(op, d) + '</div>'
    t = re.sub('(%s)(%s)</div>' % (re.escape(WRAP), ITEM), wrapped, t)
    def plain(m):
        op = re.match(r'<div data-page-id="[^"]*"[^>]*>', m.group(0)).group(0)
        return m.group(0) + new_item(op, d)
    return re.sub('(?<!%s)%s' % (re.escape(WRAP), ITEM), plain, t)
texts = {}
for p in PAGES:
    f = os.path.join(ROOT, p, 'index.html'); texts[p] = add_nav(open(f, encoding='utf-8').read(), p); open(f, 'w', encoding='utf-8').write(texts[p])

# ---------------------------------------------------------------- rebase a page built from the "medical" shell
ATTR = re.compile(r'\b(href|src|poster|data-src)=(["\'])(.*?)\2', re.S)
SRCSET = re.compile(r'\b(srcset|data-srcset)=(["\'])(.*?)\2', re.S)
CSSURL = re.compile(r'url\(\s*(["\']?)([^"\')]+)\1\s*\)')
CAND = re.compile(r',(?=\s*(?:\.\.?/)*(?:wp-content|wp-includes|assets)/)')
def ref(r, src_dir, dst_dir):
    if not r or r.startswith(('#', 'data:', 'mailto:', 'tel:', 'javascript:', '${', 'http:', 'https:', '//')): return r
    m = re.match(r'^([^?#]*)(.*)$', r); base, rest = m.group(1), m.group(2)
    path = posixpath.normpath(posixpath.join(src_dir or '.', base)); path = '' if path == '.' else path
    out = posixpath.relpath(path or '.', dst_dir or '.')
    if base.endswith('/') or base in ('', '.'): out = './' if out == '.' else out + '/'
    return out + rest
def rebase(t, s, d):
    def ss(m):
        parts = []
        for c in CAND.split(m.group(3)):
            b = c.strip().split(None, 1)
            if b: parts.append(ref(b[0], s, d) + (' ' + b[1] if len(b) > 1 else ''))
        return m.group(1) + '=' + m.group(2) + ','.join(parts) + m.group(2)
    t = SRCSET.sub(ss, t)
    t = ATTR.sub(lambda m: m.group(1) + '=' + m.group(2) + ref(m.group(3), s, d) + m.group(2), t)
    return CSSURL.sub(lambda m: 'url(' + m.group(1) + ref(m.group(2), s, d) + m.group(1) + ')', t)

E = lambda x: html.escape(x, quote=False)
def build(body, rel_dir, title, desc):
    t = rebase(texts['medical'], 'medical', rel_dir)
    start = t.find('<!-- /wp:go-x/section -->') + len('<!-- /wp:go-x/section -->')
    end = max(m.start() for m in re.finditer(r'<!-- wp:go-x/section ', t[:t.find('data-zone-type="footer"')]))
    assert 'data-zone-type="content"' in t[start:end] and start < end
    t = t[:start] + '\n' + body + '\n' + t[end:]
    t = re.sub(r'(<div data-page-id="[^"]*"[^>]*class="[^"]*?) navigation-selected', r'\1', t)
    t = re.sub(r'(<div data-page-id="%s"[^>]*class="[^"]*?)"' % NEW, r'\1 navigation-selected"', t)
    t = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % E(title), t, count=1)
    meta = '<meta name="description" content="%s">' % html.escape(desc, quote=True)
    t = re.sub(r'<meta\s+name="description"[^>]*>', meta, t, count=1, flags=re.S) if re.search(r'<meta\s+name="description"', t) else t.replace('</head>', meta + '\n</head>', 1)
    css = posixpath.join(posixpath.relpath('assets', rel_dir), 'blog.css')
    return t.replace('</head>', '<link rel="stylesheet" href="%s">\n</head>' % css, 1)

def write(rel_dir, text):
    d = os.path.join(ROOT, rel_dir); os.makedirs(d, exist_ok=True); open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(text)
def meta(post):
    return ('<p class="ns-blog-meta"><time datetime="%s">%s</time><span aria-hidden="true">·</span><span>%d min read</span></p>'
            % (post.get('date', BC.DATE), E(post.get('date_txt', BC.DATE_TXT)['en']), BC.minutes(post)))

# index
cards = ''.join('<article class="ns-blog-card"><p class="ns-blog-tag">%s</p><h2><a href="%s/">%s</a></h2><p class="ns-blog-ex">%s</p>%s<a class="ns-blog-more" href="%s/">%s</a></article>'
                % (E(p['tag']['en']), p['slug'], E(p['title']['en']), E(p['excerpt']['en']), meta(p), p['slug'], E(BC.BLOG['read']['en'])) for p in BC.POSTS)
index = ('<div class="ns-blog"><header class="ns-blog-hero"><div class="ns-blog-wrap"><p class="ns-blog-eyebrow">%s</p><h1>%s</h1><p class="ns-blog-lead">%s</p></div></header>'
         '<div class="ns-blog-wrap"><div class="ns-blog-grid">%s</div></div></div>') % (E(BC.BLOG['eyebrow']['en']), E(BC.BLOG['title']['en']), E(BC.BLOG['lead']['en']), cards)
write('blog', build(index, 'blog', 'Blog', BC.BLOG['desc']['en']))

# articles
TARGET = {'@calc': 'agriculture/calculator', '@test': 'agriculture/test-your-field'}
for p in BC.POSTS:
    d = 'blog/' + p['slug']; body = ['<p class="ns-blog-intro">%s</p>' % E(p['lead']['en'])]
    for blk in p['blocks']:
        kind, v = blk
        if kind == 'h2': body.append('<h2>%s</h2>' % E(v['en']))
        elif kind == 'p': body.append('<p>%s</p>' % E(v['en']))
        elif kind == 'note': body.append('<p class="ns-blog-note">%s</p>' % E(v['en']))
        elif kind == 'ol': body.append('<ol>%s</ol>' % ''.join('<li>%s</li>' % E(x['en']) for x in v))
        elif kind == 'olb':
            body.append('<ol>%s</ol>' % ''.join('<li><strong>%s.</strong> %s</li>' % (E(x['en'].split('. ', 1)[0]), E(x['en'].split('. ', 1)[1])) for x in v))
        elif kind == 'link':
            body.append('<p class="ns-blog-link"><span>%s</span> <a href="%s" target="_blank" rel="noopener">%s</a></p>' % (E(v['label']['en']), v['href'], E(v['text'])))
        elif kind == 'cta':
            href = posixpath.relpath(TARGET[v['href']], d) + '/'
            body.append('<aside class="ns-blog-cta"><h2>%s</h2><p>%s</p><a class="ns-blog-btn" href="%s">%s</a></aside>' % (E(v['h']['en']), E(v['p']['en']), href, E(v['btn']['en'])))
    src = '<section class="ns-blog-src"><h2>%s</h2><ul>%s</ul></section>' % (E(BC.BLOG['sources']['en']), ''.join(
        '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (h, E(l['en'])) for h, l in p['sources']))
    faq = ''
    if p.get('faq'):
        faq = '<section class="ns-blog-faq"><h2>%s</h2>%s</section>' % (E(BC.BLOG['faq']['en']), ''.join(
            '<details><summary>%s</summary><p>%s</p></details>' % (E(q['en']), E(a['en'])) for q, a in p['faq']))
    page = ('<div class="ns-blog"><header class="ns-blog-hero"><div class="ns-blog-wrap narrow"><a class="ns-blog-back" href="../">%s</a><p class="ns-blog-tag">%s</p><h1>%s</h1>%s</div></header>'
            '<div class="ns-blog-wrap narrow"><article class="ns-blog-article">%s%s</article></div></div>') % (
            E(BC.BLOG['back']['en']), E(p['tag']['en']), E(p['title']['en']), meta(p), ''.join(body), faq + src)
    write(d, build(page, d, p['title']['en'], p['excerpt']['en']))
print('added blog with', len(BC.POSTS), 'articles')
