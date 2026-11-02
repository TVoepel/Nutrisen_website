# -*- coding: utf-8 -*-
"""Blog posts (English + German). Every factual statement is taken from the sources listed with the post:
European Commission, Eurostat, EU Agri-food data portal, ARVALIS (JUBIL), Justes et al. 1994."""

def T(en, de): return {'en': en, 'de': de}

DATE = '2026-11-01'
DATE_TXT = T('1 November 2026', '1. November 2026')
WPM = 200   # reading speed used for the reading-time label

BLOG = {
    'title': T('Blog', 'Blog'),
    'eyebrow': T('NutriSen blog', 'NutriSen Blog'),
    'lead': T('Background on nutrient prices, plant nutrition and the methods behind smarter fertilisation.',
              'Hintergründe zu Nährstoffpreisen, Pflanzenernährung und den Methoden hinter klügerer Düngung.'),
    'read': T('Read the article', 'Artikel lesen'),
    'back': T('← All articles', '← Alle Artikel'),
    'min': T('min read', 'Min. Lesezeit'),
    'desc': T('Articles about fertiliser prices, plant nutrition and nitrogen management from NutriSen.',
              'Artikel von NutriSen über Düngerpreise, Pflanzenernährung und Stickstoffmanagement.'),
    'sources': T('Sources', 'Quellen'),
}

