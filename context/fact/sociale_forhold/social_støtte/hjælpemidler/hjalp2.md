table: fact.hjalp2
description: Modtagere af udlån af hjælpemidler efter kommune, køn, alder og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- konams: values [0=I alt, 1=Mænd, 2=Kvinder]
- alerams: values [TOT=Alder i alt, 0024=Under 25 år, 2549=25-49 år, 5059=50-59 år, 6064=60-64 år, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år, 8589=85-89 år, 90-=90 år og derover]
- tid: date range 2023-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- kommunedk joins dim.nuts at niveau 3 (kommuner). Use ColumnValues("nuts", "titel", for_table="hjalp2") to see the 97 kommuner available.
- kommunedk='0' is a national aggregate (hele landet) not in dim.nuts. National total: ~380K recipients in 2023. Exclude with WHERE kommunedk != '0' when joining dim.nuts.
- konams and alerams both include totals (konams=0 "I alt", alerams='TOT' "Alder i alt"). Filter both to avoid overcounting when aggregating across dimensions. Example: konams != 0 AND alerams != 'TOT'.
- indhold counts recipients (modtagere), not loans. For loan counts use hjalp1.
- Only 2 time points: 2023 and 2024.
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk='0'.