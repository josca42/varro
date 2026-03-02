table: fact.rst01
description: Råstofindvinding (1000 m3) efter område, råstoftype og tid
measure: indhold (unit 1.000 m3)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- rastoftype: values [TOTLAND=SAMLET INDVINDING PÅ LAND, SANDGRUS=Sand, grus og sten, KVARTS=Kvartssand, GRANIT=Granit, LER=Ler, EKSPLER=Ekspanderende ler , MOLER=Moler, KRIDT=Kridt/kalk, TØRV=Tørv, ANDRE=Andre råstoffer]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but contains codes at TWO hierarchy levels: niveau 1 (5 regioner, kode 81-85) and niveau 3 (98 kommuner, kode 101-860). Both are present for all years. Querying without a niveau filter double-counts everything — region totals equal the sum of their child kommuner. Filter to one: `WHERE d.niveau = 3` for kommune detail or `WHERE d.niveau = 1` for regional summary.
- omrade code '0' = national total (DK samlet). Not in dim.nuts. Useful as a quick total but exclude from aggregations across areas.
- Use `ColumnValues("nuts", "titel", for_table="rst01")` to see the 103 dim-matched omrade codes.
- rastoftype TOTLAND = sum across all material types. Filter `WHERE rastoftype != 'TOTLAND'` when summing across types to avoid double-counting. The 9 individual types are: SANDGRUS, KVARTS, GRANIT, LER, EKSPLER, MOLER, KRIDT, TØRV, ANDRE.
- indhold unit is 1.000 m³ (thousands of cubic metres).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.