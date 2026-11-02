(function(){var r=document.getElementById('ns-ha'),sec=document.querySelector('.ns-calc');if(!r||!sec)return;
var PER_HA=80, /* "up to" saving in EUR per ha: published figure for wheat at December 2022 fertilizer prices */
L=document.documentElement.lang==='de'?'de-DE':'en-GB',f=new Intl.NumberFormat(L,{style:'currency',currency:'EUR',maximumFractionDigits:0}),n=new Intl.NumberFormat(L),
o=document.getElementById('ns-ha-out'),s=sec.querySelector('[data-calc=save]'),b=sec.querySelector('.ns-calc-btn'),h=b.getAttribute('href');
function u(){var v=+r.value;o.textContent=n.format(v)+' ha';s.textContent=f.format(v*PER_HA);b.href=h+'?ha='+v}
r.addEventListener('input',u);u()})();
