table: fact.afstb4
description: Gennemsnitlig pendlingsafstand (ultimo november) efter bopælsområde, socioøkonomisk status, køn og tid
measure: indhold (unit Km)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- socio: join dim.socio on socio=kode [approx]; levels [1]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/socio.md

notes:
- Mirror of afsta4, but grouped by bopælsområde (residence) instead of arbejdsstedsområde (workplace). Same structural notes apply.
- indhold is average commuting distance in km. Do not sum rows.
- socio uses the same CUSTOM encoding as afsta4 — do NOT join dim.socio. Code 2='Beskæftigede i alt' (total), 5–40 are subcategories. Use ColumnValues("afstb4", "socio").
- bopomr contains all 3 nuts levels plus 0=Hele landet. Filter to one niveau when joining dim.nuts. Code 0 is not in dim.nuts.
- kon has TOT, M, K.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.