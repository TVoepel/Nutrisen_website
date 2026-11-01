#!/usr/bin/env python3
"""Replace the two stacked homepage banners with the audience-split hero (assets/home-split.css).
Idempotent. Usage: python3 tools/apply_home_split.py <site root>   (run after tools/build.py)"""
import os, re, sys
from PIL import Image   # pip install pillow
root = sys.argv[1] if len(sys.argv) > 1 else '.'
p = os.path.join(root, 'index.html')
t = open(p, encoding='utf-8').read()
if 'class="ns-split"' in t:
    sys.exit('already applied')
starts = [m.start() for m in re.finditer(r'<div data-zone-type="content" class="section section-root', t)]
a = next(s for s in starts if s > t.find('<!-- /wp:go-x/section -->'))          # first section after the header
b = max(s for s in starts if s < t.find('People are excited'))
assert t.find('Real-time nutrient sensing') > a and t.find('Direct molecular sensing') < b, 'unexpected layout'
AG = 'wp-content/uploads/go-x/u/6a085a64-991b-4982-8977-a632194db683/image.jpg'
MD = 'wp-content/uploads/go-x/u/e4fbeee7-9d69-4d62-8d2d-2e68bdb021aa/image.jpg'
BOOK = '//outlook.office365.com/owa/calendar/Meetingswithpartners@livesen.eu/bookings/'
def variants(src, name):
    im = Image.open(os.path.join(root, src)).convert('RGB'); os.makedirs(os.path.join(root, 'assets'), exist_ok=True)
    for w in (960, 1600):
        v = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        v.save(os.path.join(root, 'assets', f'hero-{name}-{w}.webp'), 'WEBP', quality=68, method=6)
    return f'assets/hero-{name}-960.webp 960w,assets/hero-{name}-1600.webp 1600w', round(im.height * 1600 / im.width)
AG_SET, AG_H = variants(AG, 'agri'); MD_SET, MD_H = variants(MD, 'med')
def bg(sset, h, first):
    return (f'<img class="ns-bg" src="{sset.split()[0]}" srcset="{sset}" sizes="(max-width:860px) 100vw,50vw" width="1600" height="{h}" alt="" decoding="async" '
            + ('fetchpriority="high"' if first else 'loading="lazy"') + '>')
html = f'''<section class="ns-split" aria-label="Choose your field">
<div class="ns-panel ns-panel--ag">{bg(AG_SET, AG_H, True)}<div class="ns-inner">
<span class="ns-tag">For farmers &amp; agronomists</span>
<h2>Real-time nutrient sensing for smart fertilization</h2>
<p class="ns-lead">Measure the nitrate in your plants' sap directly on the field and fertilize exactly what the crop needs.</p>
<ul class="ns-stats"><li><b>20% less</b><span>fertilizer on average, about 80&#8364; per ha</span></li><li><b>up to +10%</b><span>yield, about 240&#8364; extra per ha</span></li></ul>
<div class="ns-cta"><a class="ns-btn" href="agriculture/test-your-field/">Test your field for free</a><a class="ns-more" href="agriculture/how-does-it-work/">See how it works</a></div>
<p class="ns-note">Free pilot for farms in Bayern. *Calculated for wheat, December 2022 prices.</p>
</div></div>
<span class="ns-or" aria-hidden="true">or</span>
<div class="ns-panel ns-panel--med">{bg(MD_SET, MD_H, False)}<div class="ns-inner">
<span class="ns-tag">For medical-device makers</span>
<h2>Direct molecular sensing for enabling digital health</h2>
<p class="ns-lead">We build electrochemical biosensors that measure molecules in body fluids with high precision. Your device, with better data.</p>
<ul class="ns-stats"><li><b>Lactate</b><span>ready to be deployed (TRL 5)</span></li><li><b>Creatinine</b><span>experimental PoC (TRL 3)</span></li></ul>
<div class="ns-cta"><a class="ns-btn" href="{BOOK}" target="_blank" rel="noopener">Schedule a meeting</a><a class="ns-more" href="medical/">Explore the platform</a></div>
</div></div>
</section>
<div class="ns-trust"><b>Award-winning team:</b> 3rd place Innovationspreis Moderne Landwirtschaft &middot; 2nd place Bio-Security B&#246;nen &middot; 3rd prize Plan B Pitch Competition 2022</div>
'''
t = t[:a] + html + t[b:]
t = t.replace('</head>', '<link rel="stylesheet" href="assets/home-split.css">\n</head>', 1)
open(p, 'w', encoding='utf-8').write(t)
print('applied: replaced', b - a, 'bytes of banners')
