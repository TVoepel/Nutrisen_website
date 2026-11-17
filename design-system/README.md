# NutriSen — design system

NutriSen GmbH (Straubing) is a spin-off of the Technical University of Munich. It makes a single-use biosensor test strip that measures nitrate (and phosphate) in plant sap, read on the field with a handheld potentiostat in a few minutes. Tagline: **Laboratory precise nitrate fertilization.** This system is distilled from the NutriSen pitch decks (KWS visit, Rootcamp October 2026, Bayer pitch November 2026) and is meant for slides, one-pagers, web pages and documents.

## Content fundamentals

**Audience.** Agronomists, seed and crop-science companies, investors, consultants and mid-sized arable farms. Pitches are in English; farmer material is in German (see the section **Deutsch – Material für Landwirte und Berater**: Sie-Ansprache, Begriffe, Zahlenformat). Never mix languages on one page.

**Voice: precise, practical, optimistic.** Scientists talking to farmers: plain words, real numbers, no hype.

- Lead with the number, then the meaning: "**-30%** fertilizer, same yield", "**+25–35%** N prices vs. last season".
- One message per slide, stated in the title. Titles are statements, not topics: "Less fertilizer, same or higher yield", not "Results".
- Frame positively. "From a winter plan to in-season precision", not "Farmers apply blind".
- Explain jargon or drop it. Write "Soil test → fertilizer plan", not "Nmin → DBE". Growth stages (EC 32–39) appear only as a small tag.
- Every external figure carries a source line (footnote style): "Source: agrarheute, top agrar; Oct/Nov 2026".
- On public slides, describe competitors by **technology category** ("Satellite images", "Sap lab"), never by brand next to a weakness. Company names belong in speaker notes or a backup slide.
- Weaknesses are short and factual, prefixed with ✕: "✕ sees green, not nitrogen", "✕ results after days". Strengths with ✓.
- Calls to action are concrete and time-bound: "Let's plan the 2027 season together", with a QR code that opens an email.
- No exclamation marks, no emoji, no superlatives ("revolutionary", "best").

Recurring vocabulary: plant sap · nitrate · test strip · potentiostat / reader · field · season · fertilization (1st, 2nd, 3rd) · ground truth · validated.

## Visual foundations

**Colour roles (the rule everything follows):**

| Role | Token | Meaning |
|---|---|---|
| Brand / structure | `brand-blue` | Titles, logo, planning (soil test), the closing slide background |
| NutriSen / solution / good result | `brand-green` | Anything that is NutriSen or our result: green bar, green tile, green stats, ✓ |
| Status quo / alternatives | `surface-neutral` + `neutral-icon` | Today's tools, competitors, "before" |
| Partners / plan | `surface-tint` + `brand-blue` | Things that work with us |
| Limitation | `negative` | Only the ✕ marker, never fills |

Blue dominates (~60%), white space carries the layout, green is the accent that always points at NutriSen. A reader should find NutriSen on any slide by looking for the green.

**Canvas and grid.** 16:9, designed at 1920 × 1080 (PowerPoint 20 × 11.25 in). `page-margin` 110px left/right. Every content slide: eyebrow (`eyebrow`, UPPERCASE, colour `eyebrow`) at 90px from the top, title (`title`, colour `heading`) right under it, content from ~260px. The NutriSen logo sits top-right (about 145 × 52px) on every slide after the title slide, white on the blue slide. Page number bottom-right in `caption`, as a live slide-number field.

**Slide sandwich.** Title slide: white left half with logo, headline, lead and two stat callouts; a full-bleed field photo on the right half with a soft white fade. Content slides: white. Closing slide: `surface` in the blue theme (#004d9d) with white text, numbered goal cards and a white CTA card with a black QR code.

**Shapes.** Rounded rectangles (`radius-md` tiles, `radius-lg` panels) filled with `surface-tint` or `surface-neutral`; no borders, no shadows, no gradients. Timelines use a grey hairline with month dots and pill-shaped bars (`radius-pill`). Numbers sit in green circles. Hairline `rule` separates table rows. No accent stripes or left-border cards.

**Data.** Big stat callouts (`stat`) with a short label under them. Comparisons as diverging horizontal bars around a zero line: green for less fertilizer, blue for more. Values printed inside the bars in white bold. Market sizes as TAM / SAM / SOM columns.

**Photography.** Real field photography: hands, plants, test strip, reader, the team outdoors. Natural light, green and earth tones, no stock-photo staging. Photos fill whole halves of a slide (bleed), never small framed thumbnails, except the five-step process strip.

## Iconography

Filled glyph icons (Material, Font Awesome, Game Icons via react-icons), placed white in a filled circle: `brand-blue` circles for plan / partners, `neutral-icon` circles for alternatives, a white circle with a green check for NutriSen. Crop-growth icons (seed, sprout, wheat) stand freely above the season timeline, green for young plants and `wheat` for ripe ears. ✓ and ✕ are text glyphs coloured `brand-green` / `negative`. No emoji. The uploaded icons are PNGs at 512px in their final colour (white, green or wheat).

## Signature patterns

1. **Title slide**: logo, `display` headline, `lead`, two stat callouts (green, blue), "A Spin-Off Company of TUM" lockup bottom-left, field photo right.
2. **Season timeline**: OCT–JUN axis, event labels with small blue triangles, a blue "Soil test" bar (Jan–Feb) and a green "NutriSen · EC 32–39" bar (Apr–May), crop icons growing above.
3. **Tool tiles**: a row of icon tiles in three groups: Winter · plan (tint), Spring · today's tools (neutral, ✕ note), Our solution (green, ✓ note).
4. **Results table**: farm · variety / diverging fertilizer bar / yield / economics in green bold.
5. **Stat columns**: TAM / SAM / SOM in `stat`, business model in `stat-sm`, entry-market card in `surface-tint`.
6. **Team**: numbered green circles, name in `subhead`, role in green, one-line bio; team photo bleeding on the right.
7. **Closing CTA (blue)**: four numbered goal cards (`surface-tint` in the blue theme), traction line, white CTA card with QR code (black on white) and contact.
8. **Backup landscape**: three panels (partners, integration partners, alternatives) with ✓/✕ per solution.

## Using this system

Components: `SlideHeader`, `StatCallout`, `ToolTile`, `NumberedCard`, `Pill`, `ProCon`, `SeasonTimeline` (signature pattern 2) and `ResultRow` (signature pattern 4); the last two take German labels as props. Load `tokens.css`, the Fira Sans font (files in `fonts/`, also on Google Fonts) and `components/bundle.css`; components are in `components/bundle.js` as `window.NutriSen` and need React 18. The two themes are `light` (default) and `blue` (set `data-theme="blue"` on the closing slide's root). In PowerPoint use Fira Sans, the hex values above and the pt sizes given in each type style's note. Assets: logos and photos are in **Logos** and **Photos**, icons in **Icons**.
