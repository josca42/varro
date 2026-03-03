table: fact.enegeo
description: Industriens energiforbrug efter kommune og tid
measure: indhold (unit 1.000 GJ (gigajoule))
columns:
- komk: join dim.nuts on komk=kode; levels [1, 3]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts. Use ColumnValues("nuts", "titel", for_table="enegeo") to see available codes. niveau 1 = 5 regioner, niveau 3 = 99 kommuner. Filter WHERE d.niveau = 1 or d.niveau = 3 to pick your granularity — both levels are present, so a plain join without niveau filter will produce duplicate rows.
- komk='0' is a national total (hele Danmark) — it is NOT in dim.nuts. Use WHERE f.komk != '0' when joining to the dim table, or use it directly as f.komk = '0' to get the national figure without a join.
- No enhed selector: indhold is always in 1.000 GJ. Data covers 2012-2024 biennially.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on komk=dim_kode. Exclude komk='0'.