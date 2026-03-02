table: fact.fabrit01
description: Familiernes adgang til pc og internet i hjemmet efter type, adgang og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 110=Fam. type: Enlig, 120=Fam. type: Par uden børn, 130=Fam. type: Enlig med børn, 140=Fam. type: Par med børn, 310=Region: Hovedstaden, 320=Region: Midtjylland, 330=Region: Nordjylland, 340=Region: Sjælland, 350=Region: Syddanmark, 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover, 400=Antal børn i hjemmet: 0 stk, 410=Antal børn i hjemmet: 1 stk, 420=Antal børn i hjemmet: 2 stk, 430=Antal børn i hjemmet: 3+ stk]
- adgang: values [10=Adgang til en computer i hjemmet, 30=Adgang til internet i hjemmet]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- type is a demographic selector: type='10' = I alt. Other values are household type (enlig/par, med/uden børn), region (5 regioner), income, and number of children. Never sum across type values — always filter to one segment or use '10'.
- adgang has only 2 values — PC access (10) and internet access (30). These are two independent questions, not parts of a whole. A household can have both or neither. Do not sum.
- For regional breakdown, use type IN ('310','320','330','340','350') (5 regioner) — these are not part of the normal demographic hierarchy, just coded within type.
