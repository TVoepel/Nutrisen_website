#!/usr/bin/env python3
"""Reader mode (Safari Reader, Firefox Reader View, Readability): keep the full page content.

Readers drop boxes that look like navigation: short boxes where links make up more than about 20% of the text,
unless the class name marks them as content ("content", "text", "article", ...). They also drop low-scoring
headers next to the main text. This script adds the class token `ds-content` to the content boxes of every page
(no visual effect) and gives the home closing cards a heading without an extra wrapper box.
Idempotent. Run after apply_design_system.py, before cachebust.py:  python3 tools/reader_mode.py <site root>"""
import glob, os, re, sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
TOKEN = 'ds-content'
# content boxes (first class of the element); headers next to the main text are included
BOXES = ('nb', 'ns-uc', 'ns-fc', 'ns-blog', 'nb-wrap', 'nb-card', 'nb-hero', 'nb-tl-item', 'ns-calc-in', 'ns-calc-out', 'ns-blog-hero', 'ns-uc-hero', 'ns-uc-card',
         'ns-fc-hero', 'ns-fc-card', 'ds-goal', 'ds-cta-card', 'ns-inner')
CLS = re.compile(r'class="((?:%s)(?:\s[^"]*)?)"' % '|'.join(re.escape(b) for b in BOXES))
GOAL = re.compile(r'<div class="ds-goal-head">(<span class="ds-num" aria-hidden="true">\d</span>)<h3>(.*?)</h3></div>')

n = 0
for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith(('wp-content', 'tools', 'assets', 'design-system')): continue
    t = open(f, encoding='utf-8').read()
    new = CLS.sub(lambda m: m.group(0) if TOKEN in m.group(1).split() else 'class="%s %s"' % (m.group(1).rstrip(), TOKEN), t)
    new = GOAL.sub(r'<h3 class="ds-goal-head">\1\2</h3>', new)
    # cards with a heading and short paragraphs only (contact card): a <section> is not dropped by the readers' clean-up of
    # linky boxes, which on short pages runs without class weights
    new = re.sub(r'<div class="(nb-card ds-content)">(<h2>(?:(?!<div|</div>).)*?)</div>', r'<section class="\1">\2</section>', new, flags=re.S)
    # the article itself is content too, so readers keep the whole page as one text
    new = new.replace('<main id="main"><article>', '<main id="main"><article class="%s">' % TOKEN, 1)
    if new != t:
        open(f, 'w', encoding='utf-8').write(new); n += 1
print('reader_mode: updated %d pages' % n)
