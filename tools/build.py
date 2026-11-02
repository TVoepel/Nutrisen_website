#!/usr/bin/env python3
"""Assemble the static mirror: clean slug/index.html pages, query-free asset names, relative links."""
import os, re, shutil, glob, urllib.parse, sys
# Usage: python3 tools/build.py <workdir from tools/fetch.sh> <outdir>
W = sys.argv[1]; OUT = os.path.abspath(sys.argv[2])
RAW = os.path.join(W, 'raw', 'www.nutrisen.eu')
PAGES = os.path.join(W, 'pages')
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

# ---- 1. copy assets, stripping query strings from file names
assets = {}   # site path (no query) -> out abs path
for d in ('wp-content', 'wp-includes'):
    for root, _, files in os.walk(os.path.join(RAW, d)):
        for fn in files:
            src = os.path.join(root, fn)
            rel = os.path.relpath(src, RAW)
            clean = rel.split('?')[0]
            dst = os.path.join(OUT, clean)
            if clean in assets:  # same resource with another ?ver -> keep first
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            assets['/' + clean] = dst
print('assets copied:', len(assets))

# ---- 2. pages
slugs = ['', 'medical', 'agriculture', 'agriculture/how-does-it-work', 'agriculture/test-your-field',
         'agriculture/from-lab-to-field', 'impressum', 'datenschutzerklarung']
page_dirs = {('/' + s + '/') if s else '/': os.path.join(OUT, s) if s else OUT for s in slugs}

HOST = re.compile(r'^(?:https?:)?//(?:www\.)?nutrisen\.eu')
untouched = {}

def resolve(ref, from_dir):
    """Return rewritten ref (relative) or None to leave untouched."""
    r = ref.strip()
    if not r or r.startswith(('#', 'data:', 'mailto:', 'tel:', 'javascript:', '${')):
        return None
    if HOST.match(r):
        r = HOST.sub('', r) or '/'
    elif r.startswith(('http://', 'https://', '//')):
        return None
    if not r.startswith('/'):
        return None
    path, frag = (r.split('#', 1) + [''])[:2]
    path = path.split('?')[0]
    path = urllib.parse.unquote(path)
    frag = ('#' + frag) if frag else ''
    # page?
    p = path if path.endswith('/') else path + '/'
    if p in page_dirs:
        rel = os.path.relpath(page_dirs[p], from_dir)
        return ('./' if rel == '.' else rel + '/') + frag
    if path in assets:
        return os.path.relpath(assets[path], from_dir) + frag
    untouched[ref] = untouched.get(ref, 0) + 1
    return None

SRCSET_SPLIT = re.compile(r',(?=\s*(?:/|https?://|//))')
def rewrite_srcset(val, from_dir):
    parts = []
    for cand in SRCSET_SPLIT.split(val):
        cand = cand.strip()
        if not cand: continue
        bits = cand.split(None, 1)
        new = resolve(bits[0], from_dir)
        parts.append((new or bits[0]) + ((' ' + bits[1]) if len(bits) > 1 else ''))
    return ','.join(parts)

ATTR = re.compile(r'\b(href|src|poster|data-src)=(["\'])(.*?)\2', re.S)
SRCSET = re.compile(r'\b(srcset|data-srcset)=(["\'])(.*?)\2', re.S)
CSSURL = re.compile(r'url\(\s*(["\']?)([^"\')]+)\1\s*\)')
ESC = re.compile(r'https?:\\/\\/(?:www\.)?nutrisen\.eu((?:\\/[^"\'\s<]*)?)')
PLUMBING = re.compile(r'[ \t]*<link[^>]*(?:rel=["\'](?:alternate|https://api\.w\.org/|EditURI|wlwmanifest|shortlink)["\']|/feed/|wp-json|xmlrpc\.php)[^>]*/?>\s*\n?')

def rewrite_text(txt, from_dir, html=True):
    if html:
        txt = PLUMBING.sub('', txt)
        txt = ATTR.sub(lambda m: m.group(1) + '=' + m.group(2) + (resolve(m.group(3), from_dir) or m.group(3)) + m.group(2), txt)
        txt = SRCSET.sub(lambda m: m.group(1) + '=' + m.group(2) + rewrite_srcset(m.group(3), from_dir) + m.group(2), txt)
        def esc(m):
            new = resolve(m.group(1).replace('\\/', '/') or '/', from_dir)
            return new.replace('/', '\\/') if new else m.group(0)
        txt = ESC.sub(esc, txt)
    txt = CSSURL.sub(lambda m: 'url(' + m.group(1) + (resolve(m.group(2), from_dir) or m.group(2)) + m.group(1) + ')', txt)
    return txt

for s in slugs:
    src = os.path.join(PAGES, s, 'index.html')
    dst_dir = page_dirs[('/' + s + '/') if s else '/']
    os.makedirs(dst_dir, exist_ok=True)
    txt = open(src, encoding='utf-8').read()
    open(os.path.join(dst_dir, 'index.html'), 'w', encoding='utf-8').write(rewrite_text(txt, dst_dir))

for css in glob.glob(os.path.join(OUT, '**', '*.css'), recursive=True):
    txt = open(css, encoding='utf-8', errors='ignore').read()
    new = rewrite_text(txt, os.path.dirname(css), html=False)
    if new != txt: open(css, 'w', encoding='utf-8').write(new)

print('untouched refs:')
for k, v in sorted(untouched.items(), key=lambda x: -x[1]): print(' ', v, k)
