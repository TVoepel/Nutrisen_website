// Renders assets/og-en.jpg and assets/og-de.jpg (1200x630) from tools/og-card.html. Needs playwright (npm i playwright-core)
// and a Chromium binary: CHROME=/path/to/chrome node tools/make_og.js
const { chromium } = require('playwright-core'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME, args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  for (const l of ['en', 'de']) {
    await p.goto('file://' + path.resolve(__dirname, 'og-card.html') + (l === 'de' ? '?de' : ''));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    await p.screenshot({ path: path.resolve(__dirname, '../assets/og-' + l + '.jpg'), type: 'jpeg', quality: 84 });
  }
  await b.close();
})();
