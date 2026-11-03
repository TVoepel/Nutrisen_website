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
| `/impressum/` | NutriSen GmbH Impressum | German legal notice |
| `/datenschutzerklarung/` | Datenschutzerklärung | German privacy policy |

The page `/the-npknowledge/` (placeholder text, not linked anywhere) was removed from this copy.

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
  Medical-device makers get "Get in touch" (mailto info@nutrisen.eu, the old Outlook booking calendar of livesen.eu was removed) with the lactate and creatinine readiness levels. A strip of
  awards sits underneath. Styles are in `assets/home-split.css`; `tools/apply_home_split.py` applies the change
  and is safe to re-run after a refresh.

- **Two languages (2026-11-01):** English stays at the existing URLs (`lang="en"`). A full German version lives
  under `/de/`. A DE | EN switcher sits in the header of every page that has a translation, and every page
  carries `canonical` and `hreflang` tags. The legal pages keep their German URLs (`/impressum/`,
  `/datenschutzerklarung/`) and have new English courtesy translations at `/legal-notice/` and `/privacy-policy/`.
  All translations are in `tools/i18n_strings.py`; `tools/i18n.py` generates the pages.
  Two wording bugs were fixed on the way: the contact form button read "Seed" (now "Send" / "Absenden"), and the
  English contact page said "Telefon:" (now "Phone:"). The typo "Haftungsauschluss" in the German legal notice is fixed.

- **Practice cases page (2026-11-01):** `/agriculture/use-cases/` (German: `/de/agriculture/use-cases/`) shows five
  farm results from 2025/2026 (fertilizer vs. the standard recommendation, yield, economic result) with a bar chart,
  four headline figures and a link to the free field test. It is added to the Agriculture menu on every page.
  Styles: `assets/usecases.css`; generator: `tools/add_usecases.py`.

- **Savings calculator (2026-11-02):** a slider for farm size on the home page and the agriculture page shows the
  possible saving on fertilizer as an "up to" value: up to 90 EUR per ha with up to 30% less fertilizer, calculated
  with 30 EUR per ha for every 10% of fertilizer (fertilizer prices of 2025-2026, as in the practice cases). It sends
  the visitor to the free field test with the farm size pre-filled. No extra revenue is shown. Statements about
  extra yield are worded cautiously throughout ("in some cases", "in individual cases"). CSS and JS are inlined into
  the page. Sources: `assets/calc.css`, `assets/calc.js`; generator: `tools/add_calculator.py`.
- **Speed pass (2026-11-02):** `tools/optimize.py` runs last. All photos and graphics are WebP (larger than 1920 px
  are scaled down), the home hero uses small responsive images, fonts are woff2 only with `font-display:swap` and
  the three most used faces are preloaded, HTML comments and dead scripts (emoji, Gutenberg i18n, old-IE banner)
  are gone, inline CSS is minified, images below the fold are lazy, `background-attachment:fixed` is removed, and
  the site's analytics script (cdn.pagepulse.info) is switched off (see "Analytics switch" below). `.htaccess` (Apache,
  IONOS) and `_headers` (Netlify/Cloudflare style) add compression and one-year caching for assets.

  | Page transfer (gzip, scrolled to the end) | Before | After |
  | --- | --- | --- |
  | Home, desktop | 1,817 KB | 310 KB |
  | Home, mobile | 2,320 KB | 562 KB |
  | Agriculture, desktop | 1,131 KB | 229 KB |
  | How does it work, mobile | 1,804 KB | 379 KB |

