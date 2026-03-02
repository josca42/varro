table: fact.pris113
description: Forbrugerprisindeks, hovedtal efter type og tid
measure: indhold (unit Indeks)
columns:
- type: values [INDEKS=Forbrugerprisindeks]
- tid: date range 1980-01-01 to 2025-09-01

notes:
- Single-series table: type=INDEKS is the only value, no filtering needed beyond tid.
- Monthly CPI index from 1980 — the go-to table for recent and current CPI trends.
- No dimension joins, no measurement-selector pitfalls. Just SELECT indhold, tid FROM fact.pris113.
- For breakdown by ECOICOP category use pris111; for annual-only data back to 1900 use pris8; for annual % change use pris9 or pris112.