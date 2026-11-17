#!/usr/bin/env python3
"""Apply the NutriSen corporate design (assets/brand.css) to the pages that still had the old look:
home (awards and team), medical, agriculture, how-does-it-work, test-your-field, from-lab-to-field, impressum,
datenschutzerklarung. Texts and images are taken from the existing pages, so all translations keep working.
Run after add_blog.py and BEFORE i18n.py. Needs Pillow. Usage: python3 tools/restyle.py <site root>"""
import os, re, sys, html, posixpath
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_strings as T

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
E = lambda x: html.escape(x, quote=False)
A = lambda x: html.escape(x, quote=True)
BOOK = 'mailto:info@nutrisen.eu?subject=NutriSen%20Medical'

def rd(p): return open(os.path.join(ROOT, p, 'index.html'), encoding='utf-8').read()
def wr(p, t): open(os.path.join(ROOT, p, 'index.html'), 'w', encoding='utf-8').write(t)
def S(prefix):   # exact English text of an existing translation key (guarantees the DE translation keeps working)
    keys = [k for k in T.DE if k.startswith(prefix)]
    assert len(keys) == 1, (prefix, keys)
    return keys[0]
def L(page, target):   # relative page link
    return posixpath.relpath(target, page or '.') + '/'

# ---------------------------------------------------------------- source helpers
def find_img(t, idpart):
    m = re.search(r'<img\b[^>]*src="[^"]*%s[^"]*"[^>]*>' % re.escape(idpart), t)
    assert m, idpart
    tag = m.group(0)
    return re.search(r'\bsrc="([^"]+)"', tag).group(1), (re.search(r'\bsrcset="([^"]+)"', tag) or [None, None])[1]
def IMG(t, idpart, alt, sizes, cls=''):
    src, srcset = find_img(t, idpart)
    return '<img%s src="%s"%s sizes="%s" alt="%s" decoding="async">' % (
        ' class="%s"' % cls if cls else '', src, ' srcset="%s"' % srcset if srcset else '', sizes, A(alt))
def variants(t, page, idpart, name):
    m = re.search(r"url\('([^']*%s[^']*)'\)" % re.escape(idpart), t); assert m, idpart
    im = Image.open(os.path.normpath(os.path.join(ROOT, page, m.group(1)))).convert('RGB'); os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
    widths = sorted({w for w in (640, 960, 1600) if w < im.width} | {min(im.width, 1600)}); out = []
    for w in widths:
        v = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS) if w != im.width else im
        v.save(os.path.join(ROOT, 'assets', 'hero-%s-%d.webp' % (name, w)), 'WEBP', quality=68, method=6)
        out.append('%s %dw' % (posixpath.relpath('assets/hero-%s-%d.webp' % (name, w), page or '.'), w))
    return out[-1].split()[0], ','.join(out), widths[-1], round(im.height * widths[-1] / im.width)
def hero(t, page, bg, eyebrow, h1, lead='', actions='', sm=False):
    img = ''
    if bg:
        src, srcset, w, h = variants(t, page, bg[0], bg[1])
        img = '<img class="nb-hero-bg" src="%s" srcset="%s" sizes="100vw" width="%d" height="%d" alt="" fetchpriority="high" decoding="async">' % (src, srcset, w, h)
    return ('<header class="nb-hero%s%s">%s<div class="nb-wrap">%s<h1>%s</h1>%s%s</div></header>'
            % (' nb-hero--img' if bg else '', ' nb-hero--sm' if sm else '', img,
               '<p class="nb-eyebrow">%s</p>' % E(eyebrow) if eyebrow else '', h1,
               lead, '<div class="nb-actions">%s</div>' % actions if actions else ''))
def btn(href, text, cls='', ext=False):
    return '<a class="nb-btn %s" href="%s"%s>%s</a>' % (cls, A(href), ' target="_blank" rel="noopener"' if ext else '', E(text))
def sec(inner, cls='', wrap='nb-wrap'): return '<section class="nb-section %s"><div class="%s">%s</div></section>' % (cls, wrap, inner)

