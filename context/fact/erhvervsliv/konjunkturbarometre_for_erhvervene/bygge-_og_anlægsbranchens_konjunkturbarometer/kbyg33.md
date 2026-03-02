table: fact.kbyg33
description: Produktionsbegrænsninger i bygge og anlæg efter branche (DB07), type og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [2]
- type: values [INGEN=Ingen begrænsninger, MEFT=Mangel på efterspørgsel, DVEJR=Dårligt vejr, MAT=Mangel på materialer og/eller udstyr, AMA=Mangel på arbejdskraft, FB=Finansielle begrænsninger , ANDÅS=Andre årsager]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db_10.md

notes:
- branche07 does NOT join dim.db_10 — same DST survey groupings as kbyg11. Use ColumnValues("kbyg33", "branche07") for labels. F = total sector.
- type values are NOT mutually exclusive — each represents the % of surveyed firms citing that limitation, and one firm can cite multiple. Never sum across type. Example Q4 2025 (branche07=F): INGEN=51, MEFT=23, AMA=22, FB=6, ANDÅS=8, DVEJR=3, MAT=1 — sums to 114%, confirming overlap.
- To compare limitations: SELECT type, indhold FROM fact.kbyg33 WHERE branche07='F' AND tid='...', giving one row per limitation with its own percentage.