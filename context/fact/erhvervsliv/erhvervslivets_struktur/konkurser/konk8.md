table: fact.konk8
description: Erklærede konkurser efter region, virksomhedstype og tid
measure: indhold (unit Antal)
columns:
- region: join dim.nuts on region=kode; levels [1]
- virktyp1: values [K01=Konkurser i alt, K02=Konkurser i aktive virksomheder, K03=Konkurser i nulvirksomheder]
- tid: date range 2009-01-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- region=0 is the national total (not in dim.nuts). Exclude it with WHERE f.region != '0' when joining to dim.nuts, or use it as the Denmark-total row without a join.
- Only niveau 1 (5 regioner: 81–85) is present — no landsdele or kommuner. Join: JOIN dim.nuts d ON f.region = d.kode WHERE d.niveau = 1 (or just ON f.region = d.kode since only niveau 1 codes are used).
- virktyp1 is a measurement selector: K01=total, K02=aktive virksomheder, K03=nulvirksomheder. K01 = K02 + K03. Always filter to one — confirmed: region=0, virktyp1=K01 in 2024 = 414, which equals the sum of the 5 regions.
- This is the only konkurser table with regional breakdown. Use ColumnValues("nuts", "titel", for_table="konk8") to see the 5 regions.
- Map: /geo/regioner.parquet — merge on region=dim_kode. Exclude region='0'.