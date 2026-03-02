table: fact.jord6
description: Nøgletal for alle bedrifter (gennemsnit) efter bedriftstype region standardoutput, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- bedriftstand: values [0=Alle bedrifter, 1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 300=Hovedstaden (region), 302=Sjælland (region), 304=Syddanmark (region), 306=Fyn (landsdel), 308=Sydjylland (landsdel), 310=Midtjylland (region), 312=Østjylland (landsdel), 314=Vestjylland (landsdel), 316=Nordjylland (region), 318=Standardoutput 0-100.000 Euro, 320=Standardoutput 100.000-499.999 Euro, 322=Standardoutput 500.000-999.999 Euro, 324=Standardoutput 1.000.000+ Euro]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [3505=Ejeraflønning, 1000 kr., 3510=Nettoudbytte, 1000 kr., 3515=Rentebelastning, 1000 kr., 3520=Lønningsevne, 1000 kr., 3525=Overskudsgrad, pct., 3530=Afkastningsgrad, pct., 3535=Forrentningsprocent, pct., 3540=Lønningsevne, kr. pr. time, 3541=Værditilvækst pr. fuldtidsekvivalent, 1000 kr., 3542=Soliditetsgrad, pct. (efter hensættelser), 3545=Soliditetsgrad, pct., 3550=Gældsprocent, pct.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- bedriftstand same combined dimension as jord1 (farm types 0–4, regions 300–316, size groups 318–324). Pick one group, never sum across all.
- regnskposter are computed ratios and efficiency measures — never sum or average them. Units vary: 1000 kr. for monetary items (3505–3520, 3541), pct. for ratios (3525–3550), kr. pr. time for 3540.
- Percentage items (soliditetsgrad, gældsprocent, overskudsgrad, etc.) are pre-computed averages. Do not weight-average them from this table — just report the given value for the selected bedriftstand/kvartil.
- Companion to jord1: jord1 has the full income statement for all farms; jord6 has the derived key ratios for the same population.