- **NutriSen fertilizer calculator (2026-11-02):** `/agriculture/calculator/` (German: `/de/agriculture/calculator/`)
  compares the usual fertilization with a NutriSen fertilization in three applications (fertilizer, price per
  tonne, N content, target kg N/ha, costs, savings, detail table). In the Agriculture menu on every page, and linked
  from the quick calculator. Sources: `assets/fcalc.js`, `assets/fcalc.css`; generator: `tools/add_fertilizer_calc.py`.
  - **Where the prices come from (free sources only, nothing is invented):**
    Eurostat dataset `apri_aip_ft` "Purchase prices for fertilisers", EUR per tonne of nutrient, annual 2025, per
    Member State. Only products that match a fertilizer in the list are suggested: KAS = CAN, ASS = AN with sulphur,
    urea, AHL = UAN. For Alzon Neo, DAP and Innofert Star there is no EU price, so the user enters their own.
    The dataset is marked provisional by Eurostat and some countries clearly report in another unit, so values outside
    0.6x to 1.7x of the EU median of the nutrient group are not used (shown as "enter your own price"). Austria and
    Malta are not in the dataset. The EU Agri-food data portal supplies a monthly EU nitrogen price indicator that
    is shown as a trend only. It is not used in any cost calculation, because it is aggregated by nutrient and its
    unit basis differs from Eurostat's. Every price can be overwritten with the user's own purchase price.
  - **Refreshing the prices:** `python3 tools/fetch_prices.py` rewrites `assets/fertilizer-prices.json`. The GitHub
    workflow `.github/workflows/update-fertilizer-prices.yml` does this monthly and commits changes. The page reads the
    JSON at runtime, so no rebuild is needed. The browser cannot call the EU API directly (no CORS), hence the file.
  - The disclaimer text on the page (market data source, no liability) was provided by the site owner. The
    paragraph about Eurostat was added to cover the second source.

- **Blog (2026-11-01):** `/blog/` (German: `/de/blog/`) with five articles, each 3 to 5 minutes of reading time, in English
  and German and linked in the main menu: "Nutrient prices: why the EU reports them and how to use them" and "JUBIL®: where
  the stem-juice nitrate test comes from and why it works" (links to the ARVALIS page `arvalis.fr/jubil-en-detail`). The
  texts are in `tools/blog_content.py` (both languages, with their sources); `tools/add_blog.py` builds the pages and
  `assets/blog.css` styles them. Every statement is taken from the sources listed under each article. The reading time
  is computed from the word count at 200 words per minute. To add an article, add an entry to `POSTS` and register its
  key and slug in `tools/i18n.py`.

- **Article on BBCH stages, Germany vs France (2026-11-02):** `/blog/bbch-winter-wheat-germany-france/` (German: `/de/blog/...`). Explains the
  BBCH codes for winter wheat and compares how German practice (fertiliser ordinance requirement values, three doses, the TLL
  nitrate quick test) and French practice (bilan prévisionnel, ARVALIS timing advice, JUBIL®) tie nitrogen to growth stages. Sources are
  listed under the article. Posts can now carry their own `date` and `date_txt` in `tools/blog_content.py`.

- **Short article on the DWD Bright Sky API (2026-11-02):** `/blog/dwd-bright-sky-api-farmers/` (German: `/de/blog/...`), 3 minutes. Explains
  the free, open-source JSON API for DWD open weather data (no API key, DWD terms of use apply), what it returns, five uses on a farm
  and its limits (nearest station, spare-time service, DWD source note). The example call in the article was tested live. Every use in the article
  has a reference (QS and TOPPS drift guidance, Yara newsletter and TLL for urea timing, CERES wheat model for temperature sums, DWD warning criteria); uses without a
  reference were removed. The origin of the name BBCH is referenced to the EPPO Reporting Service 2016/204.

- **FAQ in every article (2026-11-02):** each blog post ends with three questions and answers (`faq` list per post in `tools/blog_content.py`,
  English and German). Rendered as native `<details>` elements, so no JavaScript, and added to the page as `FAQPage` structured data by
  `tools/seo.py`. The answers only restate what the article says. The FAQ is not counted in the reading time.

- **LiveSEN funding note (2026-11-02):** the 2018 card on the About page names the funding (ERC Proof of Concept, Horizon 2020, grant
  agreement No 790155, 1 June 2018 to 30 November 2019) and links the CORDIS record `https://cordis.europa.eu/project/id/790155`.
  The CORDIS page lists the call as ERC-2017-PoC. The 2017 card links REDOX SHIELDS the same way (ERC Starting Grant ERC-2016-STG, grant agreement No 715900,
  1 March 2017 to 31 August 2022, host TUM, `https://cordis.europa.eu/project/id/715900`). The page "At a glance" names both grant agreement numbers. The booking calendar button is still a mailto link until a NutriSen booking URL exists.

