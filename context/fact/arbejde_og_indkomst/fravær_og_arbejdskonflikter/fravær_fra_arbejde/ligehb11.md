table: fact.ligehb11
description: Anmeldte arbejdsulykker efter branche, køn og tid
measure: indhold (unit Antal)
columns:
- branche: join dim.db on branche=kode::text [approx]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/db.md
notes:
- branche uses letter-based DB07 codes (A, B, CA, CB, ..., S, X, TOT) — these do NOT join dim.db (0% match). Use ColumnValues("ligehb11", "branche") for labels. 38 codes total.
- kon: TOT=I alt, M=Mænd, K=Kvinder (different coding than fra0XX tables which use 0/1/2).
- indhold = count of reported work accidents (Antal). Simple count table — no fravaer1 selector, no overcounting risk from measurement type.
- This table runs through 2024 (one year further than most fra0XX tables).
