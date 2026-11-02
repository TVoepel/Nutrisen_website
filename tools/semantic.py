#!/usr/bin/env python3
"""Reader-friendly structure. Run last: python3 tools/semantic.py <site-root>

Safari's Reader, Firefox's Reader View and similar tools look for one <main>/<article> block and drop <header> blocks.
The IONOS theme only has <div> zones, so this wraps everything between the header zone and the footer zone in
<main id="main"><article> ... </article></main> and turns the <header> elements of the page content into <div>s
(same classes, so nothing changes visually). Safe to re-run."""
import glob, os, re, sys
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')

def zone_start(t, zone):
    i = t.find('data-zone-type="%s"' % zone)
    return -1 if i < 0 else t.rfind('<div', 0, i + 1)

def process(f):
    t = open(f, encoding='utf-8').read()
    if '<main id="main"' in t: return False
    hs, fs = zone_start(t, 'header'), zone_start(t, 'footer')
    if hs < 0 or fs < 0: return False
    depth, end = 0, None
    for m in re.finditer(r'<div\b|</div>', t[hs:fs]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0: end = hs + m.end(); break
    if end is None or end >= fs: return False
    body = t[end:fs]
    body = re.sub(r'<header\b', '<div', body); body = body.replace('</header>', '</div>')
    t = t[:end] + '\n<main id="main"><article>' + body.strip('\n') + '</article></main>\n' + t[fs:]
    open(f, 'w', encoding='utf-8').write(t)
    return True

n = 0
for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
    if os.path.relpath(f, ROOT).startswith(('wp-content', 'tools', 'assets')): continue
    n += process(f)
print('semantic: main/article added on %d pages' % n)
