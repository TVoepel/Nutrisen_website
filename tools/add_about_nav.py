#!/usr/bin/env python3
"""Add "About us" / "Über uns" (the page agriculture/from-lab-to-field/) to the main menu of every page,
right after "At a glance" / "Auf einen Blick", in the desktop menu, the mobile menu and the footer menu.
Idempotent. Run after add_blog.py, i18n.py and contact_form.py:  python3 tools/add_about_nav.py <site root>"""
import glob, os, re, sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
FACT = 'b7d2f4a1-3c68-4e19-a5d0-9e8f1c2b7a43'   # nav item "At a glance"
ABOUT = 'c41e8a92-6d3b-4f7a-9b25-1e0d7c3a5f68'  # nav item "About us" (new)
SLUG = 'agriculture/from-lab-to-field/'
LABEL = {'en': 'About us', 'de': 'Über uns'}
WRAP = '<div class="navigation-menu-item-wrapper">'
ITEM = re.compile(r'(?P<wrap><div class="navigation-menu-item-wrapper">)?'
                  r'(?P<open><div data-page-id="%s"[^>]*class="(?P<cls>[^"]*)">)'
                  r'<div><a href="(?P<href>[^"]*?)(?:nutrisen-at-a-glance/|\./)"(?P<rest>[^>]*)><span>[^<]*</span></a></div></div>'
                  r'(?P<close></div>)?' % FACT)

n = 0
for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
    rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
    if rel.startswith(('wp-content', 'tools', 'assets', 'design-system')): continue
    t = open(f, encoding='utf-8').read()
    if ABOUT in t or FACT not in t: continue
    lang = 'de' if rel.startswith('de/') else 'en'
    here = rel in (SLUG + 'index.html', 'de/' + SLUG + 'index.html')
    glance = rel in ('nutrisen-at-a-glance/index.html', 'de/nutrisen-at-a-glance/index.html')

    def add(m):
        cls = m.group('cls').replace(' navigation-selected', '') + (' navigation-selected' if here else '')
        op = m.group('open').replace(FACT, ABOUT).replace(m.group('cls'), cls)
        href = '../' if glance else m.group('href')   # on the facts page itself the item links to "./"
        item = op + '<div><a href="%s%s"%s><span>%s </span></a></div></div>' % (href, SLUG, m.group('rest'), LABEL[lang])
        if m.group('wrap'):                      # item in its own wrapper: add a new wrapper after it
            return m.group(0) + WRAP + item + '</div>'
        close = m.group('close') or ''           # bare item: the </div> belongs to the parent, keep it last
        return m.group(0)[:len(m.group(0)) - len(close)] + item + close

    t, k = ITEM.subn(add, t)
    if k:
        open(f, 'w', encoding='utf-8').write(t); n += 1
print('add_about_nav: updated %d pages' % n)
