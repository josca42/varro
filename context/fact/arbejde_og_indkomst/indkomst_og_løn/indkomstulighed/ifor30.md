table: fact.ifor30
description: Gennemsnitlig ækvivalleret disponibel indkomst efter decil gennemsnit, socioøkonomisk status, prisenhed og tid
measure: indhold (unit Kr.)
columns:
- decilgen: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil]
- socio: join dim.socio on socio=kode; levels [3]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- prisenhed is a measurement selector: every row exists twice — faste priser (real, code 5) and nominelle priser (nominal, code 6). Always filter to one. Use prisenhed = '5' for time series comparisons.
- socio joins dim.socio at niveau=3. Codes 100 (total i alt) and 130 (Lønmodtagere i alt) exist in the fact table but NOT in dim.socio. Use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3 to exclude these.
- Three columns to filter to avoid overcounting: choose one decilgen, one socio (or join dim.socio), one prisenhed.
- See ifor31 for the same table without prisenhed (nominal only).
