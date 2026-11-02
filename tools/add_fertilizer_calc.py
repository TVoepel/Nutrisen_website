#!/usr/bin/env python3
"""Add the NutriSen fertilizer calculator page (/agriculture/calculator/) and a menu entry on every page.
Run after add_usecases.py and BEFORE i18n.py. Prices come from assets/fertilizer-prices.json (tools/fetch_prices.py).
Usage: python3 tools/add_fertilizer_calc.py <site root>"""
import os, re, sys, posixpath
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
NEW = 'agriculture/calculator'
if os.path.exists(os.path.join(ROOT, NEW, 'index.html')): sys.exit('already applied')
PAGES = ['', 'medical', 'agriculture', 'agriculture/how-does-it-work', 'agriculture/use-cases', 'agriculture/test-your-field',
         'agriculture/from-lab-to-field', 'impressum', 'datenschutzerklarung']
TEST_ID = 'd315b558-9278-46a3-a2c5-8ad72f69d387'; NEW_ID = 'c7d2f1a8-3b5e-4c90-8e41-6a9b0d2e5f17'
item = re.compile(r'(<div data-page-id="%s"[^>]*>)<div><a href="[^"]*" data-navigation-anchor="true"><span>Test your field </span></a></div></div>' % TEST_ID)
def add_nav(t, d):
    href = posixpath.relpath(NEW, d or '.') + '/'
    return item.sub(lambda m: m.group(1).replace(TEST_ID, NEW_ID).replace(' navigation-selected', '') +
                    '<div><a href="%s" data-navigation-anchor="true"><span>Calculator </span></a></div></div>' % href + m.group(0), t)
texts = {}
for p in PAGES:
    f = os.path.join(ROOT, p, 'index.html'); texts[p] = add_nav(open(f, encoding='utf-8').read(), p); open(f, 'w', encoding='utf-8').write(texts[p])

BODY = '''<div class="ns-fc">
<section class="ns-fc-hero"><div class="ns-fc-wrap">
<p class="ns-fc-eyebrow">Fertilizer calculator</p>
<h1>NutriSen fertilizer calculator: <span>compare 3 applications</span></h1>
<p class="ns-fc-lead">Compare your usual fertilization with a NutriSen optimized one. Fertilizer prices are suggested from official EU data and can be replaced by your own purchase prices.</p>
</div></section>
<div class="ns-fc-wrap">
<div id="ns-fc-app" class="ns-fc-app"><noscript><div class="ns-fc-card">This calculator needs JavaScript.</div></noscript></div>
<div class="ns-fc-cta"><div><h2>Want exact numbers for your fields?</h2><p>Our sensors and the fertilization platform show what each field really needs.</p></div>
<a class="ns-fc-btn" href="../test-your-field/">Test your field for free</a></div>
<p class="ns-fc-disc">May contain market data from the source: European Commission – Agri-food data portal (agridata.ec.europa.eu). These are aggregated EU market data reported by the Member States. No liability is accepted for the up-to-date accuracy of this data or for trading decisions or losses resulting from it. The European Commission, for its part, excludes any liability for the use of its API and portal data. All other prices in this calculator are based on the user's own purchase prices entered by the user.</p>
<p class="ns-fc-disc">Suggested fertilizer prices come, where shown, from the Eurostat dataset apri_aip_ft “Purchase prices for fertilisers” (annual average 2025, per tonne of nutrient, marked provisional by Eurostat). Values that differ strongly from the EU median are not used. The disclaimer above applies accordingly.</p>
<p class="ns-fc-disc">Sources: <a href="https://ec.europa.eu/eurostat/databrowser/view/apri_aip_ft" target="_blank" rel="noopener">Eurostat apri_aip_ft</a> · <a href="https://agridata.ec.europa.eu/extensions/DashboardFertiliser/FertiliserPrices.html" target="_blank" rel="noopener">EU Agri-food data portal</a></p>
</div></div>
<script src="../../assets/fcalc.js" defer></script>
'''
t = texts['agriculture/how-does-it-work']
start = t.find('<!-- /wp:go-x/section -->') + len('<!-- /wp:go-x/section -->')
end = max(m.start() for m in re.finditer(r'<!-- wp:go-x/section ', t[:t.find('data-zone-type="footer"')]))
assert 'data-zone-type="content"' in t[start:end] and start < end
t = t[:start] + '\n' + BODY + '\n' + t[end:]
t = re.sub(r'(<div data-page-id="b10b79d3[^>]*class="[^"]*?) navigation-selected', r'\1', t)
t = re.sub(r'(<div data-page-id="%s"[^>]*class="[^"]*?)"' % NEW_ID, r'\1 navigation-selected"', t)
t = re.sub(r'(<div data-page-id="b10b79d3[^>]*><div><a href=")\./(")', r'\1../how-does-it-work/\2', t)
t = re.sub(r'(<div data-page-id="%s"[^>]*><div><a href=")[^"]*(")' % NEW_ID, r'\1./\2', t)
t = re.sub(r'<title>[^<]*</title>', '<title>NutriSen fertilizer calculator: compare 3 applications</title>', t, count=1)
t = re.sub(r'(<meta\s+name="description" content=")[^"]*(")', r'\1Compare your usual fertilization with NutriSen in three applications, with fertilizer price suggestions from official EU data.\2', t, count=1, flags=re.S)
t = t.replace('</head>', '<link rel="stylesheet" href="../../assets/fcalc.css">\n</head>', 1)
os.makedirs(os.path.join(ROOT, NEW), exist_ok=True)
open(os.path.join(ROOT, NEW, 'index.html'), 'w', encoding='utf-8').write(t)
print('added', NEW)
