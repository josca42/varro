table: fact.jord4
description: Familiernes økonomi for heltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [2505=Driftsresultat, jordbrug, 2510=Driftsresultat, andre erhverv, 2515=Lønindtægt, bruger (løbende indkomst), 2520=Lønindtægt, andre familiemedlemmer (løbende indkomst), 2525=Pension og dagpenge m.v. (løbende indkomst), 2530=Overskud, brugerbolig (løbende indkomst), 2535=Nettorenteudgift, privat, 2540=Indkomst, 2545=Personlige skatter, 2550=Privatforbrug, 2555=Opsparing]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- brugstype has only 3 values (2=Konventionelt, 3=Økologisk, 4=Gartneri) — there is no aggregate "alle heltidsbedrifter" row. To compare organic vs. conventional, query brugstype IN ('2','3') directly.
- regnskposter has only 11 family economy account items (2505–2555), all in 1000 kr. These represent the family's total income, not the farm's operational income (use jord2 for the full farm resultatopgørelse). regnskposter=2540 (Indkomst) is the bottom-line family income.
- indhold values are per-family averages for full-time farm households. Never sum across regnskposter (2505 + 2510 ≠ 2540 as indkomst = net of various items).