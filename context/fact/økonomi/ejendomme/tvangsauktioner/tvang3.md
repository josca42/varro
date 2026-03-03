table: fact.tvang3
description: Bekendtgjorte tvangsauktioner efter område og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. All three levels are present: niveau=1 (5 regioner), niveau=2 (11 landsdele), niveau=3 (99 kommuner). Always filter WHERE d.niveau = N to avoid double-counting across hierarchy levels.
- omrade = '0' is "Hele landet" (national total) — not in dim.nuts, handle separately if needed. Only 13 rows (one per year).
- Annual data, 2012–2024 only. No property-type breakdown — use tvang1/tvang2 for that.
- Use ColumnValues("nuts", "titel", for_table="tvang3") to see the 115 area codes present in this table.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.