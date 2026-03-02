table: fact.pskat
description: Personbeskatningen efter område, beskatningsprocent og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- skatpct: values [KOM=Kommunal udskrivningsprocent, KIRKE=Kirkeskatteprocent, GRUND=Grundskyldspromille]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. niveau 1 = 5 regioner, niveau 3 = 98 kommuner — both present in the same table. omrade='0' is a national weighted average (not in dim.nuts, 55 rows). Use ColumnValues("nuts","titel",for_table="pskat") to see available areas.
- skatpct has 3 completely different rate types: KOM=kommunal udskrivningsprocent (~25%), KIRKE=kirkeskatteprocent (~0.87%), GRUND=grundskyldspromille (~26‰). Not additive. Always filter to exactly one skatpct per query.
- indhold is a rate, not an amount. Do not sum across omrade — compute weighted averages if needed.
- GRUND (grundskyldspromille) is only available up to 2023; KOM and KIRKE continue to 2025. For 2024–2025 grundskyld rate data, use ejdsk2 instead.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
