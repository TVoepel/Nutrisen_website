#!/usr/bin/env python3
"""Speed pass, run LAST (after i18n.py): WebP images with width/height + lazy loading, woff2-only fonts with
font-display:swap and preload, no HTML comments / dead scripts (emoji, Gutenberg i18n, IE banner), analytics loaded after the page, minified inline CSS,
no fixed-attachment backgrounds, unreferenced files deleted, cache/compression config.
Not idempotent. Usage: python3 tools/optimize.py <site root>   (needs: pip install pillow; node for a syntax check)"""
import os, re, sys, glob, posixpath, subprocess, tempfile
from PIL import Image
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
os.chdir(ROOT)
pages = sorted(glob.glob('**/index.html', recursive=True))
css_files = [f for f in glob.glob('wp-content/**/*.css', recursive=True)]
def rd(f): return open(f, encoding='utf-8', errors='ignore').read()
def wr(f, t): open(f, 'w', encoding='utf-8').write(t)
def du(): return sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk('.') if '.git' not in d for f in fs)
before = du()
if any('rel="preload" href' in rd(p) and 'font/woff2' in rd(p) for p in pages): sys.exit('already applied')

# ---------------------------------------------------------------- 1. markup clean-up
SCRIPT_STYLE = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>)', re.S | re.I)
def outside(text, fn):
    parts = SCRIPT_STYLE.split(text)
    for i in range(0, len(parts), 2): parts[i] = fn(parts[i])
    return ''.join(parts)
def banner_free(js):
    s = js.find('(function(){var ua = window.navigator.userAgent;var trident')
    if s < 0 or 'old-browser-banner' not in js[s:]: return js
    for m in re.finditer(r'\}\)\(\);', js[s:]):
        cand = js[:s] + js[s + m.end():]
        if 'old-browser-banner' in cand: continue
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as tf: tf.write(cand)
        if subprocess.run(['node', '--check', tf.name], capture_output=True).returncode == 0: return cand
    return js
def cleanup(t):
    t = outside(t, lambda x: re.sub(r'<!--(?!\[if).*?-->', '', x, flags=re.S))
    t = re.sub(r'<script id="wp-(?:hooks-js|i18n-js)" src="[^"]*"></script>\s*', '', t)
    t = re.sub(r'<script id="wp-i18n-js-after">.*?</script>\s*', '', t, flags=re.S)
    t = re.sub(r'<script id="wp-emoji-settings"[^>]*>.*?</script>\s*', '', t, flags=re.S)
    t = re.sub(r'<script type="module">(?:(?!</script>).)*wp-emoji-settings.*?</script>\s*', '', t, flags=re.S)
    t = re.sub(r'<style id="wp-emoji-styles-inline-css">.*?</style>\s*', '', t, flags=re.S)
    t = re.sub(r'(<script>)((?:(?!</script>).){15000,})(</script>)', lambda m: m.group(1) + banner_free(m.group(2)) + m.group(3), t, flags=re.S)
    def mini(m):
        c = re.sub(r'/\*.*?\*/', '', m.group(2), flags=re.S); c = re.sub(r'\s+', ' ', c)
        return m.group(1) + re.sub(r' ?([{};]) ?', r'\1', c).strip() + m.group(3)
    t = re.sub(r'(<style[^>]*>)(.*?)(</style>)', mini, t, flags=re.S)
    # the site's own analytics (cdn.pagepulse.info) is switched OFF by default (GDPR, no consent banner). The code stays and runs
    # only when <meta name="ns-analytics" content="on"> is present; then it loads after the page load, when the browser is idle.
    key = "sel.src = '//cdn.pagepulse.info/js/22728.js';document.head.appendChild(sel);"
    t = t.replace(key, "sel.src = '//cdn.pagepulse.info/js/22728.js';if(document.querySelector('meta[name=ns-analytics][content=on]'))addEventListener('load',function(){(window.requestIdleCallback||setTimeout)(function(){document.head.appendChild(sel)})});")
    t = re.sub(r'(<meta charset="[^"]*"\s*/?>)', r'\1<meta name="ns-analytics" content="off">', t, count=1) if 'name="ns-analytics"' not in t else t
    return t.replace('background-attachment:fixed', 'background-attachment:scroll')

# ---------------------------------------------------------------- 2. fonts: woff2 only, swap, dedupe, preload
FF = re.compile(r'@font-face\{[^}]*\}')
def fonts(t, pdir):
    seen = set()
    def one(m):
        b = m.group(0); w2 = re.search(r'url\(([^)]*?\.woff2)\)', b)
        fam = re.search(r'font-family:([^;}]+)', b); sty = re.search(r'font-style:([^;}]+)', b); wei = re.search(r'font-weight:([^;}]+)', b)
        if not (w2 and fam): return b
        key = (fam.group(1), sty and sty.group(1), wei and wei.group(1))
        if key in seen: return ''
        seen.add(key)
        return '@font-face{font-family:%s;font-style:%s;font-weight:%s;font-display:swap;src:url(%s) format("woff2")}' % (
            key[0], key[1] or 'normal', key[2] or '400', w2.group(1))
    t = FF.sub(one, t)
    pre = ''.join('<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>\n' % posixpath.join(
        posixpath.relpath('wp-content/themes/gox/public/fonts', pdir or '.'), f) for f in
        ('Poppins-latin_latin-ext-regular.woff2', 'Poppins-latin_latin-ext-700.woff2', 'Hind-latin_latin-ext-regular.woff2'))
    return t.replace('<link rel="stylesheet"', pre + '<link rel="stylesheet"', 1) if pre not in t else t