def region(t):
    start = t.find('<!-- /wp:go-x/section -->') + len('<!-- /wp:go-x/section -->')
    end = max(m.start() for m in re.finditer(r'<!-- wp:go-x/section ', t[:t.find('data-zone-type="footer"')]))
    assert start < end
    return start, end
def put(t, page, body, css_rel=True, start=None):
    s, e = region(t); s = start if start is not None else s
    t = t[:s] + '\n<div class="nb">' + body + '</div>\n' + t[e:]
    return t.replace('</head>', '<link rel="stylesheet" href="%s">\n</head>' % posixpath.relpath('assets/brand.css', page or '.'), 1)
def take_calc(t):
    m = re.search(r'<section class="ns-calc".*?</section>\n?', t, re.S)
    return m.group(0) if m else ''

# ================================================================ MEDICAL
def medical():
    p = 'medical'; t = rd(p)
    cards = [('Get lab precision', 'Our biosensor platform can calibrate your device with high precision.'),
             ('Stay ahead', 'Digitalization is only powerful with good data. We can be your new USP.'),
             ('Innovate. Really.', 'The combination of tools is the secret for exceptional results.')]
    mols = [('Lactate', 'READY TO BE DEPLOYED', '(TRL 5)', 5), ('Creatinine', 'EXPERIMENTAL PoC', '(TRL 3)', 3), ('Cholesterol', 'CONCEPTUAL PHASE', '(TRL 2)', 2)]
    body = hero(t, p, ('e4fbeee7', 'pg-medical'), 'Medical', E('Biosensors for boosting digital health'),
                '<p class="nb-lead">%s</p>' % E('A sensor platform for every medical device.'), btn(BOOK, 'Get in touch'))
    body += sec('<h2 class="nb-h2">%s</h2><div class="nb-grid">%s</div>' % (E('Advance digitalization with better DATA'),
        ''.join('<div class="nb-card nb-card--accent"><h3>%s</h3><p>%s</p></div>' % (E(a), E(b)) for a, b in cards)))
    body += sec('<h2 class="nb-h2">%s</h2><div class="nb-grid" style="margin-top:28px">%s</div>%s' % (E('Overview of molecules in the pipeline'),
        ''.join('<div class="nb-card nb-mol"><h3>%s</h3><p class="nb-status">%s</p><p class="nb-trl">%s</p><div class="nb-bar" aria-hidden="true"><i style="width:%d%%"></i></div></div>' % (E(n), E(s), E(trl), round(v / 9 * 100)) for n, s, trl, v in mols),
        '<p class="nb-note nb-paper">Research behind the sensors: <a href="../blog/oxygen-scavenger-science-advances/">New in Science Advances: a universal oxygen scavenger for oxidase-based biosensors</a></p>'), 'nb-section--white')
    body += sec('<div class="nb-split"><div class="nb-media">%s</div><div><h2 class="nb-h2">%s</h2><p>%s</p><p>%s</p><p>%s</p><div class="nb-actions">%s</div></div></div>' % (
        IMG(t, '57d7a0fb', 'Proprietary biosensor plus your medical device', '(max-width:860px) 90vw, 480px'),
        E('We are all about R&D'), E('We build electrochemical biosensors to measure molecules in body fluids with high precision.'),
        E(S('If your medical device targets')), E("Let's see what we can revolutionize together."), btn(BOOK, 'Get in touch', 'nb-btn--blue')))
    wr(p, put(t, p, body))