- **Visibility in AI assistants (2026-11-02):**
  - New page `/nutrisen-at-a-glance/` (German: `/de/nutrisen-at-a-glance/`, menu item "At a glance" / "Auf einen Blick"): a definition list of
    key facts (company, founded, headquarters, register, managing directors, team, contact, agriculture, medical, research origin, awards),
    a four-question FAQ and links to the main pages. Texts in `tools/facts_content.py`, built by `tools/add_blog.py`. All facts come from this
    website (Impressum, About us, Medical, Agriculture) and the CORDIS record. The founding year 2023 comes from the original Impressum
    description; check it, as the awards have no exact dates on the site either.
  - `llms.txt` (written by `tools/seo.py`): short description of the company and the key pages, English and German.
  - `robots.txt` names the common AI crawlers explicitly (all allowed). Remove an entry to block that crawler.
  - Structured data: the Organization block now has the legal name, register number, team members with job titles and profile links, awards
    and topics. The page "At a glance" carries `AboutPage` and `FAQPage` data. Blog posts use a slim publisher block.

- **Article on the Science Advances paper (2026-11-02):** `/blog/oxygen-scavenger-science-advances/` (German: `/de/blog/...`), 3 minutes, with FAQ. Summarises
  "A universal oxygen scavenger for oxidase-based biosensors" (Science Advances 11(37): eadw6133, 12 September 2025, DOI 10.1126/sciadv.adw6133) from the
  Crossref abstract, links the DOI and carries the paper as `citation` in the structured data. Authors Tobias Vöpel, Alaa A. Oughli and Nicolas Plumeré are
  part of the NutriSen team. Only statements of the abstract, the author affiliations and facts from this website are used; the numbers (below 50% without, 99% with the scavenger) are the authors'. Nothing is added on top.

- **Safari feedback (2026-11-02):**
  - Home hero: the panels no longer grow on hover. Both panels share one row grid (CSS subgrid), so tag, headline, text, figures and buttons
    start at the same height on both sides. Browsers without subgrid keep the old bottom-aligned layout.
  - No grey behind the achievements and the team: the home sections are white, cards in white sections are white with a thin border, and the
    savings band on the home page is white (`body.home .ns-calc` in `assets/brand.css`).
  - Reader mode: `tools/semantic.py` (last step) wraps the page content in `<main id="main"><article>` and turns the content `<header>` blocks
    into `<div>`s, because readers drop `<header>` blocks and look for one main article. FAQ answers are now always visible (headline plus
    paragraph) instead of collapsed, since readers skip collapsed content. Checked with Mozilla Readability: 89 to 100% of the text of every page
    is extracted, the rest are buttons. Safari's own Reader could not be tested here.

- **Fertilizer calculator alignment (2026-11-03):** on desktop (901 px and wider) the two columns share one row grid (CSS subgrid, `assets/fcalc.css`), so the
  headers, the three applications, the amount and cost lines and the totals sit at the same height on both sides, whatever the length of the price notes.
  On narrow screens the columns are stacked as before. Run `tools/cachebust.py` after changing the file.
  All fields of the calculator (country, area, fertilizer, price, N content, target) have the same fixed height of 46 px. The selects use their own arrow
  (`appearance:none`), because Safari draws native selects with a different height than text inputs.

- **Hero glass boxes (2026-11-03):** the two labels above the headlines have the same width and height, and the figure boxes (15% / 10% and Lactate / Creatinine) are the same size on both sides.
- **Cache busting (2026-11-03):** `tools/cachebust.py` (last step) adds `?v=<hash>` to every `assets/*.css` and `assets/*.js` reference. The hosting caches
  these files for a long time (GitHub Pages 10 minutes, the `.htaccess` for IONOS one month), so without it visitors can keep seeing an old style
  sheet after an update. Run it again after every change to a CSS or JS file in `assets/`. The home buttons no longer move on hover either.

