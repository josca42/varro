table: fact.ifor32
description: Gennemsnitlig ækvivalret disponibel indkomst efter decil gennemsnit, kommune og tid
measure: indhold (unit Gns.)
columns:
- decilgen: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil]
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- tid: date range 1987-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- kommunedk code 0 = Danmark i alt (national aggregate), not in dim.nuts. Use WHERE kommunedk = 0 for national totals or WHERE kommunedk != 0 to get all 98 kommuner. All other codes join dim.nuts at niveau=3 (kommuner only — no regioner/landsdele in this table).
- decilgen has no aggregate/total code — all 10 decils are independent. To get a full distribution, select all 10DC values.
- Sample query (average income by decil, national): SELECT decilgen, indhold FROM fact.ifor32 WHERE kommunedk = 0 AND tid = '2023-01-01' ORDER BY decilgen;
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
