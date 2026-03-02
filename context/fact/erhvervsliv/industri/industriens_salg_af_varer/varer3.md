table: fact.varer3
description: Industriens salg af egne varer, SITC (år) efter SITC-hovedgrupper og tid
measure: indhold (unit 1.000 kr.)
columns:
- sitc: join dim.sitc on sitc=kode [approx]; levels [2]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/sitc.md

notes:
- Annual counterpart to varer2s. No saeson column — no measurement selector to worry about.
- sitc joins dim.sitc at niveau 2 (63 codes). TOT and TOT0–TOT8 are aggregate codes not in dim.sitc — filter with WHERE sitc NOT LIKE 'TOT%' before joining. Use ColumnValues("varer3", "sitc") for labels.
- All values in 1.000 kr.