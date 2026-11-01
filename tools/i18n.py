#!/usr/bin/env python3
"""Make the mirror bilingual (EN at /, DE at /de/). Run after build.py and apply_home_split.py.

  English  /                       (lang="en")      unchanged URLs
  German   /de/...                 (lang="de")      translated copies of every content page
  Legal    /impressum/, /datenschutzerklarung/   German originals (stay at their old URLs)
           /legal-notice/, /privacy-policy/      new English courtesy translations
Adds a DE|EN switcher, hreflang/canonical tags and corrects <html lang>. Not idempotent: aborts if applied.
Usage: python3 tools/i18n.py <site root>"""
import os, re, sys, html, posixpath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_strings as T

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
BASE = 'https://www.nutrisen.eu'
if 'class="ns-lang"' in open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read():
    sys.exit('already applied')

SRC = {'home': '', 'medical': 'medical', 'agri': 'agriculture', 'how': 'agriculture/how-does-it-work',
       'test': 'agriculture/test-your-field', 'cases': 'agriculture/use-cases', 'lab': 'agriculture/from-lab-to-field',
       'npk': 'the-npknowledge', 'legal': 'impressum', 'privacy': 'datenschutzerklarung'}
SRC_REV = {v: k for k, v in SRC.items()}
LANGPATH = {
    ('en', 'home'): '', ('en', 'medical'): 'medical', ('en', 'agri'): 'agriculture',
    ('en', 'how'): 'agriculture/how-does-it-work', ('en', 'test'): 'agriculture/test-your-field',
    ('en', 'lab'): 'agriculture/from-lab-to-field', ('en', 'cases'): 'agriculture/use-cases', ('en', 'npk'): 'the-npknowledge',
    ('en', 'legal'): 'legal-notice', ('en', 'privacy'): 'privacy-policy',
    ('de', 'home'): 'de', ('de', 'medical'): 'de/medical', ('de', 'agri'): 'de/agriculture',
    ('de', 'how'): 'de/agriculture/how-does-it-work', ('de', 'test'): 'de/agriculture/test-your-field',
    ('de', 'lab'): 'de/agriculture/from-lab-to-field', ('de', 'cases'): 'de/agriculture/use-cases', ('de', 'legal'): 'impressum', ('de', 'privacy'): 'datenschutzerklarung',
}
def lp(lang, key):  # npk has no German version: link to the English page
    return LANGPATH.get((lang, key)) if (lang, key) in LANGPATH else LANGPATH[('en', key)]

def read(path): return open(os.path.join(ROOT, path, 'index.html'), encoding='utf-8').read()
def write(path, text):
    d = os.path.join(ROOT, path); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(text)
def rel(target, from_dir):
    return posixpath.relpath(target or '.', from_dir or '.')

# ---------------------------------------------------------------- links
SKIP = ('#', 'data:', 'mailto:', 'tel:', 'javascript:', '${', 'http:', 'https:', '//')
def map_ref(ref, src_dir, dst_dir, lang):
    r = ref.strip()
    if not r or r.startswith(SKIP): return ref
    m = re.match(r'^([^?#]*)(\?[^#]*)?(#.*)?$', r)
    base, q, frag = m.group(1), m.group(2) or '', m.group(3) or ''
    path = posixpath.normpath(posixpath.join(src_dir or '.', base)) if base else (src_dir or '.')
    path = '' if path == '.' else path
    if path in SRC_REV and (base.endswith('/') or base in ('', '.', './') or not posixpath.splitext(path)[1]):
        new = rel(lp(lang, SRC_REV[path]), dst_dir)
        new = './' if new == '.' else new + '/'
    else:
        new = rel(path, dst_dir)
    return new + q + frag

ATTR = re.compile(r'\b(href|src|poster|data-src)=(["\'])(.*?)\2', re.S)
SRCSET = re.compile(r'\b(srcset|data-srcset)=(["\'])(.*?)\2', re.S)
CSSURL = re.compile(r'url\(\s*(["\']?)([^"\')]+)\1\s*\)')
CAND = re.compile(r',(?=\s*(?:\.\.?/)*(?:wp-content|wp-includes|assets)/)')
def rebase(text, src_dir, dst_dir, lang):
    f = lambda r: map_ref(r, src_dir, dst_dir, lang)
    def srcset(m):
        out = []
        for c in CAND.split(m.group(3)):
            bits = c.strip().split(None, 1)
            if bits: out.append(f(bits[0]) + (' ' + bits[1] if len(bits) > 1 else ''))
        return m.group(1) + '=' + m.group(2) + ','.join(out) + m.group(2)
    text = SRCSET.sub(srcset, text)
    text = ATTR.sub(lambda m: m.group(1) + '=' + m.group(2) + f(m.group(3)) + m.group(2), text)
    return CSSURL.sub(lambda m: 'url(' + m.group(1) + f(m.group(2)) + m.group(1) + ')', text)

