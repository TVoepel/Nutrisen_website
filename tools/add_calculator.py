#!/usr/bin/env python3
"""Add the interactive savings calculator to the home and agriculture pages (CSS and JS are inlined: zero extra requests).
Run after add_usecases.py and BEFORE i18n.py. Also lets the contact page pre-fill the farm size from ?ha=.
Usage: python3 tools/add_calculator.py <site root>"""
import os, re, sys
root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
here = os.path.dirname(os.path.abspath(__file__))
css = open(os.path.join(here, '..', 'assets', 'calc.css'), encoding='utf-8').read()
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S); css = re.sub(r'\s*([{};:,])\s*', r'\1', css).strip()
js = open(os.path.join(here, '..', 'assets', 'calc.js'), encoding='utf-8').read().strip()

def section(prefix):
    return f'''<section class="ns-calc" aria-labelledby="ns-calc-h"><style>{css}</style><div class="ns-calc-card">
<div class="ns-calc-in"><h2 id="ns-calc-h">What could NutriSen save on your farm?</h2><p>Move the slider to your farm size.</p>
<div class="ns-calc-row"><label for="ns-ha">Your farm size</label><output id="ns-ha-out" for="ns-ha" aria-live="polite">100 ha</output></div>
<input id="ns-ha" type="range" min="10" max="1000" step="10" value="100"><div class="ns-calc-scale" aria-hidden="true"><span>10 ha</span><span>1,000 ha</span></div></div>
<div class="ns-calc-out"><div><b data-calc="save">€8,000</b><span class="l">fertilizer costs saved per year, about 80 € per ha</span></div>
<div><b><em>up to</em> <span data-calc="gain">€24,000</span></b><span class="l">extra revenue per year, up to 240 € per ha</span></div>
<a class="ns-calc-btn" href="{prefix}agriculture/test-your-field/">Test your field for free</a>
<small>Average values for wheat, December 2022 prices. Results vary by farm, see the <a href="{prefix}agriculture/use-cases/">practice cases</a>.</small>
<a class="ns-calc-more" href="{prefix}agriculture/calculator/">Compare your own fertilization in detail</a></div></div>
<script>{js}</script></section>
'''

def put(page, marker, prefix):
    f = os.path.join(root, page, 'index.html'); t = open(f, encoding='utf-8').read()
    if 'class="ns-calc"' in t: sys.exit('already applied')
    starts = [m.start() for m in re.finditer(r'<div data-zone-type="content" class="section section-root', t)]
    at = max(s for s in starts if s < t.find(marker))
    t = t[:at] + section(prefix) + t[at:]
    open(f, 'w', encoding='utf-8').write(t)

put('', 'People are excited', '')
put('agriculture', 'Per year, we aim to save for Europe', '../')

# contact page: pre-fill the farm size chosen in the calculator
f = os.path.join(root, 'agriculture/test-your-field/index.html'); t = open(f, encoding='utf-8').read()
pre = ('<script>addEventListener("load",function(){var m=/[?&]ha=(\\d{1,5})/.exec(location.search),a=document.querySelector("textarea");'
       'if(m&&a&&!a.value){a.value=(document.documentElement.lang==="de"?"Betriebsgröße: ":"Farm size: ")+m[1]+" ha";a.dispatchEvent(new Event("input",{bubbles:true}))}})</script>')
t = t.replace('</body>', pre + '</body>', 1)
open(f, 'w', encoding='utf-8').write(t)
print('calculator added')
