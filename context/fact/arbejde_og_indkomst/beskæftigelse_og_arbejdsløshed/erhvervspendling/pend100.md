table: fact.pend100
description: Beskæftigede (ultimo november) efter bopælskommune, arbejdsstedsområde, køn og tid
measure: indhold (unit Antal)
columns:
- bopkom: join dim.nuts on bopkom=kode; levels [1, 2, 3]
- arbejdssted: join dim.nuts on arbejdssted=kode; levels [1, 2, 3]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- This is a full origin-destination (OD) commuting matrix. Both bopkom (residence) and arbejdssted (workplace) contain all 3 hierarchy levels: niveau 1 = 5 regioner, niveau 2 = 11 landsdele, niveau 3 = 99 kommuner. The table has 9 combinations of bopkom-niveau × arbejdssted-niveau — do NOT sum across all rows without filtering to a consistent pair of niveaux or you will massively double-count.
- To query at a single granularity (e.g. kommune-to-kommune flows): JOIN both sides to dim.nuts and filter WHERE b.niveau = 3 AND a.niveau = 3.
- arbejdssted=950 means 'Uden for Danmark' (abroad) — not in dim.nuts. Appears as a workplace for residents commuting internationally.
- kon has only M and K (no TOT). Sum both to get total.
- Use ColumnValues("nuts", "titel", for_table="pend100") to see all 116 area codes (including 950) available on the arbejdssted side.
- Map: bopkom and arbejdssted both support choropleths — context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopkom=dim_kode or arbejdssted=dim_kode after filtering to a single niveau. Exclude codes 0 and 950.