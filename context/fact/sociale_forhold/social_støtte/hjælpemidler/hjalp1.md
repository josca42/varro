table: fact.hjalp1
description: Udlån af hjælpemidler efter kommune og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- tid: date range 2023-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- kommunedk joins dim.nuts at niveau 3 (kommuner). Use ColumnValues("nuts", "titel", for_table="hjalp1") to see the 97 kommuner available.
- kommunedk='0' is a national aggregate (hele landet) not present in dim.nuts. It holds the Denmark total (2.17M loans in 2023). Exclude it with WHERE kommunedk != '0' when joining to dim.nuts, or use it directly as the national total without a join.
- indhold counts loans (udlån), not recipients — a single person can have multiple loans. For recipient counts, use hjalp2 instead.
- Only 2 time points: 2023 and 2024.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk='0'.