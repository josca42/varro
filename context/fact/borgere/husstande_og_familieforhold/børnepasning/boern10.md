table: fact.boern10
description: Fuldtidsomregnet børn oprykket til børnehave, før den 1. i måneden, efter de er fyldt tre år efter kommune og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 3]
- tid: date range 2023-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- kommunedk contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner), and niveau 3 (98 kommuner).
- Single-purpose table: counts children admitted to børnehave before their 3rd birthday month (early promotion). Only 2 dimensions (kommunedk, tid) — no filtering traps. indhold is the FTE count of such children.
- 2-year snapshot only (2023 and 2024). Very narrow use case — use for analysis of early-promotion policy compliance by municipality.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
