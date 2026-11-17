# -*- coding: utf-8 -*-
"""Translation tables for tools/i18n.py. Keys are the visible English (or German) text, HTML-unescaped."""
import blog_content as BC
import facts_content as FC

# ---------------------------------------------------------------- navigation / footer (all pages)
NAV_DE = {
    'Overview': 'Übersicht',
    'At a glance': 'Auf einen Blick',
    'Agriculture': 'Landwirtschaft',
    'Medical': 'Medizin',
    'How does it work': 'So funktioniert es',
    'Test your field': 'Feld testen',
    'Use cases': 'Praxisfälle',
    'Calculator': 'Düngerechner',
    'Impressum': 'Impressum',
    'Datenschutzerklärung': 'Datenschutzerklärung',
    '© Copyright. All rights reserved.': '© Copyright. Alle Rechte vorbehalten.',
}
# English tree: only the two German legal labels and two obvious wording bugs are corrected.
FIX_EN = {
    'Impressum': 'Legal Notice',
    'Datenschutzerklärung': 'Privacy Policy',
    'Seed': 'Send',            # submit button of the contact form read "Seed"
    'Telefon:': 'Phone:',
}
FIX_DE_LEGAL = {'Haftungsauschluss': 'Haftungsausschluss'}   # typo in the German heading

# ---------------------------------------------------------------- page titles and meta descriptions
TITLE_DE = {
    'home': 'NutriSen',
    'medical': 'Medizin',
    'agri': 'Landwirtschaft',
    'how': 'Wie funktioniert der Premium-Service von NutriSen?',
    'test': 'Nitratgehalt Ihres Feldes kostenlos testen',
    'lab': 'Über uns',
    'calc': 'NutriSen Düngerechner: Vergleich von 3 Gaben',
    'cases': 'Praxisfälle 2025/2026: weniger Dünger, gleicher oder höherer Ertrag',
}
TITLE_EN_LEGAL = {'legal': 'NutriSen GmbH Legal Notice', 'privacy': 'Privacy Policy'}
DESC_DE = {
    'We build a new era for fertilization by understanding nitrate concentration in the plant juice, directly on the field.':
        'Wir läuten eine neue Ära der Düngung ein: Wir erfassen die Nitratkonzentration im Pflanzensaft direkt auf dem Feld.',
    'We developed the first biosensor test strips that can precisely measure the amount of nitrate, phosphate and potassium in plants, directly on the field.':
        'Wir haben die ersten Biosensor-Teststreifen entwickelt, die die Menge an Nitrat, Phosphat und Kalium in Pflanzen direkt auf dem Feld präzise messen.',
    'Do you wonder every year when and how much fertilizer to apply to the field?\nWe are looking for innovators who want to test a new technology for free.':
        'Fragen Sie sich jedes Jahr, wann und wie viel Dünger Sie auf dem Feld ausbringen sollen?\nWir suchen Innovatoren, die eine neue Technologie kostenlos testen möchten.',
    'In the laboratory we developed the first enzymatic-based sensor for measuring plant nutrients, directly in the field.':
        'Im Labor haben wir den ersten enzymbasierten Sensor zur Messung von Pflanzennährstoffen direkt auf dem Feld entwickelt.',
    'Five practice cases 2025/2026: up to 30 % less fertilizer at the same yield, in individual cases also a higher yield.':
        'Fünf Praxisfälle 2025/2026: bis zu 30 % weniger Dünger bei gleichem Ertrag, in einzelnen Fällen auch mit höherem Ertrag.',
    'Compare your usual fertilization with NutriSen in three applications, with fertilizer price suggestions from official EU data.':
        'Vergleichen Sie Ihre betriebsübliche Düngung mit NutriSen in drei Gaben, mit Düngerpreis-Vorschlägen aus amtlichen EU-Daten.',
    'Company founded in 2023, with headquarters in Straubing.':
        'Unternehmen, gegründet 2023, mit Sitz in Straubing.',
}
DESC_EN_LEGAL = {}   # the English legal pages keep the existing English description

# ---------------------------------------------------------------- text that stays as it is
KEEP = {
    'Eurostat apri_aip_ft', '·',
    '10 ha', '100 ha', '.',
    '1 · Bayern', '2 · Bayern', '3 · Bayern', '4 · Niedersachsen', '5 · Bayern', 'KWS Emerick', 'Kometus', 'KWS Carusum', 'Spectral',
    'Tobias Vöpel', 'Débora Moretti', 'Alaa Oughli', 'Nicolas Plumeré', 'co-CEO', 'CTO', 'CSO',
    'Lactate', 'Name', 'PoC LiveSEN', 'PoC eConfidence', 'EXIST Research Transfer', 'info@nutrisen.eu',
    'Bio-Security, Bönen.', 'Forum Moderne Landwirtschaft, Berlin.', 'Plan B Competition, Straubing.',
    'Foto: Food Hub NRW', '(TRL 4)', '(TRL 2)', 'TRL', 'Telefon:',
}