# ================================================================ AGRICULTURE
def agriculture():
    p = 'agriculture'; t = rd(p); calc = take_calc(t)
    ben = [('saving fertilizers', 'ABOUT 15% LESS ON AVERAGE, UP TO 30%: savings of about 45€, up to 90€ per Ha.'), ('supporting yield', 'In some cases up to 10% higher yield is possible, depending on farm and season.'),
           ('being resilient', 'and cultivating now, the future of agriculture.')]
    stats = [('2 Million', 'TONS OF FERTILIZERS'), ('2 Billion €', 'IN FERTILIZER IMPORTS'), ('20 Million', 'TONS OF CO2')]
    body = hero(t, p, ('5f5c3656', 'pg-agri'), 'Agriculture', '%s <span>%s</span>' % (E('Real-time nutrient sensing'), E('for smart fertilization')),
                '<p class="nb-lead">%s</p>' % E('From Germany to every field.'),
                btn(L(p, 'agriculture/test-your-field'), 'Test your field for free') + '<a class="nb-link" href="%s">%s</a>' % (L(p, 'agriculture/how-does-it-work'), E('See how it works')))
    body += sec('<h2 class="nb-h2">%s</h2><div class="nb-grid" style="margin-top:24px">%s</div><p class="nb-note">%s</p>' % (E('Boost your experience and GROW by'),
        ''.join('<div class="nb-card nb-card--accent"><h3>%s</h3><p>%s</p></div>' % (E(a), E(b)) for a, b in ben), E('*values calculated for wheat farmers, fertilizer prices 2025–2026: 30€ per Ha for every 10% of fertilizer.')))
    body += '<!--calc-->'
    body += sec('<h2 class="nb-h2">%s</h2><div class="nb-stats">%s</div>' % (E('Per year, we aim to save for Europe'),
        ''.join('<div class="nb-stat"><b>%s</b><span>%s</span></div>' % (E(a), E(b)) for a, b in stats)), 'nb-section--navy nb-center')
    cols = [('7ae1b0c9', 'Proprietary biosensor test strip', [S('Exactly as a blood sugar test'), 'We bring laboratory precision to the field!']),
            ('9032af26-8241-484e-907e-b3d81dc094cf/l146', 'Satellite data', [S('We all know that fields')]),
            ('9032af26-8241-484e-907e-b3d81dc094cf/l1036', 'Fertilization platform', [S('All communication and information')])]
    cards = ''
    for i, (iid, alt, paras) in enumerate(cols):
        extra = '<div class="nb-actions" style="margin-top:auto;padding-top:14px">%s</div>' % btn(L(p, 'agriculture/how-does-it-work'), 'Check here how does it work', 'nb-btn--blue') if i == 0 else ''
        cards += '<div class="nb-card"><div class="nb-cardimg">%s</div>%s%s</div>' % (IMG(t, iid, alt, '(max-width:860px) 90vw, 340px'), ''.join('<p>%s</p>' % E(x) for x in paras), extra)
    body += sec('<div class="nb-grid">%s</div>' % cards)
    body += '<section class="nb-cta"><div class="nb-wrap"><h2>%s</h2><p>%s</p><div class="nb-actions">%s</div></div></section>' % (
        E('Do you have a farm in Bayern?'), E('We are looking for partners'), btn(L(p, 'agriculture/test-your-field'), 'Test your field for free', 'nb-btn--white'))
    t = put(t, p, body); t = t.replace('<!--calc-->', calc); wr(p, t)

