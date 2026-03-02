table: fact.jord5
description: Familiernes økonomi for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [0=Jordbrug, 12=Konventionelt landbrug (- 2019), 13=Økologisk landbrug (-2019), 14=Gartneri (- 2019)]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [2505=Driftsresultat, jordbrug, 2510=Driftsresultat, andre erhverv, 2515=Lønindtægt, bruger (løbende indkomst), 2520=Lønindtægt, andre familiemedlemmer (løbende indkomst), 2525=Pension og dagpenge m.v. (løbende indkomst), 2530=Overskud, brugerbolig (løbende indkomst), 2535=Nettorenteudgift, privat, 2540=Indkomst, 2545=Personlige skatter, 2550=Privatforbrug, 2555=Opsparing]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- CRITICAL: brugstype breakdown by farm type (12/13/14) is discontinued from 2020. From 2020 only brugstype=0 (Jordbrug/all part-time farms) has data. Gartneri (14) lost data even earlier. For recent years, cannot distinguish organic vs. conventional part-time family economy.
- Same 11 regnskposter as jord4 (family economy account items). Use brugstype=13 for organic part-time farm families up to 2019.
- Partner table to jord3: jord3 has full resultatopgørelse for deltidsbedrifter; jord5 has family economy for the same population.