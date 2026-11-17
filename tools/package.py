#!/usr/bin/env python3
"""Make the upload package for the web hosting: python3 tools/package.py [output.zip]
Contains exactly what belongs on the server. Left out: tools/, design-system/, .github/, .git/, README.md, DEPLOY-IONOS.md, .gitignore."""
import os, sys, zipfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'nutrisen-site.zip'))
SKIP_DIRS = {'tools', 'design-system', '.github', '.git', '__pycache__', 'node_modules'}
SKIP_FILES = {'README.md', 'DEPLOY-IONOS.md', '.gitignore', os.path.basename(OUT)}
n = size = 0
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        for f in sorted(files):
            if f in SKIP_FILES or f.endswith('.zip'): continue
            p = os.path.join(d, f); z.write(p, os.path.relpath(p, ROOT)); n += 1; size += os.path.getsize(p)
print('%s: %d files, %.1f MB unpacked, %.1f MB zipped' % (OUT, n, size / 1e6, os.path.getsize(OUT) / 1e6))
