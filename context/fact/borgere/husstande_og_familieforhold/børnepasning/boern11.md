table: fact.boern11
description: Fuldtidsomregnet pædagogisk personale ansat for statslige puljemidler efter kommune, stillingskategori og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 3]
- overens: values [7=Pædagog, 92=Pædagogmedhjælper, 93=Pædagogisk assistent]
- tid: date range 2023-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- kommunedk contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner), and niveau 3 (98 kommuner).
- overens has only 3 specific job categories (Pædagog, Pædagogmedhjælper, Pædagogisk assistent) — NO total row. To get total staff funded by state pool money, sum all 3 overens values.
- 2-year snapshot only (2023 and 2024). Very narrow table: only staff funded by statslige puljemidler (state pool funds), not general pedagogical staff. For general staff use boern1.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
