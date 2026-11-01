(function(){var r=document.getElementById('ns-ha');if(!r)return;var L=document.documentElement.lang||'en',
f=new Intl.NumberFormat(L==='de'?'de-DE':'en-US',{style:'currency',currency:'EUR',maximumFractionDigits:0}),
n=new Intl.NumberFormat(L==='de'?'de-DE':'en-US'),o=document.getElementById('ns-ha-out'),
s=document.querySelector('[data-calc=save]'),g=document.querySelector('[data-calc=gain]'),b=document.querySelector('.ns-calc-btn'),h=b.getAttribute('href');
function u(){var v=+r.value;o.textContent=n.format(v)+' ha';s.textContent=f.format(v*80);g.textContent=f.format(v*240);b.href=h+'?ha='+v}
r.addEventListener('input',u);u()})();
