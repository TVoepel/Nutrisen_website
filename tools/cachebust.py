#!/usr/bin/env python3
"""Cache busting. Run last: python3 tools/cachebust.py <site-root>

The server caches CSS and JavaScript for a long time (see .htaccess and _headers). So every local assets/*.css and assets/*.js
reference in the pages gets ?v=<hash of the file>. A changed file gets a new address, visitors never see an old style sheet.
Safe to re-run: an existing ?v=... is replaced."""
import glob, hashlib, os, re, sys
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
REF = re.compile(r'''((?:href|src)=["'])((?:\.\./)*assets/[^"'?#]+\.(?:css|js))(?:\?v=[0-9a-f]+)?(["'])''')
cache = {}
def ver(path):
    if path not in cache:
        cache[path] = hashlib.sha1(open(path, 'rb').read()).hexdigest()[:8] if os.path.exists(path) else None
    return cache[path]
n = 0
for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith(('wp-content', 'tools', 'assets')): continue
    t = open(f, encoding='utf-8').read()
    def sub(m):
        target = os.path.normpath(os.path.join(os.path.dirname(f), m.group(2)))
        v = ver(target)
        return m.group(0) if not v else '%s%s?v=%s%s' % (m.group(1), m.group(2), v, m.group(3))
    new = REF.sub(sub, t)
    if new != t: open(f, 'w', encoding='utf-8').write(new); n += 1
print('cachebust: updated %d pages' % n)
