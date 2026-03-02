table: fact.jord3
description: Resultatopgørelse for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [0=Jordbrug, 11=Landbrug (- 2019), 12=Konventionelt landbrug (- 2019), 13=Økologisk landbrug (-2019), 14=Gartneri (- 2019)]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [0=1. POPULATION, ANTAL BEDRIFTER, 5=2. STIKPRØVE, ANTAL BEDRIFTER, 10=3. JORDBRUGSAREAL, HA, PRIMO, 15=3.1. Selveje, ha, primo (Jordbrugsareal), 20=3.2. Forpagtning, ha, primo (jordbrugsareal) ... 1150=24.1.2. Løbende opsparing (egenkapitalforskydninger) 1.000 kr., 1155=24.2. Kapitalændringer på aktiver (egenkapital forskydninger) 1000 kr., 1160=24.3. Kapitalændringer på gæld (egenkapitalforskydninger) 1000 kr., 1165=24.4. Andre kapitalændringer i alt (egenkapitalforskydning) 1000 kr., 1170=25. EGENKAPITAL, ultimo, 1000 kr.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- CRITICAL: brugstype breakdown by farm type (11/12/13/14) is discontinued from 2020 onwards. From 2020 only brugstype=0 (Jordbrug/all part-time farms) has data. For questions about organic vs. conventional part-time farms after 2019, this table cannot help.
- For the period 2008–2019: use brugstype=13 for "Økologisk landbrug" part-time farms. From 2020: only brugstype=0 available.
- Same regnskposter structure as jord1/jord2 (238 account items). kvartil=1000 for average.
- indhold values are per-farm averages for deltidsbedrifter (part-time farms). Population is smaller than jord1/jord2.