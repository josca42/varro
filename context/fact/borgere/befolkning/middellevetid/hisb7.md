table: fact.hisb7
description: Middellevetid for 0-årige efter køn og tid
measure: indhold (unit År)
columns:
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 1840 to 2025

notes:
- Simplest and longest life-expectancy series (1840–2025). Only two kon values (M, K) — no TOT row, so no overcounting risk. For national life expectancy at birth, this is the go-to table.
- To compare men vs. women over time: SELECT kon, tid, indhold FROM fact.hisb7 ORDER BY tid, kon.