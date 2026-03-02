table: fact.pgoeko1
description: Økologisk landbrug  - Dækningsbidrag og jordrente efter produktionsgrene, regnskabsposter for afgrøder og tid
measure: indhold (unit -)
columns:
- prodgren1: values [1030=Korn i alt, 1031=Korn i alt, 1-50 hektar, 1050=Korn i alt, 50-100 hektar, 1055=Korn i alt, 100-250 hektar, 1060=Korn i alt, 250 hektar og derover ... 1135=Majs (grovfoder), 1140=Helsæd (grovfoder), 1145=Roer (grovfoder), 1150=Græs i omdrift (grovfoder), 1155=Vedvarende græs (grovfoder)]
- regnp: values [0=Population, antal bedrifter, 5=Stikprøve, antal bedrifter, 10=Areal, ha, 20=Høstudbytte, hkg/FE pr. ha, 25=Produktpris, kr. pr. hkg/FE ... 250=OMKOSTNINGER I ALT, 255=NETTOOVERSKLUD, 246=Jordomkostning, 265=Lønningsevne, 270=LØNNINGSEVNE, KR. PR. TIME]
- tid: date range 2021-01-01 to 2023-01-01
notes:
- Same structure as pgkonv1 (same regnp codes, same prodgren1 crop categories with size brackets). Same cautions apply: filter to specific regnp; don't sum totals and sub-categories.
- Covers økologisk landbrug afgrøder only. For organic livestock use pgoeko2. For conventional crops use pgkonv1.
- Only 3 years (2021–2023). Organic sample sizes are smaller than conventional — check regnp=5 (stikprøve antal bedrifter) before interpreting results.
