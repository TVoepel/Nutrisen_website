/* NutriSen contact form. Replaces the WordPress form script of the old site (window.FormProcessor) and posts to contact.php. */
(function () {
  var me = document.currentScript && document.currentScript.src;
  var endpoint = me ? me.replace(/assets\/contact\.js.*$/, 'contact.php') : '/contact.php';
  var de = document.documentElement.lang === 'de';
  var T = de ? {
    fail: 'Die Nachricht konnte nicht gesendet werden. Bitte schreiben Sie uns an info@nutrisen.eu.',
    sending: 'Wird gesendet …'
  } : {
    fail: 'The message could not be sent. Please write to us at info@nutrisen.eu.',
    sending: 'Sending …'
  };
  window.FormProcessor = function (cfg) {
    if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', function () { window.FormProcessor(cfg); }); return; }
    var form = document.querySelector('form[data-id="' + cfg.formId + '"]');
    if (!form || form.getAttribute('data-ns-ready')) return;
    form.setAttribute('data-ns-ready', '1');
    var started = Date.now();
    var name = form.querySelector('#Name'), msg = form.querySelector('#Message'), box = form.querySelector('.form-input-checkbox');
    var button = form.querySelector('.form-button'), label = button ? button.textContent : '';
    var holder = form.parentNode, errBox = holder.querySelector('.form-error'), okBox = holder.querySelector('.form-success');
    var errText = errBox && errBox.querySelector('span');
    var hp = document.createElement('input');                       // honeypot: invisible for people, bots fill it in
    hp.type = 'text'; hp.name = 'website'; hp.tabIndex = -1; hp.autocomplete = 'off'; hp.setAttribute('aria-hidden', 'true');
    hp.style.cssText = 'position:absolute;left:-9999px;width:1px;height:1px;opacity:0';
    form.appendChild(hp);
    function flag(field, bad) {
      var combo = field.closest('.form-input-combo'), e = combo && combo.querySelector('.form-label-error');
      if (e) e.classList.toggle('form-display-none', !bad);
      if (field.classList) field.classList.toggle('form-input-error', bad);
    }
    function hide(el) { if (el) el.classList.add('form-display-none'); }
    function show(el) { if (el) el.classList.remove('form-display-none'); }
    form.addEventListener('submit', function (ev) {
      ev.preventDefault(); hide(errBox); hide(okBox);
      var bad = [!name.value.trim(), !msg.value.trim(), !box.checked];
      flag(name, bad[0]); flag(msg, bad[1]); flag(box, bad[2]);
      if (bad.some(Boolean)) return;
      button.disabled = true; button.textContent = T.sending;
      var body = new URLSearchParams({ name: name.value, message: msg.value, consent: '1', lang: de ? 'de' : 'en', elapsed: String(Date.now() - started), website: hp.value });
      fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: body })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (!d || !d.ok) throw 0;
          form.reset(); show(okBox);
        })
        .catch(function () { if (errText) errText.textContent = T.fail; show(errBox); })
        .then(function () { button.disabled = false; button.textContent = label; });
    });
  };
  // The page registers its form with window.initFormProcessors.push(fn). Run those callbacks once the page is parsed.
  var queued = window.initFormProcessors || [];
  window.initFormProcessors = { push: function (fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); } };
  for (var i = 0; i < queued.length; i++) window.initFormProcessors.push(queued[i]);
})();