# ================================================================ HOW DOES IT WORK
def how():
    p = 'agriculture/how-does-it-work'; t = rd(p)
    steps = [('81398fa8', 'App screen: registration complete', 'Register your field', [S('Get access to our fertilization'), "Don't worry, your data is yours and only yours."]),
             ('9c459f7f', 'Satellite map of a field in the app', 'Receive an overview', [S('By registering the fields')]),
             ('cef63917', 'App screen: upgrade to premium', 'Empower your data', ['Satellite data is a beginning, but not enough.', S('Upgrade your account')]),
             ('eeb01f52', 'Wheat plant, plant juice and sensor', 'Check your plants', [S('With the help of satellite'), S('There you can collect')]),
             ('be72870c', 'App screen with the nitrate result', 'Time is gold', [S('At the very spot'), S('Even without internet'), 'No more, no less.']),
             ('a3800af8', 'App screen: fertilizer amount per zone', 'A win-win situation', [S('NutriSen sensors can help'), S('This could mean savings'), '*fertilizer prices 2025–2026, wheat farmers: 30€ per Ha for every 10% of fertilizer'])]
    lead = ('<p class="nb-lead">%s <strong>%s</strong> %s</p><p class="nb-lead">%s <strong>%s</strong> %s</p>' % (
        E('Our sensors measure the'), E('exact amount of nutrients'), E('your plants have in the moment of the measurement.'),
        E('Through data retrieved from satellite platforms, we understand'), E('the variability of your field'), E('and calculate the needs for each condition.')))
    body = hero(t, p, None, 'How does it work', '%s <span>%s</span> %s' % (E('What if your plants'), E('could say'), E('exactly what they need?')), lead)
    body += sec('<div class="nb-steps">%s</div>' % ''.join(
        '<div class="nb-card nb-step"><div class="nb-cardimg">%s</div><h3>%s</h3>%s</div>' % (
            IMG(t, iid, alt, '(max-width:860px) 90vw, 330px'), E(title), ''.join('<p>%s</p>' % E(x) for x in paras)) for iid, alt, title, paras in steps))
    body += '<section class="nb-cta"><div class="nb-wrap"><div class="nb-split"><div>%s</div><div><h2>%s</h2><p>%s</p><p>%s</p><div class="nb-actions">%s</div></div></div></div></section>' % (
        IMG(t, '0e0edb61', 'The NutriSen team', '(max-width:860px) 90vw, 520px'), E("We've got your back"),
        E('Power up the experience that you have, with the technology we can provide.'), E(S("The climate and environment")),
        btn(L(p, 'agriculture/test-your-field'), 'Test your field', 'nb-btn--white'))
    wr(p, put(t, p, body))

# ================================================================ TEST YOUR FIELD
def test():
    p = 'agriculture/test-your-field'; t = rd(p)
    m = re.search(r'<form class="form-form".*?</form>\s*<div class="form-message form-error.*?</div>\s*<div class="form-message form-success.*?</div>', t, re.S); assert m
    box = re.search(r'<div id="form-module-[^"]*"[^>]*class="form-container[^"]*">', t); assert box   # holds the theme's CSS variables for the form
    form = m.group(0).replace('<input type="text" data-required="true"', '<input id="Name" type="text" data-required="true"', 1).replace('<textarea data-id=', '<textarea id="Message" data-id=', 1)   # the labels point at these ids
    mail = re.search(r'href="(mailto:[^"]+)"', t).group(1); tel = re.search(r'href="(tel:[^"]+)"', t).group(1)
    body = hero(t, p, ('abb51ae4', 'pg-test'), 'Test your field', E('Do you have a farm in Bayern?'), '<p class="nb-lead">%s</p>' % E('We are looking for partners'), sm=True)
    body += sec('<div class="nb-contact"><div class="nb-card nb-form">%s%s</div><div class="nb-card"><h2>%s</h2><p>%s <a href="%s">+49 231 13707127</a></p><p>%s <a href="%s">info@nutrisen.eu</a></p><p>%s</p></div></div>' % (
        box.group(0), form + '</div>', E("Let's measure the nitrate of your plants."), E('Telefon:'), A(tel), E('E-mail:'), A(mail), E('Headquarters: Straubing, Germany.')))
    wr(p, put(t, p, body))