# ---------------------------------------------------------------- English -> German (content pages)
DE = dict(NAV_DE)
DE.update({
    # --- home: hero
    'Choose your field': 'Wählen Sie Ihren Bereich',
    'For farmers & agronomists': 'Für Landwirte & Agrarberater',
    'Real-time nutrient sensing for smart fertilization': 'Nährstoffmessung in Echtzeit für intelligentes Düngen',
    "Measure the nitrate in your plants' sap directly on the field and fertilize exactly what the crop needs.":
        'Messen Sie das Nitrat im Pflanzensaft direkt auf dem Feld und düngen Sie genau so viel, wie die Kultur braucht.',
    'about 15% less': 'ca. 15 % weniger',
    'fertilizer on average, up to 30% and 90€ per ha possible': 'Dünger im Durchschnitt, bis zu 30 % und 90 € pro ha möglich',
    'up to +10%': 'bis zu +10 %',
    'higher yield possible in some cases': 'Mehrertrag in einzelnen Fällen möglich',
    'Test your field for free': 'Feld kostenlos testen',
    'See how it works': 'So funktioniert es',
    'Free pilot for farms in Bayern. *Calculated for wheat, fertilizer prices 2025–2026.':
        'Kostenloses Pilotprojekt für Betriebe in Bayern. *Berechnet für Weizen, Düngemittelpreise 2025–2026.',
    'or': 'oder',
    'For medical-device makers': 'Für Medizinprodukte-Hersteller',
    'Direct molecular sensing for enabling digital health': 'Direkte Molekülmessung für die digitale Gesundheit',
    'We build electrochemical biosensors that measure molecules in body fluids with high precision. Your device, with better data.':
        'Wir entwickeln elektrochemische Biosensoren, die Moleküle in Körperflüssigkeiten hochpräzise messen. Ihr Gerät, mit besseren Daten.',
    'validated in the lab (TRL 4)': 'im Labor validiert (TRL 4)',
    'Creatinine': 'Kreatinin',
    'Lactate': 'Laktat',
    'Get in touch': 'Kontakt aufnehmen',
    'Explore the platform': 'Plattform entdecken',
    'Award-winning team:': 'Ausgezeichnetes Team:',
    '3rd place Innovationspreis Moderne Landwirtschaft · 2nd place Bio-Security Bönen · 3rd prize Plan B Pitch Competition 2022':
        '3. Platz Innovationspreis Moderne Landwirtschaft · 2. Platz Bio-Security Bönen · 3. Preis Plan B Pitch Competition 2022',
    # --- home: awards and team
    'People are excited about us': 'Die Menschen sind begeistert von uns',
    '3rd Prize in the Plan B Pitch Competition 2022!': '3. Preis beim Plan B Pitch Competition 2022!',
    'Side-by-Side with start-ups that are already in the market, we were able to secure third place - that is only a start. Prize delivered by Braskem!':
        'Seite an Seite mit Start-ups, die bereits am Markt sind, haben wir den dritten Platz erreicht – das ist erst der Anfang. Der Preis wurde von Braskem überreicht!',
    'Since 2007, the Bio-Gründer Wettbewerb supports founders with revolutionary ideas in Bönen.':
        'Seit 2007 unterstützt der Bio-Gründer Wettbewerb in Bönen Gründerinnen und Gründer mit revolutionären Ideen.',
    'In 2022, we secured 2nd Place! Many thanks to Dr. Oliver Bonkamp for his encouragement.':
        '2022 haben wir den 2. Platz belegt! Vielen Dank an Dr. Oliver Bonkamp für seine Ermutigung.',
    'What a night in Berlin!': 'Was für ein Abend in Berlin!',
    'We are very proud for receiving the 3rd place at the Innovationspreis Moderne Landwirtschaft, directly by the hands of Nikola Steinbock from the Rentenbank!':
        'Wir sind sehr stolz, den 3. Platz beim Innovationspreis Moderne Landwirtschaft direkt aus den Händen von Nikola Steinbock von der Rentenbank entgegennehmen zu dürfen!',
    'Diversity is our super power': 'Vielfalt ist unsere Superkraft',
    "Three nations united for one goal: NutriSen's complementary team combines co-inventors with business experts to put the best product in the farmers' hands.":
        'Drei Nationen, ein Ziel: Das sich ergänzende Team von NutriSen vereint Miterfinder mit Wirtschaftsexperten, um den Landwirten das beste Produkt in die Hand zu geben.',
    'Father, husband and biochemistry fan, Tobias dedicates his mind to bring innovative technologies to the world. His biggest aim is to reduce as much agriculture-related GHG emissions as possible.':
        'Vater, Ehemann und Biochemie-Fan: Tobias setzt sich dafür ein, innovative Technologien in die Welt zu bringen. Sein größtes Ziel ist es, die landwirtschaftlichen Treibhausgasemissionen so stark wie möglich zu senken.',
    'A proud Brazilian, Débora combines science and entrepreneurship to deliver useful technologies to the market. Responsible leadership and collaboration are her trademarks.':
        'Als stolze Brasilianerin verbindet Débora Wissenschaft und Unternehmertum, um nützliche Technologien auf den Markt zu bringen. Verantwortungsvolle Führung und Zusammenarbeit sind ihr Markenzeichen.',
    'Leading scientist of this team, Alaa coordinates research and manufacture of our biosensors. His passion is divided between his family and the application of chemistry to solve real-world needs.':
        'Alaa ist der leitende Wissenschaftler des Teams und koordiniert Forschung und Herstellung unserer Biosensoren. Seine Leidenschaft gehört seiner Familie und der Anwendung der Chemie zur Lösung realer Probleme.',
    "Nicolas's vision is the backbone of this company. His research first at the University of Bochum and now at the University of Munich is enabling farmers to better understand their plants.":
        'Nicolas’ Vision ist das Rückgrat dieses Unternehmens. Seine Forschung, zunächst an der Universität Bochum und jetzt an der Universität München, hilft Landwirten, ihre Pflanzen besser zu verstehen.',
    # --- medical
    'Biosensors for boosting digital health': 'Biosensoren für die digitale Gesundheit',
    'A sensor platform for every medical device.': 'Eine Sensorplattform für jedes Medizinprodukt.',
    'Advance digitalization with better DATA': 'Digitalisierung voranbringen mit besseren DATEN',
    'Get lab precision': 'Laborpräzision erhalten',
    'Our biosensor platform can calibrate your device with high precision.':
        'Unsere Biosensor-Plattform kann Ihr Gerät hochpräzise kalibrieren.',
    'Stay ahead': 'Bleiben Sie voraus',
    'Digitalization is only powerful with good data. We can be your new USP.':
        'Digitalisierung ist nur mit guten Daten leistungsfähig. Wir können Ihr neues Alleinstellungsmerkmal sein.',
    'Innovate. Really.': 'Wirklich innovativ.',
    'The combination of tools is the secret for exceptional results.':
        'Die Kombination der Werkzeuge ist das Geheimnis außergewöhnlicher Ergebnisse.',
    'Overview of molecules in the pipeline': 'Übersicht der Moleküle in der Pipeline',
    'VALIDATED IN THE LAB': 'IM LABOR VALIDIERT',
    'Cholesterol': 'Cholesterin',
    'CONCEPTUAL PHASE': 'KONZEPTPHASE',
    'We are all about R&D': 'Bei uns dreht sich alles um F&E',
    'We build electrochemical biosensors to measure molecules in body fluids with high precision.':
        'Wir entwickeln elektrochemische Biosensoren, die Moleküle in Körperflüssigkeiten hochpräzise messen.',
    'If your medical device targets such molecules and it is very convenient for the patient to use, but you need more comprehensive data, talk to us.':
        'Wenn Ihr Medizinprodukt solche Moleküle erfasst und für Patientinnen und Patienten sehr bequem zu verwenden ist, Sie aber umfassendere Daten benötigen, sprechen Sie uns an.',
    "Let's see what we can revolutionize together.": 'Lassen Sie uns gemeinsam sehen, was wir revolutionieren können.',
    # --- agriculture
    'Real-time nutrient sensing': 'Nährstoffmessung in Echtzeit',
    'for smart fertilization': 'für intelligentes Düngen',
    'From Germany to every field.': 'Aus Deutschland auf jedes Feld.',
    'Boost your experience and GROW by': 'Verbessern Sie Ihren Anbau und WACHSEN Sie, indem Sie',
    'saving fertilizers': 'Dünger sparen',
    'ABOUT 15% LESS ON AVERAGE, UP TO 30%: savings of about 45€, up to 90€ per Ha.': 'CA. 15 % WENIGER IM DURCHSCHNITT, BIS ZU 30 %: Einsparung von ca. 45 €, bis zu 90 € pro Hektar.',
    'supporting yield': 'den Ertrag unterstützen',
    'In some cases up to 10% higher yield is possible, depending on farm and season.': 'In einzelnen Fällen sind bis zu 10 % Mehrertrag möglich, abhängig von Betrieb und Saison.',
    'being resilient': 'widerstandsfähig werden',
    'and cultivating now, the future of agriculture.': 'und schon heute die Zukunft der Landwirtschaft gestalten.',
    '*values calculated for wheat farmers, fertilizer prices 2025–2026: 30€ per Ha for every 10% of fertilizer.': '*Werte berechnet für Weizenanbau, Düngemittelpreise 2025–2026: 30 € pro Hektar je 10 % Dünger.',
    'Per year, we aim to save for Europe': 'Pro Jahr wollen wir für Europa einsparen',
    '2 Million': '2 Millionen',
    'TONS OF FERTILIZERS': 'TONNEN DÜNGEMITTEL',
    '2 Billion €': '2 Milliarden €',
    'IN FERTILIZER IMPORTS': 'AN DÜNGEMITTELIMPORTEN',
    '20 Million': '20 Millionen',
    'TONS OF CO2': 'TONNEN CO2',
    'Exactly as a blood sugar test, our biosensor determines the concentration of nitrate in plant juice. Just a drop is enough to give instant results.':
        'Genau wie ein Blutzuckertest bestimmt unser Biosensor die Nitratkonzentration im Pflanzensaft. Ein Tropfen genügt für ein sofortiges Ergebnis.',
    'We bring laboratory precision to the field!': 'Wir bringen Laborpräzision aufs Feld!',
    'Check here how does it work': 'Hier sehen, wie es funktioniert',
    'We all know that fields are not homogeneous. With satellite data we are able to understand field variability so as to apply only 3 measurements to the whole field!':
        'Wir alle wissen, dass Felder nicht homogen sind. Mit Satellitendaten erfassen wir die Variabilität des Feldes, sodass nur 3 Messungen für das gesamte Feld nötig sind!',
    'All communication and information on how and where to take the plant samples are indicated directly to the farmer through a dedicated app. It also calculates and deliver the concentration results.':
        'Alle Informationen dazu, wie und wo die Pflanzenproben zu nehmen sind, erhält der Landwirt direkt über eine eigene App. Sie berechnet außerdem die Konzentrationsergebnisse und stellt sie bereit.',
    # --- how does it work
    'What if your plants': 'Was wäre, wenn Ihre Pflanzen',
    'could say': 'sagen könnten,',
    'exactly what they need?': 'was sie genau brauchen?',
    'Our sensors measure the': 'Unsere Sensoren messen',
    'exact amount of nutrients': 'die genaue Nährstoffmenge,',
    'your plants have in the moment of the measurement.': 'die Ihre Pflanzen im Moment der Messung enthalten.',
    'Through data retrieved from satellite platforms, we understand': 'Anhand von Satellitendaten erkennen wir',
    'the variability of your field': 'die Variabilität Ihres Feldes',
    'and calculate the needs for each condition.': 'und berechnen den Bedarf für jede Gegebenheit.',
    'Register your field': 'Feld registrieren',
    'Get access to our fertilization recommendation platform, so as you can register your fields.':
        'Erhalten Sie Zugang zu unserer Düngeempfehlungs-Plattform und registrieren Sie Ihre Felder.',
    "Don't worry, your data is yours and only yours.": 'Keine Sorge: Ihre Daten gehören Ihnen und nur Ihnen.',
    'Receive an overview': 'Überblick erhalten',
    'By registering the fields, the platform will retrieve the satellite data from the Copernicus program, so as to understand how green your fields is and how many shades of green they have!':
        'Mit der Registrierung der Felder ruft die Plattform die Satellitendaten des Copernicus-Programms ab, um zu erkennen, wie grün Ihre Felder sind und wie viele Grüntöne sie haben!',
    'Empower your data': 'Mehr aus Ihren Daten machen',
    'Satellite data is a beginning, but not enough.': 'Satellitendaten sind ein Anfang, aber nicht genug.',
    'Upgrade your account and receive at home the sensors you need for summer and winter seasons.':
        'Erweitern Sie Ihr Konto und erhalten Sie die Sensoren für Sommer- und Wintersaison bequem nach Hause.',
    'Check your plants': 'Pflanzen prüfen',
    'With the help of satellite, the fertilization platform will spot three locations that are representative for the whole field and its variability.':
        'Mithilfe von Satellitendaten bestimmt die Düngeplattform drei Stellen, die für das gesamte Feld und seine Variabilität repräsentativ sind.',
    'There you can collect a couple of plants, extract the juice, and measure with the sensor.':
        'Dort entnehmen Sie einige Pflanzen, pressen den Saft aus und messen ihn mit dem Sensor.',
    'Time is gold': 'Zeit ist Gold',
    'At the very spot, you will receive the information about the nutrient status of your plants.':
        'Direkt vor Ort erhalten Sie die Information über den Nährstoffstatus Ihrer Pflanzen.',
    'Even without internet, the platform can calculate the amount of fertilizers needed according to the nutrient status of the field.':
        'Auch ohne Internet kann die Plattform anhand des Nährstoffstatus des Feldes die benötigte Düngermenge berechnen.',
    'No more, no less.': 'Nicht mehr, nicht weniger.',
    'A win-win situation': 'Eine Win-win-Situation',
    'NutriSen sensors can help to reduce applied fertilizer by about 15% on average, and by up to 30%. In some cases, up to 10% higher yield is possible.':
        'NutriSen-Sensoren können helfen, den Düngereinsatz im Durchschnitt um ca. 15 % und um bis zu 30 % zu senken. In einzelnen Fällen sind bis zu 10 % Mehrertrag möglich.',
    'This could mean savings of about 45€ on average and up to 90€ per hectare*.':
        'Das können Einsparungen von ca. 45 € im Durchschnitt und bis zu 90 € pro Hektar* bedeuten.',
    '*fertilizer prices 2025–2026, wheat farmers: 30€ per Ha for every 10% of fertilizer': '*Düngemittelpreise 2025–2026, Weizenanbau: 30 € pro Hektar je 10 % Dünger',
    "We've got your back": 'Wir stehen hinter Ihnen',
    'Power up the experience that you have, with the technology we can provide.':
        'Ergänzen Sie Ihre Erfahrung mit der Technologie, die wir Ihnen bieten.',
    "The climate and environment are changing too fast and we won't rest until farmers receive the support they deserve.":
        'Klima und Umwelt verändern sich zu schnell, und wir ruhen nicht, bis Landwirte die Unterstützung erhalten, die sie verdienen.',
    # --- test your field (contact form)
    'Do you have a farm in Bayern?': 'Haben Sie einen Betrieb in Bayern?',
    'We are looking for partners': 'Wir suchen Partner',
    'Message': 'Nachricht',
    'This field is mandatory': 'Dieses Feld ist ein Pflichtfeld',
    'I agree that this data is stored and processed for the purpose of contacting me. I am aware that I can revoke my consent at any time.*':
        'Ich stimme zu, dass meine Daten zum Zweck der Kontaktaufnahme gespeichert und verarbeitet werden. Mir ist bewusst, dass ich meine Einwilligung jederzeit widerrufen kann.*',
    '* Indicates required fields': '* Pflichtfelder',
    'Seed': 'Absenden',
    'An error occurred while sending your message. Please try again.':
        'Beim Senden Ihrer Nachricht ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.',
    'Thank you for your message! We will get back to you as soon as possible.':
        'Vielen Dank für Ihre Nachricht! Wir melden uns so schnell wie möglich bei Ihnen.',
    "Let's measure the nitrate of your plants.": 'Lassen Sie uns den Nitratgehalt Ihrer Pflanzen messen.',
    'E-mail:': 'E-Mail:',
    'Headquarters: Straubing, Germany.': 'Firmensitz: Straubing, Deutschland.',
    # --- from lab to field
    'First, the science': 'Zuerst die Wissenschaft',
    'The enzyme we needed to place in the sensor is very sensitive to oxygen, thus very complicated to use in an open environment, such as any agricultural field.':
        'Das Enzym, das wir im Sensor einsetzen mussten, reagiert sehr empfindlich auf Sauerstoff und ist deshalb in einer offenen Umgebung wie einem landwirtschaftlichen Feld nur schwer zu verwenden.',
    'So we had to create a way to protect the enzyme without compromising the measurement - which was never done before.':
        'Also mussten wir einen Weg finden, das Enzym zu schützen, ohne die Messung zu beeinträchtigen – das war zuvor noch nie gelungen.',
    'And we nailed it, supported by the Redox Shields Project.': 'Und wir haben es geschafft, unterstützt durch das Projekt Redox Shields.',
    'Learn more': 'Mehr erfahren',
    'Funded by the European Research Council (ERC) under Horizon 2020, grant agreement No 790155.':
        'Gefördert vom Europäischen Forschungsrat (ERC) im Programm Horizont 2020, Finanzhilfevereinbarung Nr. 790155.',
    'View LiveSEN on CORDIS': 'LiveSEN bei CORDIS ansehen',
    'Funded by the European Research Council (ERC) under Horizon 2020, grant agreement No 715900.':
        'Gefördert vom Europäischen Forschungsrat (ERC) im Programm Horizont 2020, Finanzhilfevereinbarung Nr. 715900.',
    'View REDOX SHIELDS on CORDIS': 'REDOX SHIELDS bei CORDIS ansehen',
    'As part of the ERC Proof-of-Concept Grant LiveSen, our group was able to put all necessary parts into a small electrochemical biosensor. Now farmers are able to measure nitrate in their plants directly on the field!':
        'Im Rahmen des ERC Proof-of-Concept Grants LiveSen konnte unsere Gruppe alle notwendigen Komponenten in einem kleinen elektrochemischen Biosensor vereinen. Nun können Landwirte das Nitrat in ihren Pflanzen direkt auf dem Feld messen!',
    'The EU-funded eCONFIDENCE project aimed to explore potential commercial applications of a multisensory test strip, as well as the oxygen binders needed for it, patented under the European Research Council Starting Grant "REDOX SHIELDS". Such multi-analyte test strips can be used to calibrate the millions of data points generated every day by wearable technologies, improving the accuracy of non-invasive sensors in Big Data applications for health and fitness. We continued to improve the biosensor, also for health applications!':
        'Das EU-geförderte Projekt eCONFIDENCE untersuchte mögliche kommerzielle Anwendungen eines Multisensor-Teststreifens sowie der dafür nötigen Sauerstoffbinder, patentiert im Rahmen des ERC Starting Grants „REDOX SHIELDS“. Solche Multi-Analyt-Teststreifen können genutzt werden, um die Millionen Datenpunkte zu kalibrieren, die Wearables täglich erzeugen, und so die Genauigkeit nicht-invasiver Sensoren in Big-Data-Anwendungen für Gesundheit und Fitness zu verbessern. Wir haben den Biosensor weiter verbessert, auch für Gesundheitsanwendungen!',
    'After publishing outstanding papers and patenting the technology behind the biosensor, we were able to secure a EXIST Research Transfer funding, taking a step closer to the market.':
        'Nach herausragenden Veröffentlichungen und der Patentierung der Technologie hinter dem Biosensor konnten wir eine EXIST-Forschungstransfer-Förderung gewinnen und sind dem Markt einen Schritt nähergekommen.',
    'Compare your own fertilization in detail': 'Eigene Düngung im Detail vergleichen',
    # --- fertilizer calculator page
    'Fertilizer calculator': 'Düngerechner',
    'NutriSen fertilizer calculator:': 'NutriSen Düngerechner:',
    'compare 3 applications': 'Vergleich von 3 Gaben',
    'Compare your usual fertilization with a NutriSen optimized one. Fertilizer prices are suggested from official EU data and can be replaced by your own purchase prices.':
        'Vergleichen Sie Ihre betriebsübliche Düngung mit einer NutriSen-optimierten Düngung. Düngerpreise werden aus amtlichen EU-Daten vorgeschlagen und können durch Ihre eigenen Einkaufspreise ersetzt werden.',
    'This calculator needs JavaScript.': 'Dieser Rechner benötigt JavaScript.',
    'Want exact numbers for your fields?': 'Möchten Sie genaue Zahlen für Ihre Felder?',
    'Our sensors and the fertilization platform show what each field really needs.': 'Unsere Sensoren und die Düngeplattform zeigen, was jedes Feld wirklich braucht.',
    "May contain market data from the source: European Commission – Agri-food data portal (agridata.ec.europa.eu). These are aggregated EU market data reported by the Member States. No liability is accepted for the up-to-date accuracy of this data or for trading decisions or losses resulting from it. The European Commission, for its part, excludes any liability for the use of its API and portal data. All other prices in this calculator are based on the user's own purchase prices entered by the user.":
        'Enthält ggf. Marktdaten der Quelle: Europäische Kommission – Agri-Food Data Portal (agridata.ec.europa.eu). Es handelt sich um aggregierte, von den Mitgliedstaaten gemeldete EU-Marktdaten. Für die tagesaktuelle Richtigkeit dieser Daten oder daraus resultierende Handelsentscheidungen/-verluste wird keine Haftung übernommen. Die Europäische Kommission schließt ihrerseits jegliche Haftung für die Nutzung ihrer API- bzw. Portaldaten aus. Alle übrigen Preisangaben in diesem Rechner beruhen auf selbst erfassten, eigenen Einkaufspreisen des Nutzers.',
    'Suggested fertilizer prices come, where shown, from the Eurostat dataset apri_aip_ft “Purchase prices for fertilisers” (annual average 2025, per tonne of nutrient, marked provisional by Eurostat). Values that differ strongly from the EU median are not used. The disclaimer above applies accordingly.':
        'Vorgeschlagene Düngerpreise stammen, soweit angezeigt, aus dem Eurostat-Datensatz apri_aip_ft „Purchase prices for fertilisers“ (Jahresdurchschnitt 2025, je Tonne Nährstoff, von Eurostat als vorläufig gekennzeichnet). Werte, die stark vom EU-Median abweichen, werden nicht verwendet. Der obige Haftungsausschluss gilt entsprechend.',
    'Sources:': 'Quellen:',
    '· Background:': '· Hintergrund:',
    'Research behind the sensors:': 'Forschung hinter den Sensoren:',
    'New in Science Advances: a universal oxygen scavenger for oxidase-based biosensors': 'Neu in Science Advances: ein universeller Sauerstofffänger für Oxidase-Biosensoren',
    'Nutrient prices: why the EU reports them and how to use them': 'Nährstoffpreise: Warum die EU sie meldet und wie Sie sie nutzen',
    'EU Agri-food data portal': 'Agri-Food Data Portal der EU',
    # --- calculator
    'What could NutriSen save on your farm?': 'Was kann NutriSen auf Ihrem Betrieb einsparen?',
    'Move the slider to your farm size.': 'Stellen Sie den Regler auf Ihre Betriebsgröße.',
    'Your farm size': 'Ihre Betriebsgröße',
    '1,000 ha': '1.000 ha',
    '€9,000': '9.000 €',
    'up to': 'bis zu',
    'possible savings per year, up to 90 € per ha, with up to 30% less fertilizer': 'mögliche Einsparung pro Jahr, bis zu 90 € pro ha, bei bis zu 30 % weniger Dünger',
    'Up-to value based on fertilizer prices of 2025–2026: 30 € per ha for every 10% less fertilizer. Actual savings depend on current prices and on the farm, see the': 'Obergrenze auf Basis der Düngemittelpreise 2025–2026: 30 € pro ha je 10 % weniger Dünger. Die tatsächliche Einsparung hängt von den aktuellen Preisen und vom Betrieb ab, siehe die',
    'practice cases': 'Praxisfälle',
    # --- use cases
    'Results from practice': 'Ergebnisse aus der Praxis',
    'Practice cases 2025/2026:': 'Praxisfälle 2025/2026:',
    'less fertilizer, same or higher yield': 'weniger Dünger, gleicher oder höherer Ertrag',
    'up to −30 %': 'bis zu −30 %',
    'fertilizer compared to the standard recommendation': 'Dünger im Vergleich zur Standardempfehlung',
    'up to +14 %': 'bis zu +14 %',
    'extra yield in individual cases': 'Mehrertrag in einzelnen Fällen',
    'up to 90 €/ha': 'bis zu 90 €/ha',
    'savings on fertilizer costs': 'Einsparung bei den Düngerkosten',
    'up to +150 €/ha': 'bis zu +150 €/ha',
    'extra revenue in individual cases': 'Mehrerlös in einzelnen Fällen',
    'Practice cases 2025/2026': 'Praxisfälle 2025/2026',
    'Farm · variety': 'Betrieb · Sorte',
    'Fertilizer amount compared to DBE': 'Düngermenge im Vergleich zur DBE',
    'Yield': 'Ertrag',
    'Economic result': 'Wirtschaftlich',
    'Wheat KWS Carusum': 'Weizen KWS Carusum',
    'within the DBE': 'im Rahmen der DBE',
    'same yield': 'gleicher Ertrag',
    '36 €/ha saved': '36 €/ha gespart',
    '30 €/ha saved': '30 €/ha gespart',
    '90 €/ha saved': '90 €/ha gespart',
    '+14 % extra yield': '+14 % Mehrertrag',
    '+5.5 % extra yield': '+5,5 % Mehrertrag',
    '−4 % protein': '−4 % Protein',
    '+150 €/ha revenue': '+150 €/ha Erlös',
    'DBE = fertilizer requirement assessment (Düngebedarfsermittlung) under the German Fertilizer Ordinance (standard recommendation). Fertilizer costs: 30 €/ha per 10 % of fertilizer.':
        'DBE = Düngebedarfsermittlung nach deutscher Düngeverordnung (Standardempfehlung). Düngerkosten: 30 €/ha je 10 % Dünger.',
    'Results of individual farms. Actual savings and yields depend on site, variety and season.':
        'Ergebnisse einzelner Betriebe. Tatsächliche Einsparungen und Erträge hängen von Standort, Sorte und Saison ab.',
    'Curious what your field needs?': 'Neugierig, was Ihr Feld braucht?',
    'We are looking for partner farms in Bayern and test the nitrate status of your plants for free.':
        'Wir suchen Partnerbetriebe in Bayern und messen den Nitratstatus Ihrer Pflanzen kostenlos.',
    'Within EXIST, the sensor has achieved TRL 6, ready to be tested by first clients.':
        'Im Rahmen von EXIST hat der Sensor TRL 6 erreicht und kann von ersten Kunden getestet werden.',
})

