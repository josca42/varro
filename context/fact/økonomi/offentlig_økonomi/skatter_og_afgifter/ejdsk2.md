table: fact.ejdsk2
description: Ejendomsskatter efter område, skattepromille og tid
measure: indhold (unit Skattepromille)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- skatpro: values [1=Grundskyldspromille, 2=Dækningsafgift af forretningsejendomme, 3=Dækningsafgift af offentlige ejendommes grundværdi, 4=Dækningsafgift af offentlige ejendommes forskelsværdi]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade has niveau 1 (5 regioner) and niveau 3 (98 kommuner) — both present. omrade='0' is national (not in dim.nuts). Use ColumnValues("nuts","titel",for_table="ejdsk2") to see available areas, then filter by d.niveau.
- skatpro values are rates (promille), not amounts. Each is a different tax rate concept — never sum across skatpro. Many kommuner have 0 for skatpro=2/3/4 (dækningsafgifter are optional).
- This table covers grundskyldspromille through 2025 (unlike pskat where GRUND ends 2023). Use this table for the most recent property tax rate data.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