# ---------------------------------------------------------------- 3. images
keep = set()
for p in pages:
    for tag in re.findall(r'<(?:link[^>]*rel=["\'][^"\']*icon[^"\']*["\'][^>]*|meta[^>]*)>', rd(p)):
        keep.update(re.findall(r'wp-content/uploads/go-x/u/[^"\'\s)]+', tag))
conv = {}   # old root-relative path -> (new path, w, h)
for f in glob.glob('wp-content/uploads/go-x/u/**/*', recursive=True):
    ext = os.path.splitext(f)[1].lower()
    if ext not in ('.png', '.jpg', '.jpeg') or f in keep: continue
    im = Image.open(f); im.load()
    if im.width > 1920: im = im.resize((1920, round(im.height * 1920 / im.width)), Image.LANCZOS)
    new = os.path.splitext(f)[0] + '.webp'
    if ext == '.png':
        rgba = im.convert('RGBA'); few = rgba.getcolors(4096) is not None
        rgba.save(new, 'WEBP', lossless=True, method=6) if few else rgba.save(new, 'WEBP', quality=80, alpha_quality=90, method=6)
    else:
        im.convert('RGB').save(new, 'WEBP', quality=78, method=6)
    if os.path.getsize(new) >= os.path.getsize(f): os.remove(new); continue
    conv[f] = (new, im.width, im.height)
IMG = re.compile(r'(wp-content/uploads/go-x/u/[^\s"\')]+?\.(?:png|jpe?g))(?=[\s"\')?#]|$)')
def repoint(t): return IMG.sub(lambda m: (conv[m.group(1)][0] if m.group(1) in conv else m.group(1)), t)
def img_tags(t, pdir):
    first = [True]
    def one(m):
        a = m.group(1); isfirst = first[0]; first[0] = False
        src = re.search(r'\bsrc="([^"]+)"', a)
        if src:
            tgt = posixpath.normpath(posixpath.join(pdir or '.', src.group(1)))
            hit = next((v for v in conv.values() if v[0] == tgt), None)
            if hit and not isfirst and 'aspect-ratio' not in a:   # reserve space without fighting the theme's sizing
                if re.search(r'\bstyle="', a): a = re.sub(r'\bstyle="', 'style="aspect-ratio:%d/%d;' % (hit[1], hit[2]), a, count=1)
                else: a += ' style="aspect-ratio:%d/%d"' % (hit[1], hit[2])
        if not isfirst and 'loading=' not in a and 'fetchpriority' not in a: a += ' loading="lazy"'
        if 'decoding=' not in a: a += ' decoding="async"'
        return '<img' + a + '>'
    return re.sub(r'<img\b([^>]*?)/?>', one, t)

for p in pages:
    pdir = posixpath.dirname(p)
    t = cleanup(rd(p)); t = repoint(t); t = fonts(t, pdir); t = img_tags(t, pdir); wr(p, t)
for f in css_files:
    c = rd(f); wr(f, repoint(c))

# ---------------------------------------------------------------- 4. delete what nothing references any more
corpus = ''.join(rd(p) for p in pages) + ''.join(rd(f) for f in css_files + glob.glob('wp-content/**/*.js', recursive=True))
removed = 0
allf = [f for f in glob.glob('wp-content/**/*', recursive=True) + glob.glob('wp-includes/**/*', recursive=True) if os.path.isfile(f)]
bases = {}
for f in allf: bases.setdefault(os.path.basename(f), []).append(f)
def used(f):
    tok = lambda n: re.search(re.escape(n) + r'(?![A-Za-z0-9])', corpus)
    return bool(tok(f)) or (len(bases[os.path.basename(f)]) == 1 and bool(tok(os.path.basename(f))))
for f in allf:
    if not used(f): os.remove(f); removed += 1
for d, _, fs in os.walk('.', topdown=False):
    if '.git' not in d and d != '.' and not os.listdir(d): os.rmdir(d)

# ---------------------------------------------------------------- 5. server hints for Apache (IONOS) and Netlify/Cloudflare-style hosts
open('.htaccess', 'w').write('''# Speed: compression + long caching for versioned static assets (Apache / IONOS hosting)
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/json
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType application/json "access plus 1 hour"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType text/html "access plus 10 minutes"
</IfModule>
''')
open('_headers', 'w').write('''/wp-content/uploads/go-x/u/*
  Cache-Control: public, max-age=31536000, immutable
/wp-content/themes/gox/public/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/assets/hero-*
  Cache-Control: public, max-age=31536000, immutable
/assets/fertilizer-prices.json
  Cache-Control: public, max-age=3600
''')
print('images converted: %d, files removed: %d, size %.1f MB -> %.1f MB' % (len(conv), removed, before / 1e6, du() / 1e6))
