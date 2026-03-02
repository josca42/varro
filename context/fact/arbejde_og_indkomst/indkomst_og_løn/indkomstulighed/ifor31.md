table: fact.ifor31
description: Gennemsnitlig ækvivalleret disponibel indkomst efter decil gennemsnit, socioøkonomisk status og tid
measure: indhold (unit Kr.)
columns:
- decilgen: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil]
- socio: join dim.socio on socio=kode; levels [3]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- socio joins dim.socio at niveau=3. Codes 100 (total i alt) and 130 (Lønmodtagere i alt) exist in the fact table but NOT in dim.socio. Use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3 to exclude these.
- decilgen has 10 codes (1DC–10DC, no aggregate). Every decil x socio combination is a separate row — do not sum across decils.
- indhold is average equivalised disposable income in Kr. (nominal). See ifor30 for the same table with prisenhed (faste/nominelle priser).
- Sample query (average income by decil for all socio groups, national 2023): SELECT f.decilgen, d.titel, f.indhold FROM fact.ifor31 f JOIN dim.socio d ON f.socio = d.kode WHERE f.tid = '2023-01-01' AND d.niveau = 3 ORDER BY f.decilgen, f.indhold DESC;
