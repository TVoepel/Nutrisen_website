#!/usr/bin/env python3
"""SEO pass. Run last (after optimize.py): python3 tools/seo.py <site-root>

Per page: unique title and description, one absolute canonical, Open Graph and Twitter tags (1200x630 image),
robots meta, structured data (Organization + WebSite on the home pages, BreadcrumbList everywhere, BlogPosting for
the articles, WebApplication for the calculator). The wrong LocalBusiness block of the old site (opening hours,
info@livesen.eu, empty fields, broken logo path) is removed. Then writes sitemap.xml (with hreflang alternates) and
robots.txt. Safe to re-run: every tag it writes is replaced, never duplicated.
"""
import glob, html, json, os, re, subprocess, sys
from datetime import date

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
BASE = 'https://www.nutrisen.eu'
OG = {'en': 'assets/og-en.jpg', 'de': 'assets/og-de.jpg'}
OG_ALT = {'en': 'NutriSen: nitrate in the plant sap, measured directly in the field',
          'de': 'NutriSen: Nitrat im Pflanzensaft, direkt auf dem Feld gemessen'}
LOCALE = {'en': 'en_US', 'de': 'de_DE'}
ORG = {
    '@type': 'Organization', '@id': BASE + '/#organization', 'name': 'NutriSen GmbH', 'alternateName': 'NutriSen',
    'url': BASE + '/', 'logo': BASE + '/assets/nutrisen-logo.webp', 'email': 'info@nutrisen.eu',
    'telephone': '+4923113707127', 'foundingDate': '2023',
    'address': {'@type': 'PostalAddress', 'streetAddress': 'Europaring 4', 'postalCode': '94315',
                'addressLocality': 'Straubing', 'addressCountry': 'DE'},
}
NOSITEMAP = {'impressum', 'datenschutzerklarung', 'legal-notice', 'privacy-policy'}

