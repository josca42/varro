table: fact.jord8
description: Nøgletal for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- brugstype: values [0=Jordbrug, 11=Landbrug (- 2019), 12=Konventionelt landbrug (- 2019), 13=Økologisk landbrug (-2019), 14=Gartneri (- 2019)]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [3505=Ejeraflønning, 1000 kr., 3510=Nettoudbytte, 1000 kr., 3515=Rentebelastning, 1000 kr., 3520=Lønningsevne, 1000 kr., 3525=Overskudsgrad, pct., 3530=Afkastningsgrad, pct., 3535=Forrentningsprocent, pct., 3540=Lønningsevne, kr. pr. time, 3541=Værditilvækst pr. fuldtidsekvivalent, 1000 kr., 3542=Soliditetsgrad, pct. (efter hensættelser), 3545=Soliditetsgrad, pct., 3550=Gældsprocent, pct.]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- brugstype for deltidsbedrifter, same pattern as jord3: types 11–14 discontinued after 2019, only code 0=Jordbrug available for recent years.
- regnskposter is the key-ratio set (3505–3550) — same as jord6/jord7. For the full income statement for deltidsbedrifter use jord3.
