# Deploying the NutriSen website to IONOS

This is a plain static website plus one small PHP file (`contact.php`) for the contact form. It runs on any IONOS **Webhosting** package with
SFTP and PHP. It does **not** run on **MyWebsite NOW**, the website builder the old site was made with: that product only lets you edit pages in
the builder, and IONOS does not allow switching a MyWebsite package to a hosting package ([IONOS help](https://www.ionos.ca/help/my-account/orders-upgrades/switching-to-another-hosting-package/)).
So the move means: book a Webhosting package, upload the files, then point the domain to it.

Plan about 2 hours for the first time. The visitors see the old site until step 7.

---

## 0. Read this first (things that can go wrong)

1. **Do not cancel MyWebsite NOW before the new site runs.** Keep it for at least two weeks. It is also your way back.
2. **Keep the domain.** According to IONOS, a cancellation that does not say what happens to the domain also ends the domain registration, and website
   and e-mail stop working. When you cancel MyWebsite NOW, check the cancellation page in your account and choose to keep the domain.
3. **Leave the e-mail settings alone.** If `info@nutrisen.eu` is an IONOS mailbox, it is a separate product. In step 7 you only change where the
   *website* points, never the MX records.
4. **Check the privacy policy.** The German privacy policy still says the site uses web analytics. The analytics script is switched off in this version.
   Also check the wording for the contact form (it sends an e-mail and stores nothing). Have this checked legally before going live.

## 1. Get the files

Use the ZIP that comes with this guide (`nutrisen-site.zip`). Or build it yourself from the GitHub repository:

```
git clone https://github.com/TVoepel/Nutrisen_website.git
cd Nutrisen_website
python3 tools/package.py            # creates nutrisen-site.zip
```

Unzip it on your computer. You get about 200 files, 7 MB. The ZIP leaves out `tools/`, `.github/` and the README files, which do not belong on the server.

## 2. Book the web hosting

1. In your IONOS account order a **Webhosting** package (the smallest tariff is enough: 7 MB of files, PHP and SFTP are needed; check that the tariff includes an SSL certificate, otherwise add one).
2. Put it into the same IONOS customer account as the domain `nutrisen.eu`.
   The contact form needs this: IONOS only sends mail from PHP scripts if the sender address belongs to a domain of your contract
   ([IONOS help](https://www.ionos.com/help/hosting/no-sending-of-emails-with-a-different-sender-address/)).

## 3. Create an SFTP user and upload

1. IONOS menu, **Hosting**, choose the package, tile **SFTP & SSH**, **Manage**, create a user ([IONOS help](https://www.ionos.com/help/hosting/setting-up-and-managing-ftp-access/creating-an-sftp/ssh-account/)).
   Note the server name (looks like `access123456789.webspace-data.io`), the user name and the password. Port 22.
2. Open FileZilla or Cyberduck, protocol **SFTP**, enter the data from step 1.
3. Create a folder for the new site, for example `nutrisen`. Open it.
4. Upload **the contents** of the unzipped folder into it (`index.html`, `agriculture`, `assets`, `de`, `wp-content` and so on), not the folder itself.
   Make sure the hidden file `.htaccess` is uploaded too. In FileZilla: Server menu, "Force showing hidden files".
5. If the folder already contains an IONOS placeholder `index.html`, replace it.

## 4. Test on a temporary address

Do not test on the real domain yet.

1. IONOS menu, **Domains & SSL**, choose `nutrisen.eu`, add a subdomain such as `test.nutrisen.eu` and connect it to the folder `nutrisen`
   ([IONOS help](https://www.ionos.co.uk/help/domains/connecting-a-domain-to-your-webspace/connecting-a-domain-to-a-webspace-directory/)).
2. Open `http://test.nutrisen.eu` (it can take a few minutes). If you want https on the test address, activate an SSL certificate for it too.
3. Go through the checklist below.

### Test checklist

- [ ] Home page: both sides of the split hero look identical in height, buttons work.
- [ ] Language switch DE | EN on three different pages.
- [ ] Savings slider on the home page. Click "Test your field for free": the farm size is pre-filled in the message.
- [ ] Fertilizer calculator: change country, fertilizer, area. No "NaN" anywhere. Both columns line up.
- [ ] Blog: open all five articles, the FAQ and the links to the sources.
- [ ] Page "At a glance", "About us" (the two CORDIS links), Impressum, privacy policy.
- [ ] **Contact form**: send one message in English and one in German. Both must arrive at `info@nutrisen.eu` (look in the spam folder too).
      If nothing arrives, see "Mail does not arrive" below.
- [ ] Phone: open the site on a phone, scroll the home page, open the menu.
- [ ] `/sitemap.xml`, `/robots.txt` and `/llms.txt` open.

## 5. Go live

Choose a quiet time. The switch takes minutes, in rare cases up to some hours until every network sees it.

1. **SSL first.** In **Domains & SSL**, make sure an SSL certificate is active for `nutrisen.eu` and `www.nutrisen.eu`. Without it, step 3 below breaks the site.
2. **Connect the domain.**
   - The domain is now connected to MyWebsite NOW. A domain that is connected to another application has to be disconnected first
     ([IONOS help](https://www.ionos.com/help/domains/connecting-a-domain-to-your-website-at-11-ionos/disconnecting-a-domain-from-mywebsite/)).
     Do this under "Manage your MyWebsite" or in the domain settings.
   - Then connect `nutrisen.eu` to the webspace folder `nutrisen` ([IONOS help](https://www.ionos.co.uk/help/domains/connecting-a-domain-to-your-webspace/connecting-a-domain-to-a-webspace-directory/)).
     If the domain does not point to IONOS yet, IONOS offers to make the needed DNS changes for you. Look at what it wants to change and do not touch the MX (e-mail) entries.
   - Do the same for `www.nutrisen.eu`, so both names reach the same folder.
   - Wait until the status changes from "Connecting" to "Active". If the old site still shows, use the link "Update domain info".
3. **Switch on the redirects.** Open `.htaccess` in the webspace and remove the `#` in front of the four lines in the block "Go-live"
   (use a plain text editor, not Word). From now on every visitor ends at `https://www.nutrisen.eu/`. If the site stops loading, put the `#` back.
4. Open `https://www.nutrisen.eu/`, `http://nutrisen.eu` and `https://nutrisen.eu`. All three must end at `https://www.nutrisen.eu/`.
5. Run the checklist from step 4 once more on the real address, especially the contact form.

## 6. After going live

1. **Google Search Console** and **Bing Webmaster Tools**: add the domain `nutrisen.eu`, verify it (DNS TXT record or file) and submit
   `https://www.nutrisen.eu/sitemap.xml`.
2. Check the speed with https://pagespeed.web.dev and the structured data with https://search.google.com/test/rich-results.
3. In IONOS you can delete the test subdomain `test.nutrisen.eu`.
4. After about two weeks without problems you may cancel MyWebsite NOW. **Keep the domain** (see section 0).

## 7. Updating the site later

- Content changes are made in the Git repository (ask for the change, it is built and tested there). Then upload the changed files by SFTP.
  Simple way: unzip a fresh `nutrisen-site.zip` and upload everything again, overwriting. CSS and JS files carry a version number, so
  visitors get the new version immediately.
- **Fertilizer prices.** The file `assets/fertilizer-prices.json` is refreshed once a month by a GitHub workflow in the repository. IONOS does not
  receive it automatically. Upload that one file each month, or let us add an automatic SFTP upload to the workflow, or use
  [IONOS Deploy Now](https://www.ionos.com/hosting/deploy-now), which deploys every change of the GitHub repository by itself (check the current price and PHP support
  there, because the contact form needs PHP).

## 8. If something does not work

- **The site shows an IONOS placeholder page.** The files are in the wrong folder, or the placeholder `index.html` was not replaced. Check that `index.html` lies directly in the connected folder.
- **Pages show without design.** The folders `assets` and `wp-content` are missing or the upload was incomplete. Upload again.
- **Error 500 after editing `.htaccess`.** A typo in the file. Put the `#` back in front of the four lines or upload the original again.
- **Mail does not arrive.** Check the spam folder first. In `contact.php` the line `const FROM = 'noreply@nutrisen.eu';` must use a domain of your IONOS contract.
  IONOS recommends sending through SMTP (PHPMailer) instead of the simple `mail()` function. Ask for this change if the simple version is not reliable.
  To see what happens, IONOS describes a mail log in the help article "PHP Mail() Logs for Error Analysis".
- **Contact form shows "could not be sent".** The file `contact.php` is missing in the root folder or PHP is switched off for the package.
- **Back to the old site.** In Domains & SSL connect the domain to MyWebsite NOW again, as long as that contract still exists.