- **Corporate design on all pages (2026-11-02):** `assets/brand.css` holds the shared components (navy to blue hero bands,
  green call-to-action bands, white cards with soft shadows, Poppins, green and blue buttons). `tools/restyle.py`
  rebuilds the content of the home page (awards and team), Medical, Agriculture, How does it work, Test your field,
  About us and the two legal pages with these components. The texts and images are taken from the existing pages, so all
  translations keep working. The placeholder page `/the-npknowledge/` is removed (`tools/prune.py`).

- **Average saving (2026-11-02):** besides the "up to" values, the home hero, the Agriculture page and the last step of
  "How does it work" now state that fertilizer use drops by about 15% on average (about 45 EUR per ha at 30 EUR per ha for
  every 10%). The 15% figure is the owner's statement; "up to 30%" and "up to 90 EUR per ha" stay as the upper bound.

- **Analytics switch (2026-11-02):** the original site's analytics script (cdn.pagepulse.info) is OFF, because the site has no
  consent banner (GDPR). The code stays in every page and only runs when the page has `<meta name="ns-analytics" content="on">`
  (default `off`, set right after `<meta charset>`). To turn it back on for all pages, run in the repository root:
  `grep -rl 'name="ns-analytics"' --include=*.html . | xargs sed -i 's/name="ns-analytics" content="off"/name="ns-analytics" content="on"/'`
  and put a consent banner in front of it first. To turn it off again, swap `on` and `off`. `tools/optimize.py` produces this state.

- **SEO (2026-11-02):** `tools/seo.py` runs last and is safe to re-run.
  - Every page has a unique title (50 to 60 characters, with the search term) and a description of 120 to 160 characters, in
    English and German. The texts are in the `T` table at the top of the script. The home pages now have one `<h1>`.
  - One absolute canonical per page (the old relative one is gone), robots meta, Open Graph and Twitter tags with a 1200x630
    image per language (`assets/og-en.jpg`, `assets/og-de.jpg`, rendered by `tools/make_og.js` from `tools/og-card.html`).
  - Structured data (JSON-LD): Organization and WebSite on the home pages (company data from the Impressum), BreadcrumbList on
    every other page, BlogPosting on the two articles, WebApplication on the fertilizer calculator. The old LocalBusiness block of the
    IONOS site is removed: it had the wrong e-mail (info@livesen.eu), empty fields, a broken logo path and invented opening hours.
  - `sitemap.xml` (22 URLs, with hreflang alternates, legal pages left out) and `robots.txt`. After the go-live, submit
    `https://www.nutrisen.eu/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
  - Host name: `www.nutrisen.eu` is the canonical one (the live site redirects `nutrisen.eu` to it). Set up the same 301 redirect
    at IONOS, plus http to https.

## Refreshing the mirror

```
tools/fetch.sh /tmp/nutrisen-work        # downloads pages and assets with wget/curl
python3 tools/build.py /tmp/nutrisen-work /tmp/nutrisen-out
```

Then copy the contents of the output directory over this repository and run, in this order (needs `pip install pillow` and Node.js):
`prune.py`, `apply_home_split.py`, `add_usecases.py`, `add_calculator.py`, `add_fertilizer_calc.py`, `add_blog.py`, `restyle.py`, `i18n.py`, `optimize.py`, `seo.py`, `semantic.py`, `cachebust.py` (all in `tools/`, each as
`python3 tools/<name>.py .`). Copy the new files into a fresh `assets/` first: `home-split.css`, `lang.css`,
`usecases.css`, `calc.css`, `calc.js`, `fcalc.css`, `fcalc.js`, `fertilizer-prices.json`, `nutrisen-logo.webp`, `blog.css`, `brand.css`, `og-en.jpg`, `og-de.jpg`. `i18n.py` refuses to run twice on the same files.
