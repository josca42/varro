table: fact.aku230k
description: Beskæftigede efter område, alder, køn og tid
measure: indhold (unit 1.000 personer)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- alder: values [TOT=Alder i alt, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts cleanly (all 5 regioner match, no unmatched aggregate code). Use ColumnValues("nuts", "titel", for_table="aku230k") to see available regions.
- alder (TOT + 5 age bands 15-24 through 55-64) and kon (TOT + M + K) both have totals — filter to alder='TOT', kon='TOT' for a simple employed-by-region series.
- Note: alder only goes to 5564 (not 6574 like aku110k/aku230k) — this table restricts to 15-64 age range.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode.