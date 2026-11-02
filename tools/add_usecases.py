#!/usr/bin/env python3
"""Add the agriculture "Use cases" (practice cases) page and a nav entry on every page.
Run after build.py / apply_home_split.py and BEFORE i18n.py. Usage: python3 tools/add_usecases.py <site root>"""
import os, re, sys, posixpath, uuid
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
NEW = 'agriculture/use-cases'
if os.path.exists(os.path.join(ROOT, NEW, 'index.html')): sys.exit('already applied')
PAGES = ['', 'medical', 'agriculture', 'agriculture/how-does-it-work', 'agriculture/test-your-field',
         'agriculture/from-lab-to-field', 'impressum', 'datenschutzerklarung']
TEST_ID = 'd315b558-9278-46a3-a2c5-8ad72f69d387'
NEW_ID = 'a4c1e5b2-7f3d-4e8a-9b60-2d5c8e1f7a93'
item = re.compile(r'(<div data-page-id="%s"[^>]*>)<div><a href="[^"]*" data-navigation-anchor="true"><span>Test your field </span></a></div></div>' % TEST_ID)

def add_nav(text, page_dir):
    href = posixpath.relpath(NEW, page_dir or '.') + '/'
    def r(m):
        tag = m.group(1).replace(TEST_ID, NEW_ID).replace(' navigation-selected', '')
        return tag + '<div><a href="%s" data-navigation-anchor="true"><span>Use cases </span></a></div></div>' % href + m.group(0)
    return item.sub(r, text)

texts = {}
for p in PAGES:
    f = os.path.join(ROOT, p, 'index.html'); t = open(f, encoding='utf-8').read()
    t = add_nav(t, p); texts[p] = t
    open(f, 'w', encoding='utf-8').write(t)

# ------------------------------------------------------------------ content
CASES = [  # farm, variety, fertilizer %, text left of bar, yield lines, economic
    ('1 · Bayern', 'KWS Emerick', -12, None, ['same yield'], '36 €/ha saved'),
    ('2 · Bayern', 'Kometus', -10, None, ['same yield'], '30 €/ha saved'),
    ('3 · Bayern', 'Wheat KWS Carusum', -30, None, ['same yield'], '90 €/ha saved'),
    ('4 · Niedersachsen', 'KWS Carusum', 25, 'within the DBE', ['+14 % extra yield'], '+150 €/ha revenue'),
    ('5 · Bayern', 'Spectral', -10, None, ['+5.5 % extra yield', '−4 % protein'], '30 €/ha saved'),
]
def pct(v): return ('+' if v > 0 else '−') + str(abs(v)) + ' %'
rows = []
for farm, var, v, within, yl, eco in CASES:
    w = round(abs(v) / 30 * 100, 1)
    fill = '<span class="ns-uc-fill" style="width:%s%%">%s</span>' % (w, pct(v))
    left = '<div class="ns-uc-half ns-uc-left">%s</div>' % ((('<span class="ns-uc-within">%s</span>' % within) if within else '') + (fill if v < 0 else ''))
    right = '<div class="ns-uc-half ns-uc-pos">%s</div>' % (fill if v > 0 else '')
    rows.append('<tr><th scope="row"><b>%s</b><span>%s</span></th>'
                '<td data-label="Fertilizer amount compared to DBE"><div class="ns-uc-axis" role="img" aria-label="%s">%s%s</div></td>'
                '<td class="ns-uc-yield" data-label="Yield">%s</td><td class="ns-uc-eco" data-label="Economic result">%s</td></tr>'
                % (farm.replace('·', '&middot;'), var, pct(v), left, right, ''.join('<span>%s</span>' % y for y in yl), eco))
