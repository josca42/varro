table: fact.ifor20
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, socioøkonomisk status, prisenhed og tid
measure: indhold (unit Kr.)
columns:
- decilgr: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil]
- socio: join dim.socio on socio=kode; levels [3]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- prisenhed is a measurement selector: every row exists twice — faste priser (real, code 5) and nominelle priser (nominal, code 6). Always filter to one. Forgetting this doubles all values.
- socio joins dim.socio at niveau=3. Codes 100 (total i alt) and 130 (Lønmodtagere i alt) exist in the fact table but NOT in dim.socio. Use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3.
- decilgr has 9 codes (1DC–9DC): upper income boundaries between decils (not averages within decils).
- See ifor21 for the same table without prisenhed.