# ---------------------------------------------------------------- German legal pages -> English
LEGAL_NOTE_EN = ('This English version is a courtesy translation. Only the German version '
                 '(Impressum) is legally binding.')
LEGAL_NOTE_EN_PRIVACY = ('This English version is a courtesy translation. Only the German version '
                         '(Datenschutzerklärung) is legally binding.')
EN_LEGAL = {
    'Overview': 'Overview', 'Agriculture': 'Agriculture', 'Medical': 'Medical',
    'Impressum': 'Legal Notice', 'Datenschutzerklärung': 'Privacy Policy',
    'Datenschutz': 'Data protection',
    'Verantwortlich:': 'Responsible party:',
    'Deutschland': 'Germany',
    'Kontakt:': 'Contact:',
    'Tel.: +49 23113707127': 'Phone: +49 23113707127',
    'Geschäftsführer:': 'Managing directors:',
    'Registernummer:': 'Commercial register number:',
    'Registergericht:': 'Register court:',
    'AG Straubing': 'Local court (Amtsgericht) Straubing',
    'Haftungsauschluss': 'Disclaimer',
    'Haftung für Inhalte': 'Liability for content',
    'Haftung für Links': 'Liability for links',
    'Urheberrecht': 'Copyright',
    'Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.':
        'The content of our pages has been created with the utmost care. However, we cannot guarantee the accuracy, completeness or timeliness of the content. As a service provider, we are responsible for our own content on these pages in accordance with general law pursuant to § 7 (1) TMG (German Telemedia Act). Pursuant to §§ 8 to 10 TMG, however, we are not obliged as a service provider to monitor transmitted or stored third-party information or to investigate circumstances that indicate unlawful activity. Obligations to remove or block the use of information under general law remain unaffected. Liability in this respect is only possible from the point in time at which we become aware of a specific infringement. Upon becoming aware of such infringements, we will remove the content in question immediately.',
    'Unser Angebot enthält Links zu externen Webseiten Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.':
        'Our website contains links to external third-party websites over whose content we have no influence. We therefore cannot accept any liability for this third-party content. The respective provider or operator of the linked pages is always responsible for their content. The linked pages were checked for possible legal violations at the time of linking. Unlawful content was not recognizable at the time of linking. However, permanent monitoring of the content of linked pages is not reasonable without concrete indications of an infringement. Upon becoming aware of infringements, we will remove such links immediately.',
    'Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.':
        'The content and works created by the site operators on these pages are subject to German copyright law. Reproduction, editing, distribution and any kind of use beyond the limits of copyright law require the written consent of the respective author or creator. Downloads and copies of this page are only permitted for private, non-commercial use. Insofar as the content on this page was not created by the operator, the copyrights of third parties are respected. In particular, third-party content is identified as such. Should you nevertheless become aware of a copyright infringement, please let us know. Upon becoming aware of infringements, we will remove such content immediately.',
    'Die Nutzung unserer Webseite ist in der Regel ohne Angabe personenbezogener Daten möglich. Soweit auf unseren Seiten personenbezogene Daten (beispielsweise Name, Anschrift oder eMail-Adressen) erhoben werden, erfolgt dies, soweit möglich, stets auf freiwilliger Basis. Diese Daten werden ohne Ihre ausdrückliche Zustimmung nicht an Dritte weitergegeben.':
        'Our website can generally be used without providing personal data. Where personal data (for example name, address or email addresses) is collected on our pages, this is always done on a voluntary basis as far as possible. This data will not be passed on to third parties without your express consent.',
    'Wir weisen darauf hin, dass die Datenübertragung im Internet (z.B. bei der Kommunikation per E-Mail) Sicherheitslücken aufweisen kann. Ein lückenloser Schutz der Daten vor dem Zugriff durch Dritte ist nicht möglich.':
        'Please note that data transmission over the internet (e.g. when communicating by email) may have security gaps. Complete protection of data against access by third parties is not possible.',
    'Der Nutzung von im Rahmen der Impressumspflicht veröffentlichten Kontaktdaten durch Dritte zur Übersendung von nicht ausdrücklich angeforderter Werbung und Informationsmaterialien wird hiermit ausdrücklich widersprochen. Die Betreiber der Seiten behalten sich ausdrücklich rechtliche Schritte im Falle der unverlangten Zusendung von Werbeinformationen, etwa durch Spam-Mails, vor.':
        'We hereby expressly object to the use of contact data published as part of the legal notice obligation by third parties for sending advertising and information materials that were not expressly requested. The operators of the pages expressly reserve the right to take legal action in the event of the unsolicited sending of advertising information, for example by spam emails.',
    'Diese Webseite verwendet Webanalytics. Dabei werden keine personenbezogenen Daten verwendet oder Cookies verwendet. Besucher werden z.B. über die IP-Adresse und Browserkennungen eindeutig identifiziert werden. Dabei werden die IP-Adresse und Browserkennung anonymisiert gespeichert, damit keine Rückschlüsse auf die einzelnen Besucher mehr gezogen werden können.':
        'This website uses web analytics. No personal data or cookies are used in the process. Visitors may be uniquely identified, for example, via their IP address and browser identifiers. The IP address and browser identifier are stored in anonymized form so that no conclusions can be drawn about individual visitors.',
}
KEEP_LEGAL = {'Use cases', 'Calculator', 'NutriSen GmbH', 'Europaring 4', '94315 Straubing', 'Email: info@nutrisen.eu',
              'Tobias Vöpel & Alaa A. Oughli', 'HRB 13438', 'How does it work', 'Test your field',
              '© Copyright. All rights reserved.'}