BODY = '''<div class="ns-uc">
<section class="ns-uc-hero"><div class="ns-uc-wrap">
<p class="ns-uc-eyebrow">Results from practice</p>
<h1>Practice cases 2025/2026: <span>less fertilizer, same or higher yield</span></h1>
<ul class="ns-uc-kpis">
<li><b>up to −30 %</b><span>fertilizer compared to the standard recommendation</span></li>
<li><b>up to +14 %</b><span>extra yield</span></li>
<li><b>up to 90 €/ha</b><span>fertilizer costs saved</span></li>
<li><b>up to +150 €/ha</b><span>extra revenue</span></li>
</ul></div></section>
<div class="ns-uc-wrap"><div class="ns-uc-card">
<table class="ns-uc-table"><caption>Practice cases 2025/2026</caption>
<thead><tr><th scope="col">Farm &middot; variety</th><th scope="col" class="ns-uc-col-bar">Fertilizer amount compared to DBE</th><th scope="col">Yield</th><th scope="col">Economic result</th></tr></thead>
<tbody>
@@ROWS@@
</tbody></table>
<p class="ns-uc-foot">DBE = fertilizer requirement assessment (Düngebedarfsermittlung) under the German Fertilizer Ordinance (standard recommendation). Fertilizer costs: 30 €/ha per 10 % of fertilizer.</p>
<p class="ns-uc-foot">Results of individual farms. Actual savings and yields depend on site, variety and season.</p>
</div>
<div class="ns-uc-cta"><div><h2>Curious what your field needs?</h2><p>We are looking for partner farms in Bayern and test the nitrate status of your plants for free.</p></div>
<div class="ns-uc-actions"><a class="ns-uc-btn" href="../test-your-field/">Test your field for free</a><a class="ns-uc-link" href="../how-does-it-work/">See how it works</a></div></div>
<div class="ns-uc-space"></div></div>
</div>
'''.replace('@@ROWS@@', '\n'.join(rows))

# ------------------------------------------------------------------ assemble page from the how-does-it-work shell
t = texts['agriculture/how-does-it-work']
start = t.find('<!-- /wp:go-x/section -->') + len('<!-- /wp:go-x/section -->')       # end of header
end = t.find('<!-- wp:go-x/section', t.find('data-zone-type="footer"') - 6000)     # footer opener
end = max(m.start() for m in re.finditer(r'<!-- wp:go-x/section ', t[:t.find('data-zone-type="footer"')]))
assert 'data-zone-type="content"' in t[start:end] and start < end
t = t[:start] + '\n' + BODY + '\n' + t[end:]
# nav: select "Use cases" instead of "How does it work"
t = t.replace(' navigation-selected', '', 0)
t = re.sub(r'(<div data-page-id="b10b79d3[^>]*class="[^"]*?) navigation-selected', r'\1', t)
t = re.sub(r'(<div data-page-id="%s"[^>]*class="[^"]*?)"' % NEW_ID, r'\1 navigation-selected"', t)
t = re.sub(r'<a href="[^"]*" data-navigation-anchor="true"><span>How does it work', lambda m: m.group(0), t)
# "How does it work" items on this page must link to ../how-does-it-work/ (they pointed at ./ as the selected page)
t = re.sub(r'(<div data-page-id="b10b79d3[^>]*><div><a href=")\./(")', r'\1../how-does-it-work/\2', t)
t = re.sub(r'(<div data-page-id="%s"[^>]*><div><a href=")[^"]*(")' % NEW_ID, r'\1./\2', t)
t = re.sub(r'<title>[^<]*</title>', '<title>Use cases: less fertilizer, same or higher yield</title>', t, count=1)
t = re.sub(r'(<meta\s+name="description" content=")[^"]*(")',
           r'\1Five practice cases 2025/2026: up to 30 % less fertilizer at the same yield, or up to 14 % more yield.\2', t, count=1, flags=re.S)
t = t.replace('</head>', '<link rel="stylesheet" href="../../assets/usecases.css">\n</head>', 1)
os.makedirs(os.path.join(ROOT, NEW), exist_ok=True)
open(os.path.join(ROOT, NEW, 'index.html'), 'w', encoding='utf-8').write(t)
print('added', NEW)
