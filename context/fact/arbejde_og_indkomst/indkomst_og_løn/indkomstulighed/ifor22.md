table: fact.ifor22
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, kommune og tid
measure: indhold (unit Kr.)
columns:
- decilgr: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil]
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- tid: date range 1987-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- decilgr has 9 codes (1DC–9DC): these are the upper boundary of each decil (the income level that separates decil N from N+1). No code for the 10th decil boundary (it is unbounded above). Not averages within a decil — these are thresholds.
- kommunedk code 0 = Danmark i alt (not in dim.nuts). All other codes join dim.nuts at niveau=3 (kommuner).
- indhold is Kr. (income boundary, nominal). See ifor25 for the same table with prisenhed (inflation-adjusted option).
- Use this table to find "what income level puts you in the top 10%?" — filter to decilgr = '9DC' for the 90th percentile threshold.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
