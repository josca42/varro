table: fact.ifor21
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, socioøkonomisk status og tid
measure: indhold (unit Kr.)
columns:
- decilgr: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil]
- socio: join dim.socio on socio=kode; levels [3]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- socio joins dim.socio at niveau=3. Codes 100 (total i alt) and 130 (Lønmodtagere i alt) exist in the fact table but NOT in dim.socio. Use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3 to exclude these.
- decilgr has 9 codes (1DC–9DC): upper income boundaries between consecutive decils. 9DC = 90th percentile threshold for that socio group.
- indhold is Kr. (nominal). See ifor20 for the same table with prisenhed (inflation-adjusted option).
- No municipality breakdown — socio dimension replaces regional breakdown seen in ifor22/ifor25.
