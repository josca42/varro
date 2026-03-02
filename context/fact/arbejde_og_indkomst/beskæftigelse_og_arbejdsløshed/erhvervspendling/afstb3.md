table: fact.afstb3
description: Beskæftigede (ultimo november) efter bopælsområde, socioøkonomisk status, køn, pendlingsafstand og tid
measure: indhold (unit Antal)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- socio: join dim.socio on socio=kode [approx]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- pendafst: values [0=I alt, 10=Ingen pendling, 20=Indtil 5 km, 30=5-10 km, 40=10-20 km, 45=20-30 km, 50=30-40 km, 60=40-50 km, 70=Over 50 km, 80=Ikke beregnet]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/socio.md

notes:
- Mirror of afsta3, but grouped by bopælsområde (where workers live) instead of arbejdsstedsområde (where they work). Same structural notes apply.
- bopomr contains all 3 nuts levels plus 0=Hele landet (national total). Join dim.nuts and filter to a single niveau. Code 0 is not in dim.nuts.
- socio uses the same CUSTOM encoding as afsta3 — do NOT join dim.socio. 5=Selvstændige, 10=Medarbejdende ægtefæller, 15–40=Lønmodtager subcategories. Use ColumnValues("afstb3", "socio").
- pendafst=0 is total (I alt); pendafst=80 is 'Ikke beregnet'. koen has TOT, M, K.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.