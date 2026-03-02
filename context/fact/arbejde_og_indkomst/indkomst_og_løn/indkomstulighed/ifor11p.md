table: fact.ifor11p
description: Lavindkomst familier efter indkomstniveau, socioøkonomisk status og tid
measure: indhold (unit Pct.)
columns:
- indkn: values [50=50 procent af medianindkomsten, 60=60 procent af medianindkomsten]
- socio: join dim.socio on socio=kode; levels [3]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- indkn is a threshold selector (50% or 60% of median). Always filter to one: indkn = '60' is standard. Forgetting doubles all counts.
- socio joins dim.socio at niveau=3. Codes 100 (total i alt) and 130 (Lønmodtagere i alt) are in the fact table but NOT in dim.socio. Exclude them with WHERE socio NOT IN (100, 130), or use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3.
- indhold is Pct. — share of that socio group living below the poverty line. See ifor11a for absolute counts.
- These are rates (share of a group in poverty), not counts — do not sum across socio groups.
