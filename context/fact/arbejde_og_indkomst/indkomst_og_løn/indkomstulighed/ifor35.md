table: fact.ifor35
description: Gennemsnitlig ækvivalret disponibel indkomst efter decil gennemsnit, kommune, prisenhed og tid
measure: indhold (unit Gns.)
columns:
- decilgen: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil]
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- tid: date range 1987-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- prisenhed is a measurement selector: every row exists twice — faste priser (real, inflation-adjusted, code 5) and nominelle priser (nominal, code 6). Always filter to one: prisenhed = '5' for real prices or prisenhed = '6' for nominal. Forgetting this doubles all sums.
- kommunedk code 0 = Danmark i alt (not in dim.nuts). All other codes join dim.nuts at niveau=3 (kommuner). See ifor32 for the version without prisenhed.
- Use ifor35 (over ifor32) when comparing trends across time — faste priser removes inflation effects.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
