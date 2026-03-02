table: fact.pris8
description: Forbrugerprisindeks, årsgennemsnit efter type og tid
measure: indhold (unit Indeks)
columns:
- type: values [INDEKS=Forbrugerprisindeks]
- tid: date range 1900-01-01 to 2024-01-01

notes:
- Single-series table: type=INDEKS is the only value, no filtering needed beyond tid.
- Annual average CPI index going back to 1900 — use this for long historical analysis. Base year is 1900=100.
- No dimension joins, no measurement-selector pitfalls. Just SELECT indhold, tid FROM fact.pris8.
- For % change series use pris9; for monthly data from 1980 use pris113.