POSTS = [
 {
  'key': 'post_prices', 'slug': 'nutrient-prices-eu-reporting',
  'tag': T('Market data', 'Marktdaten'),
  'title': T('Nutrient prices: why the EU reports them and how to use them',
             'Nährstoffpreise: Warum die EU sie meldet und wie Sie sie nutzen'),
  'excerpt': T('Fertiliser prices swing with gas, trade and politics. Why the EU tracks them, what the numbers really mean, and how to use them for your own planning.',
               'Düngerpreise schwanken mit Gas, Handel und Politik. Warum die EU sie erfasst, was die Zahlen wirklich bedeuten und wie Sie sie für Ihre Planung nutzen.'),
  'lead': T('When fertiliser gets expensive, every nitrogen decision becomes a financial decision. That is why the European Union tracks and publishes nutrient prices, and why it pays to know what these numbers can and cannot tell you.',
            'Wenn Dünger teuer wird, ist jede Stickstoffentscheidung auch eine finanzielle Entscheidung. Deshalb erfasst und veröffentlicht die Europäische Union Nährstoffpreise, und deshalb lohnt es sich zu wissen, was diese Zahlen aussagen und was nicht.'),
  'blocks': [
   ('h2', T('A market that keeps surprising farmers', 'Ein Markt, der Landwirte immer wieder überrascht')),
   ('p', T("The European Commission describes the EU fertiliser market as persistently volatile since 2021. After Russia's invasion of Ukraine and the energy crisis that followed, prices eased but never returned to pre-COVID levels. They rose again in 2025, and the Commission says the Middle East crisis added to the pressure in February 2026. In April 2026, overall nitrogen fertiliser prices were 71% higher than the 2024 average, and fertiliser affordability, the ratio of fertiliser prices to cereal prices, was at its lowest level since 2022.",
           'Die Europäische Kommission beschreibt den EU-Düngermarkt seit 2021 als dauerhaft volatil. Nach dem russischen Angriff auf die Ukraine und der anschließenden Energiekrise gaben die Preise nach, erreichten aber nie wieder das Niveau vor Corona. 2025 stiegen sie erneut, und im Februar 2026 verstärkte laut Kommission die Krise im Nahen Osten den Druck. Im April 2026 lagen die Stickstoffdüngerpreise insgesamt 71 % über dem Durchschnitt von 2024. Die Erschwinglichkeit von Dünger, das Verhältnis von Düngerpreisen zu Getreidepreisen, war so niedrig wie zuletzt 2022.')),
   ('h2', T('Why nitrogen is so exposed', 'Warum Stickstoff so anfällig ist')),
   ('p', T('Two facts explain much of this. First, nitrogen fertiliser production relies strongly on natural gas, which is both a raw material and an energy source. According to the Commission, gas availability determines about 70% of the production costs. Second, Europe imports a large share of what it spreads: about 30% of its nitrogen fertilisers, 70% of its phosphatic fertilisers and 40% of its potassium fertilisers. A shock on gas markets or along a shipping route can therefore feed straight into the price farmers pay for fertiliser.',
           'Zwei Tatsachen erklären vieles davon. Erstens hängt die Herstellung von Stickstoffdünger stark von Erdgas ab, das zugleich Rohstoff und Energiequelle ist. Laut Kommission bestimmt die Verfügbarkeit von Erdgas etwa 70 % der Produktionskosten. Zweitens importiert Europa einen großen Teil dessen, was es ausbringt: etwa 30 % der Stickstoffdünger, 70 % der Phosphatdünger und 40 % der Kalidünger. Ein Schock auf den Gasmärkten oder auf einer Schifffahrtsroute kann daher direkt auf den Preis durchschlagen, den Landwirte für Dünger zahlen.')),
   ('h2', T('Why the EU reports prices', 'Warum die EU Preise meldet')),
   ('p', T('Collecting prices is not bureaucracy for its own sake. It serves three purposes.',
           'Preise zu erheben ist keine Bürokratie um ihrer selbst willen. Es erfüllt drei Zwecke.')),
   ('olb', [
     T("Early warning. The Commission set up the Fertilisers Market Observatory to cope better with market volatility and to read market signals. It is a platform for market intelligence on prices and stocks, and the Fertiliser Action Plan of 19 May 2026 plans to strengthen this monitoring role.",
       'Frühwarnung. Die Kommission hat die Beobachtungsstelle für den Düngemittelmarkt eingerichtet, um mit Marktschwankungen besser umzugehen und Marktsignale zu erkennen. Sie ist eine Plattform für Marktinformationen zu Preisen und Beständen, und der Düngemittel-Aktionsplan vom 19. Mai 2026 sieht vor, diese Überwachungsrolle zu stärken.'),
     T('Evidence for decisions. Support measures need numbers. In July 2026 EU countries approved 540 million euros of financial relief for farmers hit by higher fertiliser and energy costs. A shared and comparable picture of prices makes such decisions easier to justify and to target.',
       'Belege für Entscheidungen. Hilfsmaßnahmen brauchen Zahlen. Im Juli 2026 haben die EU-Länder 540 Millionen Euro Finanzhilfe für Landwirte gebilligt, die unter höheren Dünger- und Energiekosten leiden. Ein gemeinsames, vergleichbares Bild der Preise macht solche Entscheidungen leichter begründbar und gezielter.'),
     T("Transparency and comparability. The action plan calls for a systematic reporting framework to improve market transparency. In statistics, Regulation (EU) 2022/2379 on agricultural input and output, in force since December 2022, set harmonised rules. Under it, Eurostat's new dataset on purchase prices for fertilisers reports annual prices per tonne of nutrient for each reporting Member State.",
       'Transparenz und Vergleichbarkeit. Der Aktionsplan fordert einen systematischen Berichtsrahmen für mehr Markttransparenz. In der Statistik hat die Verordnung (EU) 2022/2379 über Statistiken zu landwirtschaftlichen Betriebsmitteln und Erzeugnissen, seit Dezember 2022 in Kraft, einheitliche Regeln gesetzt. Danach meldet der neue Eurostat-Datensatz zu Einkaufspreisen für Düngemittel jährliche Preise je Tonne Nährstoff für jeden berichtenden Mitgliedstaat.'),
   ]),
   ('h2', T('Two EU sources, two different jobs', 'Zwei EU-Quellen, zwei verschiedene Aufgaben')),
   ('p', T("The Commission's Agri-food data portal publishes monthly EU-level prices for nitrogen, phosphorus and potash, gathered from market intelligence services and expressed in euro per tonne. It is quick, so it works well as a trend indicator. At the time of writing, in November 2026, its latest nitrogen value, for September 2026, is 469 euro per tonne, about 23% above the 2025 average.",
           'Das Agri-Food-Datenportal der Kommission veröffentlicht monatliche Preise auf EU-Ebene für Stickstoff, Phosphor und Kali, gesammelt von Marktinformationsdiensten und in Euro je Tonne angegeben. Es ist schnell und eignet sich deshalb gut als Trendindikator. Zum Zeitpunkt dieses Artikels, im November 2026, liegt der aktuelle Stickstoffwert für September 2026 bei 469 Euro je Tonne, etwa 23 % über dem Durchschnitt von 2025.')),
   ('p', T('Eurostat’s dataset is slower but more detailed. It gives annual prices per Member State for individual products such as calcium ammonium nitrate, urea or urea ammonium nitrate solution, each per tonne of nutrient. The 2025 values were last updated in October 2026.',
           'Der Eurostat-Datensatz ist langsamer, aber detaillierter. Er nennt jährliche Preise je Mitgliedstaat für einzelne Produkte wie Kalkammonsalpeter, Harnstoff oder Harnstoff-Ammonnitrat-Lösung, jeweils je Tonne Nährstoff. Die Werte für 2025 wurden zuletzt im Oktober 2026 aktualisiert.')),
   ('h2', T('What the numbers do not tell you', 'Was die Zahlen nicht verraten')),
   ('p', T('Handle them with care. Eurostat flags the new dataset as provisional. When we compared countries for our fertiliser calculator, some national values were far away from the EU median for the same product, most likely because of different reporting units. We therefore only use values close to the median and ask you to enter your own price when a value looks doubtful. Official prices are also annual or aggregated averages. They will not match the offer from your dealer, which depends on region, quantity, delivery date and timing.',
           'Gehen Sie sorgfältig damit um. Eurostat kennzeichnet den neuen Datensatz als vorläufig. Als wir für unseren Düngerechner die Länder verglichen haben, lagen einige nationale Werte weit vom EU-Median für dasselbe Produkt entfernt, höchstwahrscheinlich wegen unterschiedlicher Meldeeinheiten. Wir verwenden deshalb nur Werte nahe am Median und bitten Sie, Ihren eigenen Preis einzutragen, wenn ein Wert zweifelhaft aussieht. Amtliche Preise sind außerdem Jahres- oder Durchschnittswerte. Sie stimmen nicht mit dem Angebot Ihres Händlers überein, das von Region, Menge, Liefertermin und Zeitpunkt abhängt.')),
   ('p', T('Your own invoice remains the best price there is.', 'Ihre eigene Rechnung bleibt der beste Preis, den es gibt.')),
   ('h2', T('How to use them', 'Wie Sie sie nutzen')),
   ('p', T('Use EU data for direction, not for the second decimal. Check whether prices are trending up or down before you fix your fertilisation budget. Compare your quote with the level in your country. And test what a change in the price per kilogram of nitrogen does to the cost of your three applications.',
           'Nutzen Sie EU-Daten für die Richtung, nicht für die zweite Nachkommastelle. Prüfen Sie, ob die Preise steigen oder fallen, bevor Sie Ihr Düngebudget festlegen. Vergleichen Sie Ihr Angebot mit dem Niveau in Ihrem Land. Und testen Sie, was eine Änderung des Preises je Kilogramm Stickstoff für die Kosten Ihrer drei Gaben bedeutet.')),
   ('cta', {'h': T('Try it with your own numbers', 'Probieren Sie es mit Ihren eigenen Zahlen'),
            'p': T('The NutriSen Düngerechner suggests a price from the Eurostat data for your country where a reliable value exists. You can overwrite it with your own purchase price.',
                   'Der NutriSen Düngerechner schlägt für Ihr Land einen Preis aus den Eurostat-Daten vor, sofern ein verlässlicher Wert vorliegt. Sie können ihn mit Ihrem eigenen Einkaufspreis überschreiben.'),
            'btn': T('Open the calculator', 'Zum Rechner'), 'href': '@calc'}),
   ('note', T('Market data: European Commission (Agri-food data portal) and Eurostat. No liability is accepted for the up-to-date accuracy of this data or for decisions resulting from it.',
              'Marktdaten: Europäische Kommission (Agri-Food-Datenportal) und Eurostat. Für die tagesaktuelle Richtigkeit dieser Daten oder daraus resultierende Entscheidungen wird keine Haftung übernommen.')),
  ],
  'sources': [
   ('https://agriculture.ec.europa.eu/common-agricultural-policy/agri-food-supply-chain/ensuring-availability-and-affordability-fertilisers_en',
    T('European Commission: Ensuring availability and affordability of fertilisers', 'Europäische Kommission: Verfügbarkeit und Erschwinglichkeit von Düngemitteln sichern (englisch)')),
   ('https://ec.europa.eu/eurostat/databrowser/view/apri_aip_ft',
    T('Eurostat: Purchase prices for fertilisers (apri_aip_ft)', 'Eurostat: Einkaufspreise für Düngemittel (apri_aip_ft, englisch)')),
   ('https://agridata.ec.europa.eu/extensions/DashboardFertiliser/FertiliserPrices.html',
    T('EU Agri-food data portal: Fertiliser prices', 'Agri-Food-Datenportal der EU: Düngerpreise (englisch)')),
   ('https://eur-lex.europa.eu/eli/reg/2022/2379/oj',
    T('Regulation (EU) 2022/2379 on statistics on agricultural input and output', 'Verordnung (EU) 2022/2379 über Statistiken zu landwirtschaftlichen Betriebsmitteln und Erzeugnissen')),
  ],
 },
 {
  'key': 'post_jubil', 'slug': 'jubil-nitrate-method',
  'tag': T('Plant nutrition', 'Pflanzenernährung'),
  'title': T('JUBIL®: where the stem-juice nitrate test comes from and why it works',
             'JUBIL®: Woher der Nitrattest im Stängelsaft kommt und warum er funktioniert'),
  'excerpt': T('JUBIL® steers the last nitrogen application in winter wheat from the nitrate content of stem-base juice. Where it comes from, the science behind it, and what it means for sensor-based fertilisation.',
               'JUBIL® steuert die letzte Stickstoffgabe bei Winterweizen über den Nitratgehalt im Saft der Stängelbasis. Woher es kommt, welche Wissenschaft dahintersteht und was es für sensorbasierte Düngung bedeutet.'),
  'lead': T('For three decades, French wheat growers have had a quick nitrate test to decide whether the third nitrogen application is really needed. It is called JUBIL®, and its logic shows how a plant measurement can replace a guess.',
            'Seit drei Jahrzehnten steht französischen Weizenanbauern ein Nitrat-Schnelltest zur Verfügung, mit dem sie entscheiden, ob die dritte Stickstoffgabe wirklich nötig ist. Er heißt JUBIL®, und seine Logik zeigt, wie eine Pflanzenmessung eine Vermutung ersetzen kann.'),
  'blocks': [
   ('link', {'label': T('Official method description at ARVALIS (in French):', 'Offizielle Methodenbeschreibung bei ARVALIS (auf Französisch):'),
             'text': 'Jubil® en détail', 'href': 'https://www.arvalis.fr/jubil-en-detail'}),
   ('h2', T('The problem it solves', 'Das Problem, das es löst')),
   ('p', T('The forecast nitrogen budget, the bilan prévisionnel, calculates a dose by balancing the crop’s nitrogen needs against the nitrogen the soil is expected to supply. In practice, ARVALIS explains, uncertainty about how much nitrogen the soil will really deliver leads farmers to insure themselves by raising the calculated dose. Over-fertilisation costs money, can cause lodging and harms the environment. JUBIL® was designed to avoid it.',
           'Die Stickstoffbilanz, auf Französisch bilan prévisionnel, berechnet eine Düngermenge, indem sie den Stickstoffbedarf der Kultur dem erwarteten Stickstoffangebot des Bodens gegenüberstellt. In der Praxis führt laut ARVALIS die Unsicherheit darüber, wie viel Stickstoff der Boden tatsächlich liefert, dazu, dass Landwirte sich absichern und die berechnete Menge erhöhen. Überdüngung kostet Geld, kann Lager verursachen und schadet der Umwelt. JUBIL® wurde entwickelt, um das zu vermeiden.')),
   ('h2', T('Where it comes from', 'Woher es kommt')),
   ('p', T('The name combines two French terms: JUs de base de tige, the stem-base juice, and BILan prévisionnel, the forecast budget. The system was designed and developed by INRA, today INRAE, together with the Institut Technique des Céréales et des Fourrages (ITCF). The experimental network of ARVALIS – Institut du végétal was used to evaluate it.',
           'Der Name verbindet zwei französische Begriffe: JUs de base de tige, der Saft der Stängelbasis, und BILan prévisionnel, die Stickstoffbilanz. Das System wurde vom INRA, heute INRAE, gemeinsam mit dem Institut Technique des Céréales et des Fourrages (ITCF) entworfen und entwickelt. Das Versuchsnetz von ARVALIS – Institut du végétal diente seiner Bewertung.')),
   ('p', T('The research started in the early 1990s in the agronomy units at Laon and Grignon with a basic question: what does the nitrate content of stem-base juice actually represent from a physiological point of view? The resulting strategy was validated in trials between 1991 and 1993, mainly on the varieties Soissons and Thésée, in about forty different soil and climate situations.',
           'Die Forschung begann Anfang der 1990er-Jahre in den Agronomie-Einheiten in Laon und Grignon mit einer Grundfrage: Was bedeutet der Nitratgehalt im Saft der Stängelbasis physiologisch eigentlich? Die daraus entstandene Strategie wurde in Versuchen zwischen 1991 und 1993 validiert, vor allem mit den Sorten Soissons und Thésée, in etwa vierzig unterschiedlichen Boden- und Klimasituationen.')),
   ('h2', T('What stem-base juice tells you', 'Was der Saft der Stängelbasis verrät')),
   ('p', T('Nitrate is the main form in which wheat takes up nitrogen, but inside the plant it is a minor pool compared with amino acids and proteins. The stem-base juice is a water extract of the plant’s tissues, including cytoplasm, vacuoles, apoplast water and xylem and phloem sap. ARVALIS therefore stresses that the measurement is neither a momentary uptake flow nor a pure sap reading. It reflects the stock of nitrate ions in the whole plant.',
           'Nitrat ist die Hauptform, in der Weizen Stickstoff aufnimmt, in der Pflanze selbst aber ein kleiner Pool im Vergleich zu Aminosäuren und Proteinen. Der Saft der Stängelbasis ist ein wässriger Extrakt aus den Geweben der Pflanze, darunter Zytoplasma, Vakuolen, Apoplastenwasser sowie Xylem- und Phloemsaft. ARVALIS betont deshalb, dass die Messung weder ein momentaner Aufnahmestrom noch eine reine Saftmessung ist. Sie spiegelt den Vorrat an Nitrationen in der gesamten Pflanze wider.')),
   ('p', T('To prove that this stock is a useful signal, it was compared with the nitrogen nutrition index, the reference indicator of a nitrogen deficit. The index is the ratio between the total nitrogen content of the aerial parts and the critical nitrogen content, the minimum needed to maximise dry-matter growth. The critical content is not constant. It falls as the crop accumulates biomass, a dilution effect described for winter wheat by Justes and colleagues in 1994.',
           'Um zu belegen, dass dieser Vorrat ein nützliches Signal ist, wurde er mit dem Stickstoff-Ernährungsindex verglichen, dem Referenzindikator für einen Stickstoffmangel. Der Index ist das Verhältnis zwischen dem Gesamtstickstoffgehalt der oberirdischen Teile und dem kritischen Stickstoffgehalt, dem Minimum, das für maximales Trockenmassewachstum nötig ist. Der kritische Gehalt ist nicht konstant. Er sinkt, wenn der Bestand Biomasse aufbaut, ein Verdünnungseffekt, den Justes und Kollegen 1994 für Winterweizen beschrieben haben.')),
   ('p', T('The comparison showed that nitrate is the earliest of the available diagnostic tools. It reveals the onset of a deficiency well before total nitrogen in the aerial parts drops, dry-matter production falls or yield suffers. It is also discriminating: during stem elongation it separated nitrogen nutrition states created by fertiliser differences of 40 kg N per hectare or even less. And it is robust across a wide range of situations, as long as growth stage, crop density, soil type and cultivar are taken into account.',
           'Der Vergleich zeigte, dass Nitrat das früheste der verfügbaren Diagnoseinstrumente ist. Es zeigt den Beginn eines Mangels deutlich bevor der Gesamtstickstoff in den oberirdischen Teilen sinkt, die Trockenmasseproduktion nachlässt oder der Ertrag leidet. Es trennt außerdem genau: Während der Schossphase unterschied es Stickstoffernährungszustände, die durch Düngerunterschiede von 40 kg N pro Hektar oder sogar weniger entstanden waren. Und es ist robust in einem breiten Spektrum von Situationen, solange Entwicklungsstadium, Bestandesdichte, Bodentyp und Sorte berücksichtigt werden.')),
   ('h2', T('How it works in the field', 'Wie es auf dem Feld funktioniert')),
   ('p', T('JUBIL® couples the measurement with the forecast budget in four steps.', 'JUBIL® koppelt die Messung in vier Schritten mit der Stickstoffbilanz.')),
   ('ol', [
     T('Calculate the total nitrogen dose X with the forecast budget method.', 'Die gesamte Stickstoffmenge X mit der Bilanzmethode berechnen.'),
     T('Apply X minus 40 units of nitrogen in two applications, at full tillering and at the “ear at 1 cm” stage.', 'X minus 40 Einheiten Stickstoff in zwei Gaben ausbringen, zu Vollbestockung und im Stadium „Ähre 1 cm“.'),
     T('Measure the nitrate content of the stem-base juice at the “one node” stage and, depending on the result, at “two nodes” and possibly at “last leaf visible”.', 'Den Nitratgehalt im Saft der Stängelbasis im Stadium „1 Knoten“ messen und je nach Ergebnis bei „2 Knoten“ und gegebenenfalls bei „letztes Blatt sichtbar“.'),
     T('Apply a further 40 to 80 kg N per hectare if, and only if, the nitrate content is at or below the intervention threshold. After a third application, stop measuring.', 'Weitere 40 bis 80 kg N pro Hektar nur dann ausbringen, wenn der Nitratgehalt auf oder unter dem Eingriffsschwellenwert liegt. Nach einer dritten Gabe die Messungen beenden.'),
   ]),
   ('p', T('The test itself is simple. About 60 plants are taken from about 20 representative spots, away from spreader overlaps, headlands and wheel tracks, and early in the morning, because the nitrate content changes during the day. The stem bases are cut and pressed, the juice is diluted, a test strip is dipped in and read after one minute with a portable reflectometer. One example given by ARVALIS is a threshold of 1,000 mg nitrate per litre at the two-node stage and normal crop density.',
           'Der Test selbst ist einfach. Etwa 60 Pflanzen werden an etwa 20 repräsentativen Stellen entnommen, abseits von Überlappungen des Streuers, Vorgewenden und Fahrspuren und früh am Morgen, weil sich der Nitratgehalt im Tagesverlauf ändert. Die Stängelbasen werden geschnitten und gepresst, der Saft wird verdünnt, ein Teststreifen eingetaucht und nach einer Minute mit einem tragbaren Reflektometer abgelesen. Ein Beispiel von ARVALIS ist ein Schwellenwert von 1.000 mg Nitrat pro Liter im Stadium „2 Knoten“ bei normaler Bestandesdichte.')),
   ('h2', T('What had to be learned along the way', 'Was unterwegs gelernt werden musste')),
   ('p', T('Trials in 1994 and 1995 showed that the threshold does not have to change with the fertiliser form, whether ammonium nitrate, nitrogen solution or urea. Varieties, however, differ: some consistently showed higher or lower nitrate than Soissons for the same dose. That led to four variety groups and a multi-site trial in 1996 to calibrate new varieties.',
           'Versuche in den Jahren 1994 und 1995 zeigten, dass der Schwellenwert nicht an die Düngerform angepasst werden muss, ob Ammonsalpeter, Stickstofflösung oder Harnstoff. Sorten unterscheiden sich jedoch: Manche hatten bei gleicher Düngermenge durchgehend höhere oder niedrigere Nitratwerte als Soissons. Das führte zu vier Sortengruppen und zu einem Mehrstandortversuch 1996, um neue Sorten zu kalibrieren.')),
   ('p', T('ARVALIS states the goal clearly: a saving of 40 units of nitrogen compared with the budget dose where possible, and, when a third application is justified, no extra risk of nitrate pollution, because splitting the dose into three applications improves the wheat’s uptake efficiency.',
           'ARVALIS formuliert das Ziel klar: wo möglich eine Einsparung von 40 Einheiten Stickstoff gegenüber der Bilanzmenge und, wenn eine dritte Gabe gerechtfertigt ist, kein zusätzliches Risiko einer Nitratbelastung, weil die Aufteilung auf drei Gaben die Aufnahmeeffizienz des Weizens verbessert.')),
   ('h2', T('Where its limits lie', 'Wo seine Grenzen liegen')),
   ('p', T('Thresholds depend on stage, density, soil and variety, and the sample has to be taken early in the morning and prepared by hand. Above all, the nitrate indicator should not be used after the third application to check whether the crop has been resupplied, because the fertiliser form and rainfall then determine how the nitrate content evolves. ARVALIS has since extended JUBIL® to spring malting barley, maize and potato.',
           'Die Schwellenwerte hängen von Stadium, Dichte, Boden und Sorte ab, und die Probe muss früh am Morgen genommen und von Hand aufbereitet werden. Vor allem sollte der Nitratindikator nach der dritten Gabe nicht mehr genutzt werden, um zu prüfen, ob der Bestand nachversorgt wurde, denn dann bestimmen Düngerform und Niederschlag, wie sich der Nitratgehalt entwickelt. ARVALIS hat JUBIL® inzwischen auf Sommerbraugerste, Mais und Kartoffel ausgeweitet.')),
   ('h2', T('From a test strip to a sensor', 'Vom Teststreifen zum Sensor')),
   ('p', T('JUBIL® established a principle that still holds: nitrate in plant juice is an early and meaningful signal of nitrogen status. NutriSen builds on the same kind of signal. Our biosensor determines the concentration of nitrate in plant juice directly in the field, from a single drop, and the platform uses satellite data to find representative measuring spots. The technology differs, but the question is the same: how much nitrogen does the plant really have right now?',
           'JUBIL® hat ein Prinzip etabliert, das bis heute gilt: Nitrat im Pflanzensaft ist ein frühes und aussagekräftiges Signal für den Stickstoffstatus. NutriSen baut auf derselben Art von Signal auf. Unser Biosensor bestimmt die Nitratkonzentration im Pflanzensaft direkt auf dem Feld aus einem einzigen Tropfen, und die Plattform nutzt Satellitendaten, um repräsentative Messstellen zu finden. Die Technik ist anders, aber die Frage ist dieselbe: Wie viel Stickstoff hat die Pflanze gerade wirklich?')),
   ('cta', {'h': T('See what your own field needs', 'Finden Sie heraus, was Ihr Feld braucht'),
            'p': T('We are looking for partner farms in Bayern and test the nitrate status of your plants for free.',
                   'Wir suchen Partnerbetriebe in Bayern und messen den Nitratstatus Ihrer Pflanzen kostenlos.'),
            'btn': T('Test your field for free', 'Feld kostenlos testen'), 'href': '@test'}),
   ('note', T('This article is an independent explanation based on ARVALIS’s public documentation. JUBIL® is an ARVALIS tool.',
              'Dieser Artikel ist eine unabhängige Erläuterung auf Grundlage der öffentlichen Dokumentation von ARVALIS. JUBIL® ist ein Werkzeug von ARVALIS.')),
  ],
  'sources': [
   ('https://www.arvalis.fr/jubil-en-detail', T('ARVALIS: Jubil® en détail (in French)', 'ARVALIS: Jubil® en détail (auf Französisch)')),
   ('https://www.arvalis.fr/jubil-les-especes-concernees', T('ARVALIS: Jubil®, les espèces concernées (in French)', 'ARVALIS: Jubil®, les espèces concernées (auf Französisch)')),
   ('https://hal.inrae.fr/hal-02710650v1', T('Justes E., Mary B., Meynard J.-M., Machet J.-M., Thelier-Huché L. (1994): Determination of a critical nitrogen dilution curve for winter wheat crops. Annals of Botany 74: 397–407',
                                           'Justes E., Mary B., Meynard J.-M., Machet J.-M., Thelier-Huché L. (1994): Determination of a critical nitrogen dilution curve for winter wheat crops. Annals of Botany 74: 397–407')),
  ],
 },
 {
  'key': 'post_bbch', 'slug': 'bbch-winter-wheat-germany-france',
  'date': '2026-11-02', 'date_txt': T('2 November 2026', '2. November 2026'),
  'tag': T('Plant nutrition', 'Pflanzenernährung'),
  'title': T('Winter wheat, BBCH and nitrogen: how Germany and France time their fertilisation',
             'Winterweizen, BBCH und Stickstoff: Wie Deutschland und Frankreich ihre Düngung takten'),
  'excerpt': T('Wheat takes up nitrogen by growth stage, not by calendar date. How the BBCH scale works, how German and French practice split the nitrogen, and where JUBIL® fits in.',
               'Weizen nimmt Stickstoff nach Entwicklungsstadium auf, nicht nach Kalender. Wie die BBCH-Skala funktioniert, wie deutsche und französische Praxis den Stickstoff aufteilen und wo JUBIL® hineinpasst.'),
  'lead': T('Ask a German and a French wheat grower when to apply the last nitrogen and neither will name a date. Both will name a growth stage. The BBCH scale is the common language behind that answer, and comparing the two countries shows how much room there is for measuring what the plant really needs.',
            'Fragt man einen deutschen und einen französischen Weizenanbauer, wann die letzte Stickstoffgabe fällig ist, nennt keiner ein Datum. Beide nennen ein Entwicklungsstadium. Die BBCH-Skala ist die gemeinsame Sprache hinter dieser Antwort, und der Vergleich beider Länder zeigt, wie viel Spielraum es gibt, genau zu messen, was die Pflanze wirklich braucht.'),
  'blocks': [
   ('h2', T('The BBCH scale in one minute', 'Die BBCH-Skala in einer Minute')),
   ('p', T('BBCH is a uniform decimal code for the growth stages of crops and weeds, named after the institutions that created it: the German Federal Biological Research Centre, the Federal Plant Variety Office and the chemical industry. For cereals, these are the codes that matter for nitrogen.',
           'BBCH ist ein einheitlicher dezimaler Code für die Entwicklungsstadien von Kulturpflanzen und Unkräutern, benannt nach den Einrichtungen, die ihn geschaffen haben: Biologische Bundesanstalt, Bundessortenamt und Chemische Industrie. Für Getreide sind diese Codes für den Stickstoff wichtig.')),
   ('ol', [
     T('BBCH 21 to 29, tillering: from the first tiller to the maximum number of tillers.', 'BBCH 21 bis 29, Bestockung: vom ersten Bestockungstrieb bis zur maximalen Triebzahl.'),
     T('BBCH 30 to 32, start of stem elongation: 30 is the beginning, 31 the first node at least 1 cm above the tillering node, 32 the second node at least 2 cm above the first.', 'BBCH 30 bis 32, Beginn des Schossens: 30 ist der Beginn, 31 der erste Knoten mindestens 1 cm über dem Bestockungsknoten, 32 der zweite Knoten mindestens 2 cm über dem ersten.'),
     T('BBCH 37 and 39, flag leaf: 37 is the flag leaf just visible and still rolled, 39 the flag leaf fully unrolled with the ligule just visible.', 'BBCH 37 und 39, Fahnenblatt: 37 ist das Fahnenblatt gerade sichtbar und noch eingerollt, 39 das Fahnenblatt voll entfaltet, das Blatthäutchen gerade sichtbar.'),
     T('BBCH 49 to 59, ear emergence: from the first awns visible (49) and the beginning of heading (51) to the end of heading (59).', 'BBCH 49 bis 59, Ährenschieben: von den ersten sichtbaren Grannen (49) und dem Beginn des Ährenschiebens (51) bis zu dessen Ende (59).'),
   ]),
   ('h2', T('Why stages beat the calendar', 'Warum Stadien besser sind als der Kalender')),
   ('p', T('Wheat does not take up nitrogen evenly. ARVALIS describes how, between the stage ear at 1 cm and flowering, the crop grows from about 1 tonne to 10 to 15 tonnes of dry matter per hectare and absorbs roughly 150 kg of nitrogen per hectare or more.',
           'Weizen nimmt Stickstoff nicht gleichmäßig auf. ARVALIS beschreibt, dass der Bestand zwischen dem Stadium „Ähre 1 cm“ und der Blüte von etwa 1 Tonne auf 10 bis 15 Tonnen Trockenmasse pro Hektar wächst und dabei rund 150 kg Stickstoff pro Hektar oder mehr aufnimmt.')),
   ('h2', T('Germany: a legal ceiling and three doses', 'Deutschland: eine gesetzliche Obergrenze und drei Gaben')),
   ('p', T('In Germany the starting point is the fertiliser ordinance. Its annex 4 sets the nitrogen requirement value for winter wheat at a yield level of 80 dt per hectare: 230 kg N per hectare for quality groups A and B, 210 for C and 260 for E. The requirement must be determined for each field before substantial amounts are applied, and the sum of all doses must not exceed it. The last dose therefore has an upper limit, as the Thuringian agricultural office TLL puts it: the requirement minus what has already been applied.',
           'In Deutschland ist die Düngeverordnung der Ausgangspunkt. Ihre Anlage 4 legt den Stickstoffbedarfswert für Winterweizen bei einem Ertragsniveau von 80 dt pro Hektar fest: 230 kg N pro Hektar für die Qualitätsgruppen A und B, 210 für C und 260 für E. Der Bedarf muss für jeden Schlag ermittelt werden, bevor wesentliche Mengen ausgebracht werden, und die Summe aller Gaben darf ihn nicht überschreiten. Die letzte Gabe hat deshalb eine Obergrenze, wie das Thüringer Landesamt TLL es formuliert: den Bedarf abzüglich der bisherigen Düngung.')),
   ('p', T('The usual pattern is three doses. The first goes on at the start of vegetation, with the mineral nitrogen in the soil (Nmin) taken into account. The second, the stem-elongation dose, has its optimum in the middle of stem elongation, BBCH 31 to 37, and TLL caps it at 60 kg N per hectare, or 75 at very high yields. The third dose, for the ear, is given from BBCH 37 to the beginning of heading at BBCH 51. Early doses raise the yield more, later ones raise the protein content.',
           'Üblich sind drei Gaben. Die erste erfolgt zu Vegetationsbeginn, unter Berücksichtigung des mineralischen Stickstoffs im Boden (Nmin). Die zweite, die Schossergabe, hat ihr Optimum in der Mitte des Schossens, BBCH 31 bis 37, und wird laut TLL auf 60 kg N pro Hektar begrenzt, bei sehr hohen Erträgen auf 75. Die dritte Gabe, für die Ähre, erfolgt ab BBCH 37 bis zum Beginn des Ährenschiebens bei BBCH 51. Frühe Gaben erhöhen eher den Ertrag, spätere mehr den Proteingehalt.')),
   ('p', T('A late dose does not always pay. TLL points out that drought, a low yield potential or a large nitrogen supply from the soil can reduce its effect or remove it completely, and that only about half of the nitrogen of the last dose leaves the field with the grain.',
           'Eine Spätgabe zahlt sich nicht immer aus. Die TLL weist darauf hin, dass Trockenheit, ein geringes Ertragspotenzial oder ein hohes Stickstoffangebot aus dem Boden ihre Wirkung mindern oder ganz ausbleiben lassen können, und dass nur etwa die Hälfte des Stickstoffs der letzten Gabe mit dem Korn abgefahren wird.')),
   ('p', T('Germany also has its own plant-sap test. A TLL guideline from March 2021 describes a nitrate quick test for winter cereals: sap is pressed from stem pieces taken about 1 cm above the ground and read on a test strip. The colour value from 5 to 0 translates into a dose. For the stem-elongation dose, tested between BBCH 30 and 37, it ranges from none at colour value 5 to 60 to 75 kg N per hectare at 0. The ear dose is tested between BBCH 37 and 55.',
           'Deutschland hat außerdem einen eigenen Pflanzensafttest. Eine Leitlinie der TLL vom März 2021 beschreibt einen Nitrat-Schnelltest für Wintergetreide: Aus Halmstücken, die etwa 1 cm über dem Boden entnommen werden, wird Saft gepresst und auf einem Teststäbchen abgelesen. Der Farbwert von 5 bis 0 wird in eine Gabe übersetzt. Für die Schossergabe, getestet zwischen BBCH 30 und 37, reicht sie von keiner Gabe bei Farbwert 5 bis zu 60 bis 75 kg N pro Hektar bei 0. Die Ährengabe wird zwischen BBCH 37 und 55 getestet.')),
   ('h2', T('France: a budget first, then the plant decides', 'Frankreich: erst die Bilanz, dann entscheidet die Pflanze')),
   ('p', T('French practice starts with a nitrogen budget, the bilan prévisionnel, which gives a total dose X. JUBIL® then splits it and lets the plant decide the end. X minus 40 units of nitrogen go on in two doses, at full tillering and at the stage ear at 1 cm, which roughly marks BBCH 30. Nitrate in the stem-base juice is measured at one node (BBCH 31), if needed at two nodes (BBCH 32) and possibly when the last leaf is visible, around BBCH 37. Only if the nitrate content is at or below the threshold does a third dose of 40 to 80 kg N per hectare follow.',
           'Die französische Praxis beginnt mit einer Stickstoffbilanz, dem bilan prévisionnel, die eine Gesamtmenge X ergibt. JUBIL® teilt sie dann auf und lässt die Pflanze über das Ende entscheiden. X minus 40 Einheiten Stickstoff werden in zwei Gaben ausgebracht, zu Vollbestockung und im Stadium „Ähre 1 cm“, das ungefähr BBCH 30 entspricht. Der Nitratgehalt im Saft der Stängelbasis wird im Stadium „1 Knoten“ (BBCH 31) gemessen, bei Bedarf bei „2 Knoten“ (BBCH 32) und gegebenenfalls bei sichtbarem letztem Blatt, um BBCH 37. Nur wenn der Nitratgehalt auf oder unter dem Schwellenwert liegt, folgt eine dritte Gabe von 40 bis 80 kg N pro Hektar.')),
   ('p', T('ARVALIS timing advice follows the same stages. For 2026 it advised delaying the first dose until early stem elongation or ear at 1 cm, depending on the region, and skipping the tillering dose when residual soil nitrogen is high. The stage ear at 1 cm is only a guide for the second dose: soil supply or rain can move it.',
           'Die Terminempfehlungen von ARVALIS folgen denselben Stadien. Für 2026 riet ARVALIS, die erste Gabe je nach Region bis zum frühen Schossen oder zu „Ähre 1 cm“ zu verschieben und die Bestockungsgabe bei hohem Reststickstoff ausfallen zu lassen. Das Stadium „Ähre 1 cm“ ist für die zweite Gabe nur ein Anhaltspunkt: Bodenangebot oder Regen können sie verschieben.')),
   ('p', T('The last dose stays important. In May 2025, ARVALIS advisers recommended keeping it clearly, between the flag leaf and the swelling of the ear, because ear fertility is a key yield component and wheat keeps absorbing nitrogen after the flag leaf appears.',
           'Die letzte Gabe bleibt wichtig. Im Mai 2025 empfahlen ARVALIS-Berater klar, sie beizubehalten, zwischen Fahnenblatt und Ährenanschwellen, weil die Ährenfruchtbarkeit eine wichtige Ertragskomponente ist und Weizen auch nach dem Erscheinen des Fahnenblatts weiter Stickstoff aufnimmt.')),
   ('h2', T('Side by side', 'Im direkten Vergleich')),
   ('olb', [
     T('Same stages. Both countries place the second dose in stem elongation, around BBCH 30 to 37, and the last dose around the flag leaf and the ear.',
       'Gleiche Stadien. Beide Länder legen die zweite Gabe ins Schossen, um BBCH 30 bis 37, und die letzte Gabe um Fahnenblatt und Ähre.'),
     T('Same measurement. Both read nitrate with a test strip in juice pressed from the stem base.',
       'Gleiche Messung. Beide lesen Nitrat mit einem Teststreifen im Saft ab, der aus der Stängelbasis gepresst wird.'),
     T('Different anchor. In Germany the legal requirement value is a ceiling for all doses, and the test steers within it, never beyond it. In France the budget dose X is the reference, and JUBIL® builds in a saving of 40 units where the plant allows it.',
       'Anderer Anker. In Deutschland ist der gesetzliche Bedarfswert eine Obergrenze für alle Gaben, und der Test steuert innerhalb davon, nie darüber hinaus. In Frankreich ist die Bilanzmenge X der Bezug, und JUBIL® baut eine Einsparung von 40 Einheiten ein, wo die Pflanze es erlaubt.'),
     T('Different question. The German tables give a dose for every colour value of the strip. JUBIL® first asks whether a third dose is needed at all, and only then how much.',
       'Andere Frage. Die deutschen Tabellen nennen für jeden Farbwert des Stäbchens eine Gabe. JUBIL® fragt zuerst, ob überhaupt eine dritte Gabe nötig ist, und erst dann, wie viel.'),
   ]),
   ('h2', T('What this means for measuring in the field', 'Was das für das Messen auf dem Feld bedeutet')),
   ('p', T('Both examples follow the same logic: a plant measurement is only useful if the stage is known. Thresholds depend on stage, density, soil and variety, so the same nitrate reading can mean different things at BBCH 32 and at BBCH 39. NutriSen starts here. Our biosensor determines the nitrate concentration in plant juice directly in the field, and the platform uses satellite data to find representative measuring spots.',
           'Beide Beispiele folgen derselben Logik: Eine Pflanzenmessung ist nur nützlich, wenn das Stadium bekannt ist. Die Schwellenwerte hängen von Stadium, Dichte, Boden und Sorte ab, derselbe Nitratwert kann deshalb bei BBCH 32 und bei BBCH 39 Unterschiedliches bedeuten. Hier setzt NutriSen an. Unser Biosensor bestimmt die Nitratkonzentration im Pflanzensaft direkt auf dem Feld, und die Plattform nutzt Satellitendaten, um repräsentative Messstellen zu finden.')),
   ('cta', {'h': T('See what your own field needs', 'Finden Sie heraus, was Ihr Feld braucht'),
            'p': T('We are looking for partner farms in Bayern and test the nitrate status of your plants for free.',
                   'Wir suchen Partnerbetriebe in Bayern und messen den Nitratstatus Ihrer Pflanzen kostenlos.'),
            'btn': T('Test your field for free', 'Feld kostenlos testen'), 'href': '@test'}),
   ('note', T('This article is an independent explanation based on public documents of German and French agricultural services and ARVALIS. It is not a fertilisation recommendation. Legal limits and advisory figures change, so check the current rules and advice for your region and field.',
              'Dieser Artikel ist eine unabhängige Erläuterung auf Grundlage öffentlicher Unterlagen deutscher und französischer Fachstellen und von ARVALIS. Er ist keine Düngeempfehlung. Rechtliche Grenzen und Beratungswerte ändern sich, prüfen Sie deshalb die aktuellen Vorgaben und Empfehlungen für Ihre Region und Ihr Feld.')),
  ],
  'sources': [
   ('https://en.wikipedia.org/wiki/Cereal_growth_staging_scales', T('Cereal growth staging scales: BBCH and Zadoks codes (Wikipedia)', 'Cereal growth staging scales: BBCH- und Zadoks-Codes (Wikipedia, englisch)')),
   ('https://www.gesetze-im-internet.de/d_v_2017/anlage_4.html', T('Düngeverordnung, Annex 4: nitrogen requirement values (in German)', 'Düngeverordnung, Anlage 4: Stickstoffbedarfswerte')),
   ('https://www.tll.de/www/daten/pflanzenproduktion/duengung/nschnelltest.pdf', T('TLL Thüringen (March 2021): Nitrat-Schnelltest bei Wintergetreide (in German)', 'TLL Thüringen (März 2021): Nitrat-Schnelltest bei Wintergetreide')),
   ('https://www.arvalis.fr/jubil-en-detail', T('ARVALIS: Jubil® en détail (in French)', 'ARVALIS: Jubil® en détail (auf Französisch)')),
   ('https://www.terre-net.fr/arvalis/amp/article/146064/stade-epi-1-cm-du-ble-un-marqueur-determinant-a-savoir-reperer', T('ARVALIS on Terre-net: Stade épi 1 cm du blé (in French)', 'ARVALIS bei Terre-net: Stade épi 1 cm du blé (auf Französisch)')),
   ('https://www.reussir.fr/grandes-cultures/azote-sur-ble-quand-realiser-le-premier-apport-en-2026', T('Réussir Grandes cultures (7 February 2026): Azote sur blé, quand réaliser le premier apport en 2026 (in French)', 'Réussir Grandes cultures (7. Februar 2026): Azote sur blé, quand réaliser le premier apport en 2026 (auf Französisch)')),
   ('https://www.pleinchamp.com/actualite/bles-ne-pas-solder-l-azote-trop-tot-pour-soutenir-le-potentiel-de-rendement', T('ARVALIS on Pleinchamp (13 May 2025): Blés, ne pas solder l’azote trop tôt (in French)', 'ARVALIS bei Pleinchamp (13. Mai 2025): Blés, ne pas solder l’azote trop tôt (auf Französisch)')),
  ],
 },
]

