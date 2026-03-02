table: fact.nrhb
description: Befolkning efter område, socioøkonomisk status og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- socio: values [POP=Gennemsnitsbefolkning]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but code 0 (hele landet) is NOT in the dim table — it is the national total. Exclude omrade=0 when doing regional analysis.
- omrade uses levels 1 (5 regioner: 81–85) and 2 (11 landsdele: 1–11). Filter WHERE d.niveau=1 or d.niveau=2 to avoid double-counting.
- socio has only one value (POP=Gennemsnitsbefolkning), so no filter is needed on that column. This table is essentially regional average population by year.
- Simplest table in the subject — no measurement selector to worry about: SELECT d.titel, f.tid, f.indhold FROM fact.nrhb f JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=1.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.