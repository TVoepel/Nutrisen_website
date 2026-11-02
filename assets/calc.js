(function(){var sec=document.querySelector('.ns-calc'),r=document.getElementById('ns-ha');if(!sec||!r)return;
var BASE=80, /* EUR saved per ha at the December 2022 price level (published figure, wheat); scaled to the current price level below */
L=document.documentElement.lang==='de'?'de':'en',loc=L==='de'?'de-DE':'en-GB',
f=new Intl.NumberFormat(loc,{style:'currency',currency:'EUR',maximumFractionDigits:0}),n=new Intl.NumberFormat(loc),
o=document.getElementById('ns-ha-out'),s=sec.querySelector('[data-calc=save]'),lb=sec.querySelector('[data-calc=lbl]'),nt=sec.querySelector('[data-calc=note]'),
b=sec.querySelector('.ns-calc-btn'),h=b.getAttribute('href'),per=0,
T={de:{lbl:function(p){return 'gesparte Düngerkosten pro Jahr, bis zu '+n.format(p)+' € pro ha'},note:function(m){return 'Schätzung „bis zu“ auf Basis aktueller Düngemittelpreise (EU-Stickstoffindikator, '+m+'). Weizen. Die Ergebnisse variieren je nach Betrieb, siehe die'}},
en:{lbl:function(p){return 'fertilizer costs saved per year, up to €'+n.format(p)+' per ha'},note:function(m){return 'Up-to estimate based on current fertilizer prices (EU nitrogen indicator, '+m+'). Wheat. Results vary by farm, see the'}}}[L];
function u(){var v=+r.value;o.textContent=n.format(v)+' ha';s.textContent=per?f.format(v*per):'–';b.href=h+'?ha='+v}
r.addEventListener('input',u);u();
fetch(new URL(sec.getAttribute('data-src'),location.href)).then(function(x){if(!x.ok)throw 0;return x.json()}).then(function(d){var a=d.agridata&&d.agridata.N;if(!a||!a.dec2022)throw 0;
per=Math.round(BASE*a.price/a.dec2022);lb.textContent=T.lbl(per);nt.textContent=T.note(new Intl.DateTimeFormat(loc,{month:'long',year:'numeric'}).format(new Date(a.year,a.month-1,1)));u()}).catch(function(){})})();
