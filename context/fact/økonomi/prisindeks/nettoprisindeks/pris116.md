table: fact.pris116
description: Nettoprisindeks, hovedtal efter type og tid
measure: indhold (unit Indeks)
columns:
- type: values [NINDEKS=Nettoprisindeks]
- tid: date range 1980-01-01 to 2025-09-01

notes:
- type has only one value (NINDEKS). No filtering needed, but include WHERE type='NINDEKS' for clarity.
- This is the simplest monthly NPI series: one row per month, headline aggregate only, from 1980M01 to 2025M09. Best choice for trend charts and long-run comparisons.
- No product breakdown. For category-level monthly NPI, use pris114 (from 2001). For annual figures, use pris115.