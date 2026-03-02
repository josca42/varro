table: fact.straf10
description: Anmeldte forbrydelser efter overtrædelsens art og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: Fact col is string, dim KODE is int64. Also has TOT placeholder.]; levels [1, 2, 3]
- tid: date range 1995-01-01 to 2025-07-01
dim docs: /dim/overtraedtype.md

notes:
- overtraed joins dim.overtraedtype via `f.overtraed = d.kode::text` (fact is string, dim kode is int). Use ColumnValues("overtraedtype", "titel") to browse the hierarchy.
- The table contains niveaux 1, 2, and 3 simultaneously — they are nested aggregates (niveau 1 sums niveau 2, which sums niveau 3). Always filter to a single niveau to avoid double-counting. Example: `JOIN dim.overtraedtype d ON ... WHERE d.niveau = 3` for finest granularity.
- overtraed='TOT' is the national grand total across all offense types — not in dim.overtraedtype. Exclude it when joining to the dim, or use it directly for an all-offenses total without joining.
- Only Straffelov (kode=1) and Særlov (kode=3) are present at niveau 1 — Færdselslov (kode=2) is not in this table.
- tid is annual (July observation dates, e.g. 2020-07-01), covering 1995–2025. This is the longest available series for crime counts without geographic breakdown.
- Simple query for total reported crimes per year: `SELECT tid, indhold FROM fact.straf10 WHERE overtraed = 'TOT' ORDER BY tid`