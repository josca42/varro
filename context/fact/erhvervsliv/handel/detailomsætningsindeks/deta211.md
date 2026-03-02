table: fact.deta211
description: Detailomsætningsindeks efter branche (DB07) og tid
measure: indhold (unit Indeks)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- tid: date range 2000-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- branche07 joins dim.db at niveau=5 for 29 of 44 codes. Use `JOIN dim.db d ON f.branche07 = d.kode::text WHERE d.niveau = 5` to get standard branch labels. ColumnValues("db", "titel", for_table="deta211") shows the 29 matchable codes.
- 15 codes don't match dim.db: `4700` is a DST aggregate for total retail (Detailhandel i alt — equivalent to sector 47). The 11 `S`-suffix codes (e.g. `472900S`, `474300S`) are DST-specific custom groupings not in the standard DB07 hierarchy. Three further codes (`472410`, `477615`, `479110`) are fine-grained sub-classes not in dim.db. All 15 appear for every time period.
- To get a clean branche breakdown without custom codes, filter to codes that join dim.db: `JOIN dim.db d ON f.branche07 = d.kode::text AND d.niveau = 5`. This covers 29 branches (standard niveau-5 detail retail codes under sector 47).
- To include the overall total, use `branche07 = '4700'` directly — it does not join to dim.db but represents all retail combined.
- Indices are monthly. The table has only one dimension (branche07) plus tid, so no overcounting risk from other dimensions.