# ================================================================ ABOUT US
def about():
    p = 'agriculture/from-lab-to-field'; t = rd(p)
    links = re.findall(r'href="(https://(?:cordis|news\.rub)[^"]+)"', t); assert len(links) == 4, links
    items = [('2017', 'First, the science', [S('The enzyme we needed'), S('So we had to create'), 'And we nailed it, supported by the Redox Shields Project.'], '1e520f10', 'Researchers working in the lab', links[0]),
             ('2018', 'PoC LiveSEN', [S('As part of the ERC'), None], '07f8e945', 'Handheld sensor device in a field', links[1]),
             ('2020', 'PoC eConfidence', [S('The EU-funded eCONFIDENCE')], '1f1b9e3c', 'Multisensory test strips', links[2]),
             ('2021', 'EXIST Research Transfer', [S('After publishing outstanding'), S('Within EXIST')], 'a9d2abf3', 'Hand in a blue glove holding a wheat plant', links[3])]
    FUND = {'2017': ('715900', 'REDOX SHIELDS'), '2018': ('790155', 'LiveSEN')}   # CORDIS: ERC-2016-STG and ERC-2017-PoC
    out = ''
    for y, title, paras, iid, alt, href in items:
        ps = ''.join('<p>%s</p>' % E(x) for x in paras if x)
        if y in FUND:   # EU funding note with the CORDIS record of the project (ERC grants under Horizon 2020)
            gid, pname = FUND[y]
            ps += '<p class="nb-funding">%s <a href="https://cordis.europa.eu/project/id/%s" target="_blank" rel="noopener">%s</a></p>' % (
                E('Funded by the European Research Council (ERC) under Horizon 2020, grant agreement No %s.' % gid), gid, E('View %s on CORDIS' % pname))
        if y == '2018': ps += '<p class="nb-credit">%s</p>' % E('Foto: Food Hub NRW')
        out += '<article class="nb-tl-item"><div><span class="nb-year">%s</span><h2>%s</h2>%s<a class="nb-btn nb-btn--blue" href="%s" target="_blank" rel="noopener">%s</a></div><div class="nb-tl-media">%s</div></article>' % (
            y, E(title), ps, A(href), E('Learn more'), IMG(t, iid, alt, '(max-width:860px) 90vw, 440px'))
    body = hero(t, p, None, 'NutriSen', E('About us'), sm=True) + sec('<div class="nb-tl" style="margin-top:calc(-1 * clamp(28px,4vw,48px));position:relative">%s</div>' % out, 'nb-section--tl')
    wr(p, put(t, p, body))

# ================================================================ LEGAL (German originals; English copies are generated by i18n.py)
def legal():
    p = 'impressum'; t = rd(p)
    rows = [('Verantwortlich:', ['NutriSen GmbH', 'Europaring 4', '94315 Straubing', 'Deutschland']), ('Kontakt:', ['Tel.: +49 23113707127', 'Email: info@nutrisen.eu']),
            ('Geschäftsführer:', ['Tobias Vöpel & Alaa A. Oughli']), ('Registernummer:', ['HRB 13438']), ('Registergericht:', ['AG Straubing'])]
    de = [k for k in T.EN_LEGAL if len(k) > 200]
    para = lambda pre: next(k for k in de if k.startswith(pre))
    dl = '<dl>%s</dl>' % ''.join('<dt>%s</dt><dd>%s</dd>' % (E(a), '<br>'.join(E(x) for x in b)) for a, b in rows)
    doc = ('<!--ns-legal-note--><h2>%s</h2>%s<h2>%s</h2><h3>%s</h3><p>%s</p><h3>%s</h3><p>%s</p><h3>%s</h3><p>%s</p>' % (
        E('Impressum'), dl, E('Haftungsauschluss'), E('Haftung für Inhalte'), E(para('Die Inhalte unserer Seiten')), E('Haftung für Links'), E(para('Unser Angebot enthält')),
        E('Urheberrecht'), E(para('Die durch die Seitenbetreiber'))))
    body = hero(t, p, None, '', E('Impressum'), sm=True) + sec('<div class="nb-doc">%s</div>' % doc.replace('<h2>Impressum</h2>', '', 1), '', 'nb-wrap narrow')
    wr(p, put(t, p, body))
    p = 'datenschutzerklarung'; t = rd(p)
    doc = '<!--ns-legal-note--><h2>%s</h2>%s' % (E('Datenschutz'), ''.join('<p>%s</p>' % E(para(x)) for x in ('Die Nutzung unserer Webseite', 'Wir weisen darauf hin', 'Der Nutzung von im Rahmen', 'Diese Webseite verwendet')))
    body = hero(t, p, None, '', E('Datenschutzerklärung'), sm=True) + sec('<div class="nb-doc">%s</div>' % doc, '', 'nb-wrap narrow')
    wr(p, put(t, p, body))

