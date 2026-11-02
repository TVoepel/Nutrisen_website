#!/usr/bin/env python3
"""Remove pages that are no longer part of the site (run first). Usage: python3 tools/prune.py <site root>"""
import os, shutil, sys
root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
for d in ('the-npknowledge',):   # unlinked placeholder page with lorem ipsum text
    if os.path.isdir(os.path.join(root, d)): shutil.rmtree(os.path.join(root, d)); print('removed', d)
