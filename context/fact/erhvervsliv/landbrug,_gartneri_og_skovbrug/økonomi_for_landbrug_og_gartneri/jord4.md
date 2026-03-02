table: fact.jord4
description: Familiernes økonomi for heltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [2505=Driftsresultat, jordbrug, 2510=Driftsresultat, andre erhverv, 2515=Lønindtægt, bruger (løbende indkomst), 2520=Lønindtægt, andre familiemedlemmer (løbende indkomst), 2525=Pension og dagpenge m.v. (løbende indkomst), 2530=Overskud, brugerbolig (løbende indkomst), 2535=Nettorenteudgift, privat, 2540=Indkomst, 2545=Personlige skatter, 2550=Privatforbrug, 2555=Opsparing]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- brugstype only has 3 values: Konventionelt (2), Økologisk (3), Gartneri (4). There is no "alle heltidsbedrifter" total row in this table.
- Same kvartil and regnskposter structure as the other jord tables. regnskposter here covers family income items (2505–2555): driftsresultat, lønindtægt, indkomst, privatforbrug, opsparing.
- indhold is per-farm average. Covers family/household economy, not the farm business account (for that use jord2).
