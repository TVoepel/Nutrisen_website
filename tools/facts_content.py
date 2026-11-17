# -*- coding: utf-8 -*-
"""Content of the page "NutriSen at a glance" (English + German). Every statement comes from pages of this website
(Impressum, About us, Medical, Agriculture, How does it work), the CORDIS record of LiveSEN or the owners."""

def T(en, de): return {'en': en, 'de': de}

FACTS = {
 'slug': 'nutrisen-at-a-glance',
 'title': T('NutriSen at a glance', 'NutriSen auf einen Blick'),
 'eyebrow': T('Facts', 'Fakten'),
 'nav': T('At a glance', 'Auf einen Blick'),
 'lead': T('NutriSen develops electrochemical biosensors that measure nitrate in plant juice directly in the field, so that farmers can fertilise by need. The same biosensor platform is being developed for medical devices.',
           'NutriSen entwickelt elektrochemische Biosensoren, die Nitrat im Pflanzensaft direkt auf dem Feld messen, damit Landwirte bedarfsgerecht düngen können. Dieselbe Biosensor-Plattform wird für Medizinprodukte entwickelt.'),
 'desc': T('Key facts about NutriSen GmbH: nitrate biosensor for farmers, medical biosensor platform, team, research funding, awards and contact.',
           'Die wichtigsten Fakten zur NutriSen GmbH: Nitrat-Biosensor für Landwirte, medizinische Biosensor-Plattform, Team, Forschungsförderung, Auszeichnungen und Kontakt.'),
 'h_facts': T('Key facts', 'Die wichtigsten Fakten'),
 'h_more': T('More about NutriSen', 'Mehr über NutriSen'),
 'rows': [
  (T('Company', 'Unternehmen'), T('NutriSen GmbH', 'NutriSen GmbH')),
  (T('Founded', 'Gegründet'), T('2023', '2023')),
  (T('Headquarters', 'Sitz'), T('Europaring 4, 94315 Straubing, Germany', 'Europaring 4, 94315 Straubing, Deutschland')),
  (T('Commercial register', 'Handelsregister'), T('HRB 13438, Amtsgericht Straubing', 'HRB 13438, Amtsgericht Straubing')),
  (T('Managing directors', 'Geschäftsführer'), T('Tobias Vöpel and Alaa A. Oughli', 'Tobias Vöpel und Alaa A. Oughli')),
  (T('Team', 'Team'), T('Tobias Vöpel, co-CEO. Alaa Oughli, CTO. Nicolas Plumeré, CSO.', 'Tobias Vöpel, Co-CEO. Alaa Oughli, CTO. Nicolas Plumeré, CSO.')),
  (T('Contact', 'Kontakt'), T('info@nutrisen.eu, +49 231 13707127', 'info@nutrisen.eu, +49 231 13707127')),
  (T('Agriculture', 'Landwirtschaft'),
   T('A biosensor that measures nitrate in plant juice in the field, and a fertilisation recommendation platform that uses satellite data to find representative measuring spots. Within EXIST, the sensor has achieved TRL 6.',
     'Ein Biosensor, der Nitrat im Pflanzensaft auf dem Feld misst, und eine Düngeempfehlungs-Plattform, die Satellitendaten nutzt, um repräsentative Messstellen zu finden. Im Rahmen von EXIST hat der Sensor TRL 6 erreicht.')),
  (T('Possible effect for farms', 'Mögliche Wirkung auf dem Betrieb'),
   T('About 15% less fertiliser on average and up to 30%, in some cases up to 10% higher yield. Values for wheat farms and fertiliser prices of 2025 to 2026, depending on farm and season.',
     'Im Durchschnitt etwa 15 % weniger Dünger und bis zu 30 %, in einzelnen Fällen bis zu 10 % Mehrertrag. Werte für Weizenbetriebe und Düngerpreise von 2025 bis 2026, abhängig von Betrieb und Saison.')),
  (T('Pilot offer', 'Pilotangebot'), T('Free nitrate test for farms in Bayern.', 'Kostenloser Nitrattest für Betriebe in Bayern.')),
  (T('Medical', 'Medizin'),
   T('An electrochemical biosensor platform for medical devices. Pipeline: lactate, TRL 4, validated in the lab. Creatinine, TRL 4, validated in the lab. Cholesterol, TRL 2, conceptual phase.',
     'Eine elektrochemische Biosensor-Plattform für Medizinprodukte. Pipeline: Laktat, TRL 4, im Labor validiert. Kreatinin, TRL 4, im Labor validiert. Cholesterin, TRL 2, Konzeptphase.')),
  (T('Research origin', 'Forschungsursprung'),
   T('ERC Starting Grant REDOX SHIELDS (grant agreement 715900), ERC Proof of Concept LiveSEN (grant agreement 790155), the EU-funded project eCONFIDENCE and EXIST Research Transfer funding.',
     'ERC Starting Grant REDOX SHIELDS (Finanzhilfevereinbarung 715900), ERC Proof of Concept LiveSEN (Finanzhilfevereinbarung 790155), das EU-geförderte Projekt eCONFIDENCE und die Förderung EXIST-Forschungstransfer.')),
  (T('Awards', 'Auszeichnungen'),
   T('3rd place Innovationspreis Moderne Landwirtschaft. 2nd place Bio-Security Bönen 2022. 3rd prize Plan B Pitch Competition 2022.',
     '3. Platz Innovationspreis Moderne Landwirtschaft. 2. Platz Bio-Security Bönen 2022. 3. Preis Plan B Pitch Competition 2022.')),
  (T('Languages', 'Sprachen'), T('English and German', 'Englisch und Deutsch')),
 ],
 'faq': [
  (T('What does NutriSen do?', 'Was macht NutriSen?'),
   T('NutriSen develops electrochemical biosensors. In agriculture, the sensor measures nitrate in plant juice directly in the field, so farmers can adjust fertilisation to what the plants need. In medicine, the same platform is being developed for devices that measure molecules in body fluids.',
     'NutriSen entwickelt elektrochemische Biosensoren. In der Landwirtschaft misst der Sensor Nitrat im Pflanzensaft direkt auf dem Feld, damit Landwirte die Düngung an den Bedarf der Pflanzen anpassen können. In der Medizin wird dieselbe Plattform für Geräte entwickelt, die Moleküle in Körperflüssigkeiten messen.')),
  (T('Where does the technology come from?', 'Woher kommt die Technologie?'),
   T('From research at the University of Bochum, supported by the ERC Starting Grant REDOX SHIELDS and the ERC Proof of Concept grant LiveSEN. NutriSen then received EXIST Research Transfer funding.',
     'Aus der Forschung an der Universität Bochum, unterstützt durch den ERC Starting Grant REDOX SHIELDS und den ERC Proof of Concept Grant LiveSEN. Danach erhielt NutriSen die Förderung EXIST-Forschungstransfer.')),
  (T('Who leads NutriSen?', 'Wer leitet NutriSen?'),
   T('The managing directors are Tobias Vöpel and Alaa A. Oughli. Tobias Vöpel is co-CEO, Alaa Oughli is CTO and Nicolas Plumeré is CSO.',
     'Die Geschäftsführer sind Tobias Vöpel und Alaa A. Oughli. Tobias Vöpel ist Co-CEO, Alaa Oughli ist CTO und Nicolas Plumeré ist CSO.')),
  (T('How can a farm try NutriSen?', 'Wie kann ein Betrieb NutriSen ausprobieren?'),
   T('Farms in Bayern can have the nitrate status of their plants tested for free through the form on the page Test your field. The website also offers calculators for savings and fertilisation costs.',
     'Betriebe in Bayern können den Nitratstatus ihrer Pflanzen kostenlos über das Formular auf der Seite „Feld testen“ messen lassen. Die Website bietet außerdem Rechner für Einsparungen und Düngekosten.')),
 ],
 # (label, target page dir)
 'links': [
  (T('Agriculture', 'Landwirtschaft'), 'agriculture'), (T('How does it work', 'So funktioniert es'), 'agriculture/how-does-it-work'),
  (T('Use cases', 'Praxisfälle'), 'agriculture/use-cases'), (T('Calculator', 'Düngerechner'), 'agriculture/calculator'),
  (T('Test your field', 'Feld testen'), 'agriculture/test-your-field'), (T('Medical', 'Medizin'), 'medical'),
  (T('Blog', 'Blog'), 'blog'), (T('Our story', 'Unsere Geschichte'), 'agriculture/from-lab-to-field'),
 ],
}

def de_pairs():
    d = {}
    def add(x): d[x['en']] = x['de']
    for k in ('title', 'eyebrow', 'nav', 'lead', 'desc', 'h_facts', 'h_more'): add(FACTS[k])
    for lab, val in FACTS['rows']: add(lab); add(val)
    for q, a in FACTS['faq']: add(q); add(a)
    for lab, _ in FACTS['links']: add(lab)
    return d