# ---------------------------------------------------------------- blog (texts live in tools/blog_content.py)
DE.update(BC.de_pairs())
TITLE_DE.update({'blog': 'Blog', **{p['key']: p['title']['de'] for p in BC.POSTS}})
DESC_DE[BC.BLOG['desc']['en']] = BC.BLOG['desc']['de']
DESC_DE.update({p['excerpt']['en']: p['excerpt']['de'] for p in BC.POSTS})
# ---------------------------------------------------------------- page "NutriSen at a glance" (tools/facts_content.py)
DE.update(FC.de_pairs())
TITLE_DE['facts'] = FC.FACTS['title']['de']
DESC_DE[FC.FACTS['desc']['en']] = FC.FACTS['desc']['de']
KEEP.update({'Jubil® en détail', 'Blog', '·', 'NutriSen blog'})
KEEP_LEGAL.add('Blog')

# ---------------------------------------------------------------- corporate-design pass (tools/restyle.py): new strings
DE.update({
    'About us': 'Über uns', 'E-mail': 'E-Mail',
    'Proprietary biosensor plus your medical device': 'Eigener Biosensor plus Ihr Medizinprodukt',
    'Proprietary biosensor test strip': 'Eigener Biosensor-Teststreifen',
    'Satellite data': 'Satellitendaten', 'Fertilization platform': 'Düngeplattform',
    'App screen: registration complete': 'App-Ansicht: Registrierung abgeschlossen',
    'Satellite map of a field in the app': 'Satellitenkarte eines Feldes in der App',
    'App screen: upgrade to premium': 'App-Ansicht: Upgrade auf Premium',
    'Wheat plant, plant juice and sensor': 'Weizenpflanze, Pflanzensaft und Sensor',
    'App screen with the nitrate result': 'App-Ansicht mit dem Nitratergebnis',
    'App screen: fertilizer amount per zone': 'App-Ansicht: Düngermenge je Zone',
    'The NutriSen team': 'Das NutriSen-Team',
    'Researchers working in the lab': 'Forscher bei der Laborarbeit',
    'Handheld sensor device in a field': 'Handgerät mit Sensor auf dem Feld',
    'Multisensory test strips': 'Multisensor-Teststreifen',
    'Hand in a blue glove holding a wheat plant': 'Hand im blauen Handschuh mit einer Weizenpflanze',
    'Award ceremony of the Plan B Pitch Competition': 'Preisverleihung beim Plan B Pitch Competition',
    'Logo of the Bio-Security competition': 'Logo des Bio-Security-Wettbewerbs',
    'Logo of the Innovationspreis Moderne Landwirtschaft': 'Logo des Innovationspreises Moderne Landwirtschaft',
})
KEEP.update({'NutriSen', 'LinkedIn', 'Twitter'})
