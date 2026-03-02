table: fact.ifor25
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, kommune, prisenhed og tid
measure: indhold (unit Kr.)
columns:
- decilgr: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil]
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- tid: date range 1987-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- prisenhed is a measurement selector: every row exists twice — faste priser (real, code 5) and nominelle priser (nominal, code 6). Always filter to one. Forgetting this doubles all values.
- decilgr has 9 codes (1DC–9DC): upper income boundaries between consecutive decils, not averages. 9DC = the 90th percentile income threshold.
- kommunedk code 0 = Danmark i alt (not in dim.nuts). All other codes join dim.nuts at niveau=3 (kommuner).
- See ifor22 for the same table without prisenhed. Use ifor25 with prisenhed = '5' for real price comparisons over time.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
