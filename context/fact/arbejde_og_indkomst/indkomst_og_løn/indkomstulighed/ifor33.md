table: fact.ifor33
description: Indkomstdecilers sammensætning efter indkomstdecil, socioøkonomisk status, enhed og tid
measure: indhold (unit -)
columns:
- inddecil: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil]
- socio: join dim.socio on socio=kode; levels [3]
- enhed: values [PCT=Andel af decil (pct.), ANT=Personer (antal)]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- enhed is a measurement selector: PCT=andel af decil (pct.) and ANT=antal personer. Both units exist for every row combination. Always filter to one: WHERE enhed = 'PCT' or WHERE enhed = 'ANT'. Forgetting this doubles all values.
- socio joins dim.socio at niveau=3. Codes 100 (total i alt) and 130 (Lønmodtagere i alt) exist in the fact table but NOT in dim.socio. Use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3 to get only the 15 matchable niveau=3 codes.
- PCT values show the share of persons in a given decil that belong to each socio group. They sum to 100 across all socio groups within a decil (when including aggregate code 100). Do not sum PCT across decils.
- inddecil has 10 codes (1DC–10DC), no total. To see socio composition of the richest decil: WHERE inddecil = '10DC' AND enhed = 'PCT'.
- Sample query (socio composition of top decil, 2023): SELECT d.titel, f.indhold FROM fact.ifor33 f JOIN dim.socio d ON f.socio = d.kode WHERE f.inddecil = '10DC' AND f.enhed = 'PCT' AND f.tid = '2023-01-01' AND d.niveau = 3 ORDER BY f.indhold DESC;