# key = path of the English page (without /de/). (title, description or None to keep the existing one)
T = {
 'en': {
  '': ('NutriSen: plant sap nitrate test for precise fertilization',
       'Biosensors measure nitrate in the plant sap right in the field, so you fertilize by need. Up to 30% less fertilizer is possible. Test your field for free.'),
  'medical': ('Biosensors for digital health | NutriSen Medical',
       'Biosensors for lactate, creatinine and more: direct molecular sensing for medical-device makers and digital health. Get in touch with NutriSen.'),
  'agriculture': ('Fertilize by need: nitrate sensing for farmers | NutriSen',
       'Real-time nutrient sensing for smart fertilization: up to 30% less fertilizer and savings of up to 90 EUR per ha are possible. Calculate your own savings.'),
  'agriculture/how-does-it-work': ('How it works: nitrate test strips for your field | NutriSen', None),
  'agriculture/test-your-field': ('Free nitrate test for your field in Bayern | NutriSen', None),
  'agriculture/use-cases': ('Practice cases 2025/2026: less fertilizer | NutriSen', None),
  'agriculture/calculator': ('NutriSen fertilizer calculator: compare 3 applications', None),
  'agriculture/from-lab-to-field': ('About NutriSen: from the lab to the field', None),
  'blog': ('Blog: fertilizer prices, plant nutrition, nitrate | NutriSen', None),
  'blog/nutrient-prices-eu-reporting': ('Nutrient prices: why the EU reports them | NutriSen', None),
  'blog/jubil-nitrate-method': ('JUBIL® stem-juice nitrate test explained | NutriSen',
       'Where the JUBIL® stem-juice nitrate test comes from, how it steers the last nitrogen application in winter wheat, and why it works.'),
  'blog/bbch-winter-wheat-germany-france': ('Wheat nitrogen by BBCH stage: Germany vs France | NutriSen',
       'How the BBCH scale guides nitrogen in winter wheat, how Germany and France split the doses, and where the JUBIL® stem-juice nitrate test fits in.'),
  'legal-notice': ('NutriSen GmbH Legal Notice',
       'Legal notice (courtesy translation) of NutriSen GmbH, Europaring 4, 94315 Straubing, Germany. The German Impressum is binding.'),
  'privacy-policy': ('Privacy Policy | NutriSen',
       'How NutriSen GmbH handles personal data on this website (courtesy translation). The German privacy policy is binding.'),
 },
 'de': {
  '': ('NutriSen: Nitrattest im Pflanzensaft für präzises Düngen',
       'Biosensoren messen Nitrat im Pflanzensaft direkt auf dem Feld, damit Sie bedarfsgerecht düngen. Bis zu 30 % weniger Dünger möglich. Feld kostenlos testen.'),
  'medical': ('Biosensoren für digitale Gesundheit | NutriSen Medizin',
       'Biosensoren für Laktat, Kreatinin und mehr: direkte Molekülmessung für Hersteller von Medizinprodukten und die digitale Gesundheit. Jetzt Kontakt aufnehmen.'),
  'agriculture': ('Düngen nach Bedarf: Nitratmessung für Landwirte | NutriSen',
       'Nährstoffmessung in Echtzeit für intelligentes Düngen: bis zu 30 % weniger Dünger und Einsparungen von bis zu 90 € pro ha sind möglich. Jetzt selbst berechnen.'),
  'agriculture/how-does-it-work': ('So funktioniert es: Nitrat-Teststreifen fürs Feld | NutriSen', None),
  'agriculture/test-your-field': ('Kostenloser Nitrattest für Ihr Feld in Bayern | NutriSen', None),
  'agriculture/use-cases': ('Praxisfälle 2025/2026: weniger Dünger | NutriSen', None),
  'agriculture/calculator': ('NutriSen Düngerechner: Vergleich von 3 Gaben', None),
  'agriculture/from-lab-to-field': ('Über NutriSen: vom Labor aufs Feld', None),
  'blog': ('Blog: Düngerpreise, Pflanzenernährung, Nitrat | NutriSen', None),
  'blog/nutrient-prices-eu-reporting': ('Nährstoffpreise: Warum die EU sie meldet | NutriSen', None),
  'blog/jubil-nitrate-method': ('JUBIL®: Nitrattest im Stängelsaft erklärt | NutriSen',
       'Woher der JUBIL®-Nitrattest im Stängelsaft kommt, wie er die letzte Stickstoffgabe bei Winterweizen steuert und warum er funktioniert.'),
  'blog/bbch-winter-wheat-germany-france': ('Winterweizen-Stickstoff nach BBCH: DE und FR | NutriSen',
       'Wie die BBCH-Skala die Stickstoffdüngung bei Winterweizen lenkt, wie Deutschland und Frankreich die Gaben aufteilen und wo der JUBIL®-Nitrattest passt.'),
  'impressum': ('NutriSen GmbH Impressum',
       'Impressum der NutriSen GmbH, Europaring 4, 94315 Straubing: Verantwortliche, Kontakt, Geschäftsführung und Registerdaten.'),
  'datenschutzerklarung': ('Datenschutzerklärung | NutriSen',
       'Datenschutzerklärung der NutriSen GmbH: wie wir personenbezogene Daten auf dieser Website verarbeiten.'),
 },
}
CRUMB = {  # last or intermediate crumb name by English key
 'en': {'medical': 'Medical', 'agriculture': 'Agriculture', 'agriculture/how-does-it-work': 'How it works',
        'agriculture/test-your-field': 'Test your field', 'agriculture/use-cases': 'Practice cases',
        'agriculture/calculator': 'Fertilizer calculator', 'agriculture/from-lab-to-field': 'About us', 'blog': 'Blog',
        'legal-notice': 'Legal notice', 'privacy-policy': 'Privacy policy', '': 'Home'},
 'de': {'medical': 'Medizin', 'agriculture': 'Landwirtschaft', 'agriculture/how-does-it-work': 'So funktioniert es',
        'agriculture/test-your-field': 'Feld testen', 'agriculture/use-cases': 'Praxisfälle',
        'agriculture/calculator': 'Düngerechner', 'agriculture/from-lab-to-field': 'Über uns', 'blog': 'Blog',
        'impressum': 'Impressum', 'datenschutzerklarung': 'Datenschutzerklärung', '': 'Start'},
}

