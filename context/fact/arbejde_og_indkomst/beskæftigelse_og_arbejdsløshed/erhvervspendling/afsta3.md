table: fact.afsta3
description: Beskæftigede (ultimo november) efter arbejdsstedsområde, socioøkonomisk status, køn, pendlingsafstand og tid
measure: indhold (unit Antal)
columns:
- arbejdssted: join dim.nuts on arbejdssted=kode [approx]; levels [1, 2, 3]
- socio: join dim.socio on socio=kode [approx]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- pendafst: values [0=I alt, 10=Ingen pendling, 20=Indtil 5 km, 30=5-10 km, 40=10-20 km, 45=20-30 km, 50=30-40 km, 60=40-50 km, 70=Over 50 km, 80=Ikke beregnet]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/socio.md

notes:
- arbejdssted contains all 3 nuts hierarchy levels (niveau 1=5 regioner, niveau 2=11 landsdele, niveau 3=99 kommuner). Always join dim.nuts and filter to a single niveau to avoid double-counting. Three special codes are NOT in dim.nuts: 0=Hele landet (national total), 950=Uden for Danmark, 998=Uoplyst kommune.
- socio uses a CUSTOM employment-type encoding that does NOT match dim.socio. Do NOT join dim.socio. Treat socio as inline coded: 5=Selvstændige, 10=Medarbejdende ægtefæller, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau, 25=Lønmodtagere på mellemniveau, 30=Lønmodtagere på grundniveau, 35=Andre lønmodtagere, 40=Lønmodtagere u.n.a. Use ColumnValues("afsta3", "socio") for the full list.
- pendafst=0 is the total (I alt). pendafst=80 means 'Ikke beregnet' (distance could not be calculated). Filter pendafst=0 for total counts or filter to specific distance bands (10–70) and exclude 80.
- koen has TOT, M, K — filter koen='TOT' for totals or koen IN ('M','K') for gender breakdown.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on arbejdssted=dim_kode. Exclude arbejdssted IN (0, 950, 998).