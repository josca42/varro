<fact tables>
<table>
id: oeko4
description: Udenrigshandel med økologiske varer efter im- og eksport, varer og tid
columns: indud, vare, tid (time), indhold (unit 1.000 kr.)
tid range: 2003-01-01 to 2023-01-01
</table>
<table>
id: oeko55
description: Udenrigshandel med økologiske varer efter im- og eksport, land og tid
columns: indud, land, tid (time), indhold (unit 1.000 kr.)
tid range: 2003-01-01 to 2023-01-01
</table>
<table>
id: oeko66
description: Udenrigshandel med økologiske varer efter im- og eksport, land, SITC-hovedgrupper og tid
columns: indud, nation, sitc, tid (time), indhold (unit 1.000 kr.)
tid range: 2003-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All three tables cover 2003–2023 (annual) with values in 1.000 kr. They differ in breakdown:
  - oeko4: product detail — 47 SITC-like commodity codes, no country breakdown.
  - oeko55: country detail — ~112 countries/continents, no product breakdown.
  - oeko66: country × product — ~21 nations × 16 SITC groups (niveau 2). Smaller country set than oeko55 (main trading partners only).
- For "which countries do we import most organic food from?": use oeko55 (broadest country coverage).
- For "what types of organic goods do we import?": use oeko4 (finest product granularity) or oeko66 (SITC main groups, also by country).
- For "organic trade with Germany by product category": use oeko66 (country + SITC group).
- All tables have indud with two values (415=Import, 430=Eksport) — always filter to one direction; never sum across both.
- land/nation columns in oeko55/oeko66 mix continent codes (niveau 1: 51-55) and country codes (niveau 4: ISO alpha-2). Filter by niveau when joining dim.lande_uhv. TOT = grand total in all three tables, not in the dimension — query with WHERE column = 'TOT' directly.