def rd(p): return open(p, encoding='utf-8').read()
def esc(s): return html.escape(s, quote=True)
def jd(o): return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

def pages():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(('wp-content', 'tools', 'assets')): continue
        out.append((f, os.path.dirname(rel).replace(os.sep, '/')))
    return out

def key_lang(d):
    """directory -> (english key, lang)."""
    if d == 'de': return '', 'de'
    if d.startswith('de/'): return d[3:], 'de'
    return d, ('de' if d in ('impressum', 'datenschutzerklarung') else 'en')

def url(d): return BASE + '/' + (d + '/' if d else '')

def head_title(t): return re.search(r'<title>(.*?)</title>', t, re.S).group(1)

def process(f, d):
    t = rd(f)
    key, lang = key_lang(d)
    spec = T[lang].get(key)
    if not spec:
        print('no SEO entry for', d); return None
    title, desc = spec
    old_desc = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', t)
    desc = desc or (html.unescape(old_desc.group(1)) if old_desc else '')
    if not desc: raise SystemExit('no description for ' + d)
    if len(desc) > 165: print('long description (%d): %s' % (len(desc), d))
    if len(title) > 62: print('long title (%d): %s' % (len(title), d))
    page_url = url(d)
    img = BASE + '/' + OG[lang]
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    h1 = html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip() if h1 else title
    post = key.startswith('blog/')
    # --- strip what is rewritten
    t = re.sub(r'<title>.*?</title>', lambda m: '<title>%s</title>' % esc(title), t, count=1, flags=re.S)
    t = re.sub(r'<meta\s+name="description"[^>]*>\s*', '', t)
    t = re.sub(r'<meta\s+(?:property|name)="(?:og|twitter|article):[^"]*"[^>]*>\s*', '', t)
    t = re.sub(r'<meta\s+name=\'robots\'[^>]*>\s*', '', t)
    t = re.sub(r'<meta\s+name="robots"[^>]*>\s*', '', t)
    t = re.sub(r'<link rel="canonical" href="(?!https://)[^"]*"\s*/?>\s*', '', t)          # old relative canonical
    t = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', t, flags=re.S)  # old LocalBusiness
    t = re.sub(r'<!--seo-->.*?<!--/seo-->\s*', '', t, flags=re.S)
    # --- structured data
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': CRUMB[lang][''], 'item': url('de' if lang == 'de' and d != 'impressum' and d != 'datenschutzerklarung' else '')}]
    if d not in ('', 'de'):
        base_path = key
        parts = base_path.split('/')
        acc = []
        for i, seg in enumerate(parts):
            acc.append(seg); k = '/'.join(acc)
            last = i == len(parts) - 1
            name = h1 if (last and post) else CRUMB[lang].get(k) or CRUMB['en'].get(k) or seg
            crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1, 'name': name,
                           'item': url(('de/' if lang == 'de' and d.startswith('de/') else '') + k)})
    graph = [{'@type': 'BreadcrumbList', 'itemListElement': crumbs}] if d not in ('', 'de') else []
    if d in ('', 'de'):
        graph += [ORG, {'@type': 'WebSite', '@id': BASE + '/#website', 'name': 'NutriSen', 'url': BASE + '/',
                        'publisher': {'@id': BASE + '/#organization'}, 'inLanguage': ['en', 'de']}]
    if post:
        graph.append({'@type': 'BlogPosting', 'headline': h1, 'description': desc, 'inLanguage': lang,
                      'datePublished': re.search(r'datetime="([\d-]+)"', t).group(1) if re.search(r'datetime="([\d-]+)"', t) else '2026-11-01',
                      'image': img, 'mainEntityOfPage': page_url, 'author': {'@id': BASE + '/#organization'},
                      'publisher': ORG})
        graph[-1]['dateModified'] = graph[-1]['datePublished']
    if key == 'agriculture/calculator':
        graph.append({'@type': 'WebApplication', 'name': h1, 'description': desc, 'url': page_url, 'inLanguage': lang,
                      'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Any',
                      'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'},
                      'provider': {'@id': BASE + '/#organization'}})
    ld = {'@context': 'https://schema.org', '@graph': [g for g in graph if g]}
    other = 'en_US' if lang == 'de' else 'de_DE'
    og = [
        ('name', 'description', desc),
        ('name', 'robots', 'index,follow,max-image-preview:large'),
        ('property', 'og:type', 'article' if post else 'website'),
        ('property', 'og:site_name', 'NutriSen'),
        ('property', 'og:locale', LOCALE[lang]),
        ('property', 'og:locale:alternate', other),
        ('property', 'og:title', title),
        ('property', 'og:description', desc),
        ('property', 'og:url', page_url),
        ('property', 'og:image', img),
        ('property', 'og:image:width', '1200'),
        ('property', 'og:image:height', '630'),
        ('property', 'og:image:alt', OG_ALT[lang]),
        ('name', 'twitter:card', 'summary_large_image'),
        ('name', 'twitter:title', title),
        ('name', 'twitter:description', desc),
        ('name', 'twitter:image', img),
    ]
    if post: og.append(('property', 'article:published_time', graph[-1]['datePublished']))
    block = '<!--seo-->' + ''.join('<meta %s="%s" content="%s">' % (a, b, esc(c)) for a, b, c in og)
    block += '<script type="application/ld+json">%s</script><!--/seo-->\n' % jd(ld)
    # canonical: exactly one absolute (added by i18n); make sure it points at this page
    if not re.search(r'<link rel="canonical" href="https://', t):
        t = t.replace('</head>', '<link rel="canonical" href="%s">\n</head>' % page_url, 1)
    t = re.sub(r'<link rel="canonical" href="https://[^"]*">', '<link rel="canonical" href="%s">' % page_url, t, count=1)
    t = re.sub(r'(<link rel="canonical" href="[^"]*">)', lambda m: m.group(1) + '\n' + block, t, count=1)
    # one h1 on the home pages: the farmer panel is the first headline
    if d in ('', 'de') and '<h1' not in t:
        t = t.replace('<h2>', '<h1>', 1).replace('</h2>', '</h1>', 1)
    # the comment markers are only for idempotency; drop them from the output
    t = t.replace('<!--seo-->', '').replace('<!--/seo-->', '')
    open(f, 'w', encoding='utf-8').write(t)
    return page_url

def lastmod(f):
    rel = os.path.relpath(f, ROOT)
    try:
        if subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--', rel], capture_output=True, text=True).stdout.strip():
            return date.today().isoformat()
        d = subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%cs', '--', rel], capture_output=True, text=True).stdout.strip()
        return d or date.today().isoformat()
    except Exception:
        return date.today().isoformat()

def sitemap(done):
    rows = []
    for f, d in done:
        if d in NOSITEMAP or d.rstrip('/') in NOSITEMAP: continue
        t = rd(f)
        alts = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', t)
        loc = url(d)
        r = ['  <url>', '    <loc>%s</loc>' % loc, '    <lastmod>%s</lastmod>' % lastmod(f)]
        for hl, hr in alts:
            r.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (hl, hr))
        r.append('  </url>')
        rows.append('\n'.join(r))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + '\n'.join(rows) + '\n</urlset>\n')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(xml)
    open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(
        'User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: %s/sitemap.xml\n' % BASE)
    return len(rows)

def main():
    done = []
    for f, d in pages():
        if process(f, d): done.append((f, d))
    n = sitemap(done)
    print('seo: %d pages, %d in sitemap' % (len(done), n))

if __name__ == '__main__':
    main()
