table: fact.jord7
description: Nøgletal for alle heltidsbedrifter (gennemsnit) efter bedriftstype årsværk, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- bedriftaars: values [1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 5=Landbrug, 1-3 årsværk ... 560=Væksthusgrøntsager, 563=Frilandsgartneri, 565=Frilandsgrøntsager, 570=Frugt og bær, 575=Planteskole]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [3505=Ejeraflønning, 1000 kr., 3510=Nettoudbytte, 1000 kr., 3515=Rentebelastning, 1000 kr., 3520=Lønningsevne, 1000 kr., 3525=Overskudsgrad, pct., 3530=Afkastningsgrad, pct., 3535=Forrentningsprocent, pct., 3540=Lønningsevne, kr. pr. time, 3541=Værditilvækst pr. fuldtidsekvivalent, 1000 kr., 3542=Soliditetsgrad, pct. (efter hensættelser), 3545=Soliditetsgrad, pct., 3550=Gældsprocent, pct.]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- Same bedriftaars and kvartil structure as jord2. bedriftaars has detailed enterprise subtypes — filter to code 1 (Landbrug) or specific type.
- regnskposter is the same key-ratio set as jord6 (3505–3550). For the full income statement for heltidsbedrifter use jord2.