import re as _re
def words(post, lang):
    parts = [post['title'][lang], post['lead'][lang]]
    for kind, v in post['blocks']:
        if kind in ('h2', 'p', 'note'): parts.append(v[lang])
        elif kind in ('ol', 'olb'): parts += [x[lang] for x in v]
        elif kind == 'cta': parts += [v['h'][lang], v['p'][lang]]
        elif kind == 'link': parts.append(v['label'][lang])
    return len(_re.findall(r"\S+", ' '.join(parts)))

def minutes(post):
    return max(1, round(words(post, 'en') / WPM))

def de_pairs():
    """EN text -> DE text for every string of the blog (used by tools/i18n_strings.py)."""
    d = {}
    def add(x): d[x['en']] = x['de']
    for k in ('title', 'eyebrow', 'lead', 'read', 'back', 'desc'): add(BLOG[k])
    add(BLOG['sources']); add(DATE_TXT)
    for p in POSTS:
        if 'date_txt' in p: add(p['date_txt'])
    for p in POSTS: d['%d min read' % minutes(p)] = '%d %s' % (minutes(p), BLOG['min']['de'])
    for p in POSTS:
        for k in ('tag', 'title', 'excerpt', 'lead'): add(p[k])
        for kind, v in p['blocks']:
            if kind in ('h2', 'p', 'note'): add(v)
            elif kind == 'ol':
                for x in v: add(x)
            elif kind == 'olb':   # bold lead-in (first sentence) and rest are separate text nodes
                for x in v:
                    h = {l: x[l].split('. ', 1)[0] + '.' for l in ('en', 'de')}; r = {l: x[l].split('. ', 1)[1] for l in ('en', 'de')}
                    add(h); add(r)
            elif kind == 'cta':
                for k in ('h', 'p', 'btn'): add(v[k])
            elif kind == 'link': add(v['label'])
        for _, label in p['sources']: add(label)
    return d
