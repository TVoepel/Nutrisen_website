#!/usr/bin/env python3
"""Download free, official EU fertiliser price data and write assets/fertilizer-prices.json for the calculator.

Sources (no key, no cost):
  1. Eurostat apri_aip_ft  "Purchase prices for fertilisers (expressed in nutritive content)", EUR per tonne of
     nutrient, annual, per Member State and product. Marked provisional by Eurostat. Some Member States evidently
     report in another unit; values outside 0.6x to 1.7x of the EU median of the nutrient group are NOT used.
  2. European Commission, Agri-food data portal API /fertiliser/prices: monthly EU-level price indicator for N, P, K.
     Only shown as a market trend, never used in the cost calculation.
Nothing is estimated or filled in. If a download fails the existing file is kept and the script exits with an error.
Usage: python3 tools/fetch_prices.py [output.json]"""
import json, os, sys, time, statistics, datetime, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'fertilizer-prices.json')
ES = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/apri_aip_ft?format=JSON&lang=en'
AG = 'https://api.tech.ec.europa.eu/agrifood/api/fertiliser/prices'
NAMES = {  # EU-27: (German, English); Eurostat uses EL for Greece
    'BE': ('Belgien', 'Belgium'), 'BG': ('Bulgarien', 'Bulgaria'), 'CZ': ('Tschechien', 'Czechia'), 'DK': ('Dänemark', 'Denmark'),
    'DE': ('Deutschland', 'Germany'), 'EE': ('Estland', 'Estonia'), 'IE': ('Irland', 'Ireland'), 'EL': ('Griechenland', 'Greece'),
    'ES': ('Spanien', 'Spain'), 'FR': ('Frankreich', 'France'), 'HR': ('Kroatien', 'Croatia'), 'IT': ('Italien', 'Italy'),
    'CY': ('Zypern', 'Cyprus'), 'LV': ('Lettland', 'Latvia'), 'LT': ('Litauen', 'Lithuania'), 'LU': ('Luxemburg', 'Luxembourg'),
    'HU': ('Ungarn', 'Hungary'), 'MT': ('Malta', 'Malta'), 'NL': ('Niederlande', 'Netherlands'), 'AT': ('Österreich', 'Austria'),
    'PL': ('Polen', 'Poland'), 'PT': ('Portugal', 'Portugal'), 'RO': ('Rumänien', 'Romania'), 'SI': ('Slowenien', 'Slovenia'),
    'SK': ('Slowakei', 'Slovakia'), 'FI': ('Finnland', 'Finland'), 'SE': ('Schweden', 'Sweden')}
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def get(url, tries=8):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'Accept': 'application/json', 'User-Agent': 'nutrisen-price-fetch'}), timeout=90) as r:
                data = json.load(r)
            if isinstance(data, dict) and data.get('code') and not data.get('dimension'):   # gateway hiccup of the EU API
                raise RuntimeError(data.get('description', 'gateway error'))
            return data
        except Exception as e:
            print(f'  retry {i + 1}/{tries}: {e}', file=sys.stderr); time.sleep(3 * (i + 1))
    sys.exit(f'download failed: {url}')

# ---------------------------------------------------------------- Eurostat
d = get(ES)
ids, size, dim = d['id'], d['size'], d['dimension']
idx = {k: dim[k]['category']['index'] for k in ids}
assert 'EUR_T' in idx['unit'] and len(idx['time']) >= 1, 'unexpected Eurostat structure'
year = sorted(idx['time'])[-1]
vals, flags = d['value'], d.get('status', {})
def cell(item, geo):
    pos, mult = 0, 1
    co = {'freq': 'A', 'am_item': item, 'unit': 'EUR_T', 'geo': geo, 'time': year}
    for k in reversed(ids): pos += idx[k][co[k]] * mult; mult *= size[ids.index(k)]
    v = vals.get(str(pos)) if isinstance(vals, dict) else vals[pos]
    return v, flags.get(str(pos))
items = {c: dim['am_item']['category']['label'][c] for c in idx['am_item']}
GROUPS = {'N': ('AM203111', 'AM203112', 'AM203113', 'AM203114', 'AM203115', 'AM203116', 'AM203117', 'AM203118', 'AM203119'),
          'P': ('AM203121',), 'K': ('AM203131', 'AM203132', 'AM203133')}
median = {}   # reference per product = median of its nutrient group (robust even for products reported by few countries)
for grp in GROUPS.values():
    xs = [cell(it, g)[0] for it in grp if it in items for g in idx['geo']]; xs = [x for x in xs if x]
    for it in grp: median[it] = statistics.median(xs) if xs else None
countries = {}
for code, (de, en) in NAMES.items():
    prices, excluded = {}, []
    if code in idx['geo']:
        for it in items:
            v, fl = cell(it, code)
            if not v: continue
            if median[it] and 0.6 * median[it] <= v <= 1.7 * median[it]: prices[it] = {'v': round(v, 2), 'p': 1 if fl == 'p' else 0}
            else: excluded.append(it)
    countries[code] = {'de': de, 'en': en, 'prices': prices, 'excluded': excluded, 'reported': code in idx['geo']}
upd = next((a['date'] for a in d['extension']['annotation'] if a.get('type') == 'UPDATE_DATA'), d.get('updated'))

# ---------------------------------------------------------------- Agri-food data portal (EU level, monthly)
rows = get(AG)
assert isinstance(rows, list) and rows, 'unexpected agri-food data portal response'
agri = {}
for key, prefix in (('N', 'N '), ('P', 'P '), ('K', 'K ')):
    s = sorted(((r['year'], MONTHS.index(r['month']) + 1, r['price']) for r in rows if r['product'].startswith(prefix)))
    y, m, p = s[-1]
    ref = [x[2] for x in s if x[0] == int(year)]
    agri[key] = {'year': y, 'month': m, 'price': p, 'avg_ref_year': round(sum(ref) / len(ref), 1) if len(ref) == 12 else None,
                 'change_pct': round((p / (sum(ref) / len(ref)) - 1) * 100, 1) if len(ref) == 12 else None}
out = {
    'retrieved': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d'),
    'eurostat': {'dataset': 'apri_aip_ft', 'label': d['label'], 'year': int(year), 'updated': upd[:10], 'unit': 'EUR per tonne of nutrient',
                 'url': 'https://ec.europa.eu/eurostat/databrowser/view/apri_aip_ft', 'median': median,
                 'rule': 'Values outside 0.6x-1.7x of the EU median of the same nutrient group (all N products, P, K) are not used (probable unit differences in reporting).'},
    'items': items, 'countries': countries,
    'agridata': {'unit': 'EUR per tonne (as published, aggregated by nutrient)', 'ref_year': int(year),
                 'url': 'https://agridata.ec.europa.eu/extensions/DashboardFertiliser/FertiliserPrices.html', **agri}}
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
new = json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True)
old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
strip = lambda t: '\n'.join(l for l in t.splitlines() if '"retrieved"' not in l)
if strip(new) != strip(old): open(OUT, 'w', encoding='utf-8').write(new + '\n'); print('updated', OUT)
else: print('no change in source data')
used = sum(len(c['prices']) for c in countries.values()); skipped = sum(len(c['excluded']) for c in countries.values())
print(f'Eurostat {year}: {used} prices used, {skipped} excluded as outliers; agri-food portal latest {agri["N"]["year"]}-{agri["N"]["month"]:02d}')
