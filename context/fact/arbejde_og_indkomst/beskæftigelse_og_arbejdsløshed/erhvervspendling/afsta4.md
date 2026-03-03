table: fact.afsta4
description: Gennemsnitlig pendlingsafstand (ultimo november) efter arbejdsstedsområde, socioøkonomisk status, køn og tid
measure: indhold (unit Km)
columns:
- arbejdssted: join dim.nuts on arbejdssted=kode; levels [1, 2, 3]
- socio: join dim.socio on socio=kode [approx]; levels [1]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/socio.md

notes:
- indhold is average commuting distance in km (not a count). Do not sum across rows — use AVG or just select directly for a given combination.
- socio uses a CUSTOM encoding that does NOT match dim.socio. Do NOT join dim.socio. Code 2='Beskæftigede i alt' (total employed) is the overall total. Subcategories: 5=Selvstændige, 10=Medarbejdende ægtefæller, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau, 25=Lønmodtagere på mellemniveau, 30=Lønmodtagere på grundniveau, 35=Andre lønmodtagere, 40=Lønmodtagere u.n.a. Use ColumnValues("afsta4", "socio").
- arbejdssted contains all 3 nuts levels plus 0=Hele landet (national). Join dim.nuts and filter to a single niveau. Code 0 is not in dim.nuts — filter it out or handle separately as the national figure.
- koen has TOT, M, K — filter koen='TOT' for overall average or use M/K to compare gender.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on arbejdssted=dim_kode. Exclude arbejdssted=0.