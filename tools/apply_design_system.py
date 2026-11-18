#!/usr/bin/env python3
"""Apply the NutriSen design system (the same visual language as the pitch decks) to the site.

Every page gets assets/ds.css (tokens, Fira Sans, all shared components in the new look) after lang.css.
The home pages (index.html, de/index.html) also get assets/ds-home.css, an UPPERCASE eyebrow above every
section title and the blue closing call-to-action section.
Idempotent. Run after semantic.py (it needs the <article> wrapper), before cachebust.py:
    python3 tools/apply_design_system.py <site root>
"""
import glob, os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'

T = {
    'en': {
        'calc': 'Savings calculator · winter wheat',
        'awards': 'Recognition',
        'team': 'Team',
        'close_eyebrow': 'Next steps',
        'close_title': "Let's plan the 2027 season together",
        'g1_title': 'Farms &amp; agronomists',
        'g1_text': 'Free pilot for farms in Bavaria: measure the nitrate in your plant sap on the field and fertilize what the crop needs.',
        'g1_link': 'See how it works', 'g1_href': 'agriculture/how-does-it-work/',
        'g2_title': 'Medical-device makers',
        'g2_text': 'Glucose is tested in human blood (TRL 5), lactate and creatinine are validated in the lab (TRL 4). Your device, with better data.',
        'g2_link': 'Explore the platform', 'g2_href': 'medical/',
        'cta_text': 'Questions, pilots, partnerships: write to us.',
        'cta_btn': 'Test your field for free',
    },
    'de': {
        'calc': 'Ersparnisrechner · Winterweizen',
        'awards': 'Auszeichnungen',
        'team': 'Team',
        'close_eyebrow': 'Nächste Schritte',
        'close_title': 'Planen wir die Saison 2027 gemeinsam',
        'g1_title': 'Landwirte &amp; Berater',
        'g1_text': 'Kostenloses Pilotprojekt für Betriebe in Bayern: Messen Sie das Nitrat im Pflanzensaft direkt auf dem Feld und düngen Sie, was die Kultur braucht.',
        'g1_link': 'So funktioniert es', 'g1_href': 'agriculture/how-does-it-work/',
        'g2_title': 'Medizinprodukte-Hersteller',
        'g2_text': 'Glukose ist in menschlichem Blut getestet (TRL 5), Laktat und Kreatinin sind im Labor validiert (TRL 4). Ihr Gerät, mit besseren Daten.',
        'g2_link': 'Plattform entdecken', 'g2_href': 'medical/',
        'cta_text': 'Fragen, Pilotprojekte, Partnerschaften: Schreiben Sie uns.',
        'cta_btn': 'Feld kostenlos testen',
    },
}


def eyebrow(text):
    return '<p class="ds-eyebrow">%s</p>' % text


def closing(s):
    mail = 'info@nutrisen.eu'
    return ('<section class="ds-close" aria-labelledby="ds-close-h"><div class="ds-wrap">' + eyebrow(s['close_eyebrow']) +
            '<h2 id="ds-close-h">%s</h2><div class="ds-close-grid">' % s['close_title'] +
            '<div class="ds-goal"><div class="ds-goal-head"><span class="ds-num" aria-hidden="true">1</span><h3>%s</h3></div><p>%s</p><a href="%s">%s</a></div>'
            % (s['g1_title'], s['g1_text'], s['g1_href'], s['g1_link']) +
            '<div class="ds-goal"><div class="ds-goal-head"><span class="ds-num" aria-hidden="true">2</span><h3>%s</h3></div><p>%s</p><a href="%s">%s</a></div>'
            % (s['g2_title'], s['g2_text'], s['g2_href'], s['g2_link']) +
            '<div class="ds-cta-card"><a class="ds-mail" href="mailto:%s">%s</a><p>%s</p><a class="ds-btn" href="agriculture/test-your-field/">%s</a></div>'
            % (mail, mail, s['cta_text'], s['cta_btn']) +
            '</div></div></section>')


def apply(path, lang, css):
    t = open(path, encoding='utf-8').read()
    if 'ds-home.css' in t:
        print('%s: already applied' % path)
        return
    s = T[lang]
    # style sheet after lang.css, so it wins over home-split.css and brand.css
    m = re.search(r'<link rel="stylesheet" href="[^"]*ds\.css[^"]*">', t)
    assert m, 'ds.css link not found in ' + path
    t = t[:m.end()] + '\n<link rel="stylesheet" href="%s">' % css + t[m.end():]
    # eyebrows
    n = 0
    t, k = re.subn(r'(<div class="ns-calc-in">)(<h2 id="ns-calc-h">)', r'\1' + eyebrow(s['calc']) + r'\2', t, count=1); n += k
    t, k = re.subn(r'(<div class="nb-wrap">)(<h2 class="nb-h2 nb-center">)', r'\1' + eyebrow(s['awards']) + r'\2', t, count=1); n += k
    t, k = re.subn(r'(<div class="nb-wrap">)(<h2 class="nb-h2">)', r'\1' + eyebrow(s['team']) + r'\2', t, count=1); n += k
    assert n == 3, 'expected 3 section titles in %s, found %d' % (path, n)
    # blue closing section at the end of the page content
    assert t.count('</article>') == 1, 'expected one </article> in ' + path
    t = t.replace('</article>', closing(s) + '</article>', 1)
    open(path, 'w', encoding='utf-8').write(t)
    print('%s: applied' % path)


def color_scheme_meta():
    """<meta name="color-scheme" content="only light"> after the viewport meta: the site has no dark mode, so browsers
    with an automatic dark theme (e.g. Chrome on Android) leave it light."""
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(('wp-content', 'tools', 'assets', 'design-system')): continue
        t = open(f, encoding='utf-8').read()
        if 'name="color-scheme"' in t: continue
        m = re.search(r'<meta name="viewport"[^>]*>', t)
        if not m: print('skipped (no viewport meta):', rel); continue
        t = t[:m.end()] + '\n<meta name="color-scheme" content="only light">' + t[m.end():]
        open(f, 'w', encoding='utf-8').write(t); n += 1
    print('color-scheme meta on %d pages' % n)


def link_site_css():
    """ds.css right after lang.css on every page (lang.css is on every page)."""
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(('wp-content', 'tools', 'assets', 'design-system')): continue
        t = open(f, encoding='utf-8').read()
        if re.search(r'assets/ds\.css', t): continue
        m = re.search(r'<link rel="stylesheet" href="((?:\.\./)*)assets/lang\.css[^"]*">', t)
        if not m:
            print('skipped (no lang.css):', rel); continue
        t = t[:m.end()] + '\n<link rel="stylesheet" href="%sassets/ds.css">' % m.group(1) + t[m.end():]
        open(f, 'w', encoding='utf-8').write(t); n += 1
    print('ds.css linked on %d pages' % n)


link_site_css()
color_scheme_meta()
apply(os.path.join(ROOT, 'index.html'), 'en', 'assets/ds-home.css')
apply(os.path.join(ROOT, 'de', 'index.html'), 'de', '../assets/ds-home.css')
