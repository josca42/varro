table: fact.ifor11a
description: Personer i Lavindkomst familier efter indkomstniveau, socioøkonomisk status og tid
measure: indhold (unit Antal)
columns:
- indkn: values [50=50 procent af medianindkomsten, 60=60 procent af medianindkomsten]
- socio: join dim.socio on socio=kode; levels [3]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- indkn is a threshold selector (50% or 60% of median). Always filter to one: indkn = '60' is standard. Forgetting doubles all counts.
- socio joins dim.socio at niveau=3. However, codes 100 (total i alt, sum of all socio groups) and 130 (Lønmodtagere i alt, sum of 131-139) exist in the fact table but NOT in dim.socio. Exclude them when working at niveau=3: WHERE socio NOT IN (100, 130). Code 100 is the national total; code 130 is the Lønmodtagere subtotal.
- To work with all valid niveau=3 socio codes: JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3 (this automatically excludes codes 100 and 130).
- indhold is Antal (count of low-income persons per socio group). See ifor11p for the percentage version.
- Sample query (low-income persons by socio, 60% threshold, 2023): SELECT d.titel, f.indhold FROM fact.ifor11a f JOIN dim.socio d ON f.socio = d.kode WHERE f.indkn = '60' AND f.tid = '2023-01-01' AND d.niveau = 3 ORDER BY f.indhold DESC;
