#!/usr/bin/env python3
"""Contact form without a WordPress backend. Run after optimize.py (before seo.py): python3 tools/contact_form.py <site-root>

The old form script (wp-content/plugins/go-x-blocks/js/forms/forms.js) posts to /wp-admin/admin-ajax.php, which does not exist on static hosting.
assets/contact.js takes its place (it provides the same window.FormProcessor entry point the page already calls) and posts to contact.php.
Safe to re-run."""
import os, re, sys
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
n = 0
for rel in ('agriculture/test-your-field', 'de/agriculture/test-your-field'):
    f = os.path.join(ROOT, rel, 'index.html')
    if not os.path.exists(f): continue
    t = open(f, encoding='utf-8').read()
    up = '../' * (rel.count('/') + 1)
    new = re.sub(r'<script id="gox-script-0-js" src="[^"]*forms/forms\.js"></script>', '<script id="gox-script-0-js" src="%sassets/contact.js"></script>' % up, t)
    # the phone link of the original site points to a placeholder number; the visible number is +49 231 13707127
    new = new.replace('href="tel:001555123456789"', 'href="tel:+4923113707127"')
    if new != t: open(f, 'w', encoding='utf-8').write(new); n += 1
print('contact_form: %d pages switched to assets/contact.js' % n)