# ---------------------------------------------------------------- text
unmatched = {}
def translate(text, table, keep, label, report=True):
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->)', text, flags=re.S | re.I)
    def seg(m):
        raw = m.group(1)
        key = html.unescape(raw).replace('\xa0', ' ').strip()
        if key in table:
            lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
            nb = '&nbsp;' if raw.rstrip().endswith('&nbsp;') else ''
            return '>' + lead + html.escape(table[key], quote=False) + nb + trail + '<'
        if report and key not in keep and re.search(r'[A-Za-zÄÖÜäöü]{3,}', key):
            unmatched.setdefault(label, set()).add(key)
        return m.group(0)
    def attr(m):   # translatable attributes (mobile table labels, aria-labels)
        k = html.unescape(m.group(2))
        return m.group(1) + html.escape(table[k], quote=True) + m.group(3) if k in table else m.group(0)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'>([^<>]+)<', seg, parts[i])
        parts[i] = re.sub(r'(\b(?:data-label|aria-label)=")([^"]*)(")', attr, parts[i])
    return ''.join(parts)

def set_title(text, title):
    return re.sub(r'<title>[^<]*</title>', '<title>' + html.escape(title, quote=False) + '</title>', text, count=1) if title else text
def map_desc(text, table, label):
    def d(m):
        k = html.unescape(m.group(2))
        if k in table: return m.group(1) + html.escape(table[k], quote=True) + m.group(3)
        if table is T.DESC_DE: unmatched.setdefault(label, set()).add('META: ' + k)
        return m.group(0)
    return re.sub(r'(<meta\s+name="description" content=")([^"]*)(")', d, text, flags=re.S)

# ---------------------------------------------------------------- head / switcher
def url(lang, key):
    p = lp(lang, key); return BASE + '/' + (p + '/' if p else '')
def decorate(text, key, lang, dst_dir):
    has_pair = (('de', key) in LANGPATH) and (('en', key) in LANGPATH)
    head = ['<link rel="stylesheet" href="%s">' % posixpath.join(rel('assets', dst_dir), 'lang.css'),
            '<link rel="canonical" href="%s">' % url(lang, key)]
    if has_pair:
        head += ['<link rel="alternate" hreflang="de" href="%s">' % url('de', key),
                 '<link rel="alternate" hreflang="en" href="%s">' % url('en', key),
                 '<link rel="alternate" hreflang="x-default" href="%s">' % url('en', key)]
    text = text.replace('</head>', '\n'.join(head) + '\n</head>', 1)
    text = re.sub(r'<html lang="[^"]*"', '<html lang="%s"' % lang, text, count=1)
    if has_pair:
        def a(l, label):
            href = rel(lp(l, key), dst_dir); href = './' if href == '.' else href + '/'
            cur = ' aria-current="true"' if l == lang else ''
            return '<a href="%s" lang="%s" hreflang="%s"%s>%s</a>' % (href, l, l, cur, label)
        sw = '<nav class="ns-lang" aria-label="Language / Sprache">%s%s</nav>' % (a('de', 'DE'), a('en', 'EN'))
        text = text.replace('<div id="root">', '<div id="root">' + sw, 1)
    return text

# ---------------------------------------------------------------- build
src = {k: read(p) for k, p in SRC.items()}
for key, p in SRC.items():
    s = src[key]
    # 1) English tree (same URLs; legal pages get the English labels, two wording bugs fixed)
    if key in ('legal', 'privacy'):
        # the German originals stay where they are; German nav, German links
        t = rebase(s, p, p, 'de')
        t = translate(t, {**T.NAV_DE, **T.FIX_DE_LEGAL}, set(), 'de-legal:' + key, report=False)
        t = decorate(t, key, 'de', p)
        write(p, t)
        # English courtesy translation
        t = rebase(s, p, LANGPATH[('en', key)], 'en')
        t = translate(t, T.EN_LEGAL, T.KEEP_LEGAL, 'en-legal:' + key)
        t = set_title(t, T.TITLE_EN_LEGAL[key])
        note = T.LEGAL_NOTE_EN if key == 'legal' else T.LEGAL_NOTE_EN_PRIVACY
        t = t.replace('</h2></div>', '</h2><p class="ns-legal-note">%s</p></div>' % html.escape(note), 1)
        t = decorate(t, key, 'en', LANGPATH[('en', key)])
        write(LANGPATH[('en', key)], t)
        continue
    t = rebase(s, p, p, 'en')
    t = translate(t, T.FIX_EN, set(), 'en:' + key, report=False)
    t = decorate(t, key, 'en', p)
    write(p, t)
    # 2) German tree
    if ('de', key) in LANGPATH:
        d = LANGPATH[('de', key)]
        t = rebase(s, p, d, 'de')
        t = translate(t, T.DE, T.KEEP, 'de:' + key)
        t = set_title(t, T.TITLE_DE[key]); t = map_desc(t, T.DESC_DE, 'de:' + key)
        t = decorate(t, key, 'de', d)
        write(d, t)

# shared stylesheet
os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
if not os.path.exists(os.path.join(ROOT, 'assets', 'lang.css')):
    sys.exit('assets/lang.css missing')
print('pages written; untranslated text:')
for k, v in sorted(unmatched.items()):
    for s in sorted(v): print(' ', k, '|', s[:100])
