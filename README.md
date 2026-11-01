# NutriSen website mirror

Static mirror of <https://www.nutrisen.eu>, taken on 2026-10-05. Open `index.html` locally or serve the
repository root with any static web server (for example `python3 -m http.server`). All internal links are
relative, so the site works from a sub-path as well as from a domain root.

## How the original site is built

- **Platform:** IONOS *MyWebsite NOW* (`<meta name="generator" content="MyWebsite NOW">`). Under the hood this is
  WordPress with the IONOS `gox` theme and the `go-x-post-editor` / `go-x-blocks` plugins plus a Gutenberg build.
  Pages are rendered server-side as full HTML with all theme CSS inlined into each page.
- **Fonts:** Poppins (regular, italic, 500, 500 italic, 700, 700 italic) and Hind (regular, 500, 700) are
  self-hosted from `wp-content/themes/gox/public/fonts/` in eot/woff/woff2/ttf/svg. No Google Fonts or other
  third-party font hosts.
- **Images:** served from `wp-content/uploads/go-x/u/<uuid>/...`. Crop variants live in sub-directories such as
  `l334,t0,w1333,h1333/` (left, top, width, height) and responsive sizes are suffixed `image-<w>x<h>.jpg`, each
  exposed via `srcset`.
- **Scripts:** three small front-end scripts (go-x post editor front end, Gutenberg hooks and i18n), the go-x form
  script, and the WordPress emoji loader. No analytics, no cookie banner, no external embeds.
- **Language (before this change):** every page declared `lang="de"`, but all content except Impressum and
  Datenschutzerklärung was English, and there was no language switcher.

## Pages (from the site's `wp-sitemap`)

| Path | Title | Notes |
| --- | --- | --- |
| `/` | NutriSen | Two hero sections (agriculture, medical), awards, team |
| `/medical/` | Medical | Biosensor platform, molecule pipeline (lactate, creatinine, cholesterol) |
| `/agriculture/` | Agriculture | Benefits, savings targets |
| `/agriculture/how-does-it-work/` | How does the premium service of NutriSen work | Six-step process |
| `/agriculture/test-your-field/` | Test for free the nitrate concentrations of your field | Contact form |
| `/agriculture/from-lab-to-field/` | About us | Timeline 2017 to EXIST transfer. **Not linked from any menu.** |
| `/the-npknowledge/` | The NPKnowledge | **Not linked from any menu and still contains placeholder text.** |
| `/impressum/` | NutriSen GmbH Impressum | German legal notice |
| `/datenschutzerklarung/` | Datenschutzerklärung | German privacy policy |

The two unlinked pages are still publicly reachable on the live site because they are listed in the sitemap.

## What was changed for the static mirror

- Each page is stored as `<slug>/index.html`, matching the live server, which redirects `/medical` to `/medical/`.
- Absolute and root-relative links to `www.nutrisen.eu` were rewritten to relative paths.
- Cache-busting query strings (`?ver=...`, `?v=...`) were stripped from asset file names and references, because a
  static host cannot serve a file whose name contains `?`.
- WordPress plumbing `<link>` tags that only work with a live WordPress backend were removed: RSS and comment feeds,
  oEmbed discovery, REST API (`wp-json`), RSD/`xmlrpc.php`, and shortlinks.
- `og:image` meta tags still point to the live site, as Open Graph requires absolute URLs.

## Known limitations of a static copy

- The contact form on `/agriculture/test-your-field/` posts to the WordPress backend and will not send anything
  from this mirror. Wire it to a form service or replace it with a `mailto:` link if you host this copy.
- Nothing else on the site is dynamic.

## Changes beyond the mirror

- **Home hero (2026-11-01):** the two stacked banners are replaced by a full-screen audience split. Farmers get
  "Test your field for free" with the 20% fertilizer saving and up to 10% yield figures from the agriculture page.
  Medical-device makers get "Schedule a meeting" with the lactate and creatinine readiness levels. A strip of
  awards sits underneath. Styles are in `assets/home-split.css`; `tools/apply_home_split.py` applies the change
  and is safe to re-run after a refresh.

- **Two languages (2026-11-01):** English stays at the existing URLs (`lang="en"`). A full German version lives
  under `/de/`. A DE | EN switcher sits in the header of every page that has a translation, and every page
  carries `canonical` and `hreflang` tags. The legal pages keep their German URLs (`/impressum/`,
  `/datenschutzerklarung/`) and have new English courtesy translations at `/legal-notice/` and `/privacy-policy/`.
  All translations are in `tools/i18n_strings.py`; `tools/i18n.py` generates the pages.
  Two wording bugs were fixed on the way: the contact form button read "Seed" (now "Send" / "Absenden"), and the
  English contact page said "Telefon:" (now "Phone:"). The typo "Haftungsauschluss" in the German legal notice is fixed.
- `/the-npknowledge/` is still English only and unlinked, because it contains placeholder text.

- **Practice cases page (2026-11-01):** `/agriculture/use-cases/` (German: `/de/agriculture/use-cases/`) shows five
  farm results from 2025/2026 (fertilizer vs. the standard recommendation, yield, economic result) with a bar chart,
  four headline figures and a link to the free field test. It is added to the Agriculture menu on every page.
  Styles: `assets/usecases.css`; generator: `tools/add_usecases.py`.

- **Savings calculator (2026-11-02):** a slider for farm size on the home page and the agriculture page shows the
  expected fertilizer saving (about 80 EUR/ha) and extra revenue (up to 240 EUR/ha), using the figures already
  published on the site, and sends the visitor to the free field test with the farm size pre-filled in the message.
  CSS and JS are inlined into the page (no extra requests). Sources: `assets/calc.css`, `assets/calc.js`;
  generator: `tools/add_calculator.py`.
- **Speed pass (2026-11-02):** `tools/optimize.py` runs last. All photos and graphics are WebP (larger than 1920 px
  are scaled down), the home hero uses small responsive images, fonts are woff2 only with `font-display:swap` and
  the three most used faces are preloaded, HTML comments and dead scripts (emoji, Gutenberg i18n, old-IE banner)
  are gone, inline CSS is minified, images below the fold are lazy, `background-attachment:fixed` is removed, and
  the site's analytics script (cdn.pagepulse.info) is requested only after the page has loaded. `.htaccess` (Apache,
  IONOS) and `_headers` (Netlify/Cloudflare style) add compression and one-year caching for assets.

  | Page transfer (gzip, scrolled to the end) | Before | After |
  | --- | --- | --- |
  | Home, desktop | 1,817 KB | 310 KB |
  | Home, mobile | 2,320 KB | 562 KB |
  | Agriculture, desktop | 1,131 KB | 229 KB |
  | How does it work, mobile | 1,804 KB | 379 KB |

## Refreshing the mirror

```
tools/fetch.sh /tmp/nutrisen-work        # downloads pages and assets with wget/curl
python3 tools/build.py /tmp/nutrisen-work /tmp/nutrisen-out
```

Then copy the contents of the output directory over this repository and run, in this order (needs `pip install pillow` and Node.js):
`apply_home_split.py`, `add_usecases.py`, `add_calculator.py`, `i18n.py`, `optimize.py` (all in `tools/`, each as
`python3 tools/<name>.py .`). Copy the new files into a fresh `assets/` first: `home-split.css`, `lang.css`,
`usecases.css`, `calc.css`, `calc.js`. `i18n.py` refuses to run twice on the same files.
