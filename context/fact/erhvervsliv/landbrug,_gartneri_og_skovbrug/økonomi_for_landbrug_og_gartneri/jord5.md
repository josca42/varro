table: fact.jord5
description: Familiernes økonomi for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [0=Jordbrug, 12=Konventionelt landbrug (- 2019), 13=Økologisk landbrug (-2019), 14=Gartneri (- 2019)]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [2505=Driftsresultat, jordbrug, 2510=Driftsresultat, andre erhverv, 2515=Lønindtægt, bruger (løbende indkomst), 2520=Lønindtægt, andre familiemedlemmer (løbende indkomst), 2525=Pension og dagpenge m.v. (løbende indkomst), 2530=Overskud, brugerbolig (løbende indkomst), 2535=Nettorenteudgift, privat, 2540=Indkomst, 2545=Personlige skatter, 2550=Privatforbrug, 2555=Opsparing]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- brugstype for deltidsbedrifter: 0=Jordbrug (all), 12–14 are sub-types discontinued after 2019 (same "(- 2019)" pattern as jord3). Post-2019 only code 0 available.
- regnskposter covers family income items (2505–2555) — same set as jord4. For deltidsbedrifter family economy; for heltidsbedrifter use jord4.
- Same kvartil structure: filter to kvartil=1000 for the overall average.