# ================================================================ HOME (lower part: awards and team)
def home():
    p = ''; t = rd(p)
    starts = [m.start() for m in re.finditer(r'<div data-zone-type="content" class="section section-root', t)]
    at = max(s for s in starts if s < t.find('People are excited'))
    aw = [('bde581b1', 'Award ceremony of the Plan B Pitch Competition', 'Plan B Competition, Straubing.', ['3rd Prize in the Plan B Pitch Competition 2022!', S('Side-by-Side with start-ups')], ''),
          ('601ec95f', 'Logo of the Bio-Security competition', 'Bio-Security, Bönen.', [S('Since 2007'), S('In 2022, we secured')], ' contain'),
          ('945aded1', 'Logo of the Innovationspreis Moderne Landwirtschaft', 'Forum Moderne Landwirtschaft, Berlin.', ['What a night in Berlin!', S('We are very proud')], ' contain')]
    # Team cards (three members; the text above them says "Three nations united for one goal").
    team = [('b76c62ba', 'Tobias Vöpel', 'co-CEO', S('Father, husband'), 'linkedin.com/in/tobias'), ('ffefe5f4', 'Alaa Oughli', 'CTO', S('Leading scientist'), 'alaa-oughli'), ('48bc2463', 'Nicolas Plumeré', 'CSO', S("Nicolas's vision"), 'NicolasPlumere')]
    hrefs = re.findall(r'href="((?:https://(?:de\.|www\.)?linkedin\.com/in/[^"]+|https://twitter\.com/[^"]+|mailto:[^"]+))"', t)
    def link_for(key):
        return next(h for h in hrefs if key in h) if key != 'linkedin.com/in/tobias' else next(h for h in hrefs if 'tobias-v' in h)
    def mail_for(name):
        first = name.split()[0].lower().replace('é', 'e'); last = name.split()[-1].lower().replace('é', 'e')
        return next(h for h in hrefs if h.startswith('mailto:') and (first in h.lower() or last in h.lower()))
    awards = ''.join('<div class="nb-card nb-award"><div class="nb-award-img%s">%s</div><div class="nb-award-body"><h3>%s</h3>%s</div></div>' % (
        c, IMG(t, i, alt, '(max-width:860px) 90vw, 360px'), E(label), ''.join('<p>%s</p>' % E(x) for x in paras)) for i, alt, label, paras, c in aw)
    members = ''
    for iid, name, role, bio, key in team:
        ln = link_for(key); soc = 'Twitter' if 'twitter.com' in ln else 'LinkedIn'
        members += '<div class="nb-card nb-team">%s<div class="nb-team-body"><h3>%s</h3><p class="nb-role">%s</p><p>%s</p><div class="nb-chips"><a class="nb-chip" href="%s" target="_blank" rel="noopener">%s</a><a class="nb-chip" href="%s">%s</a></div></div></div>' % (
            IMG(t, iid, name, '(max-width:860px) 90vw, 260px'), E(name), E(role), E(bio), A(ln), soc, A(mail_for(name)), E('E-mail'))
    body = (sec('<h2 class="nb-h2 nb-center">%s</h2><div class="nb-grid" style="margin-top:28px">%s</div>' % (E('People are excited about us'), awards), 'nb-section--white') +
            sec('<h2 class="nb-h2">%s</h2><p class="nb-sub">%s</p><div class="nb-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,240px),1fr))">%s</div>' % (
                E('Diversity is our super power'), E(S('Three nations united')), members), 'nb-section--white'))
    s, e = region(t)
    t = t[:at] + '<div class="nb">' + body + '</div>\n' + t[e:]
    wr(p, t.replace('</head>', '<link rel="stylesheet" href="assets/brand.css">\n</head>', 1))

for fn in (medical, agriculture, how, test, about, legal, home): fn()
print('restyled: home (lower part), medical, agriculture, how-does-it-work, test-your-field, from-lab-to-field, impressum, datenschutzerklarung')
