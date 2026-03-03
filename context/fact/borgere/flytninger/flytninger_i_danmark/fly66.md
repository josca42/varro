table: fact.fly66
description: Flytninger mellem kommuner efter tilflytningskommune, fraflytningskommune, alder, køn og tid
measure: indhold (unit Antal)
columns:
- tilkommune: join dim.nuts on tilkommune=kode; levels [3]
- frakommune: join dim.nuts on frakommune=kode; levels [3]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tilkommune and frakommune join dim.nuts at niveau 3 (99 kommuner). Perfect 99/99 match on both columns. Use `JOIN dim.nuts d ON f.tilkommune = d.kode AND d.niveau = 3`.
- No total rows: alder is individual ages only (goes up to 107+), kon is M/K only. No overcounting risk.
- Origin-destination matrix at municipality level: each row is moves from frakommune to tilkommune. To get "moves into Kommune X" filter `tilkommune = X`; for "moves from" filter `frakommune = X`. Do not sum both dimensions simultaneously.
- Covers only *inter-municipal* moves. For within-municipality moves see fly33; for all moves use fly.
- ColumnValues("nuts", "titel", for_table="fly66") works for both tilkommune and frakommune — same 99 kommuner.
- Map: /geo/kommuner.parquet — OD matrix; merge on tilkommune=dim_kode (moves into) or frakommune=dim_kode (moves out of) for choropleth. Exclude omrade=0.