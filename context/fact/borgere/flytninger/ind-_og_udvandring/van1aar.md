table: fact.van1aar
description: Indvandringer efter område, køn, alder, indvandringsland, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- indvland: join dim.lande_psd on indvland=kode; levels [3]
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md, /dim/nuts.md

notes:
- omrade=0 is the national total (not in dim.nuts). When joining dim.nuts, always filter WHERE d.niveau = 1 (5 regioner) or d.niveau = 3 (99 kommuner) to avoid double-counting.
- indvland and statsb only use niveau 3 (~212 countries each). ColumnValues("lande_psd", "titel", for_table="van1aar") to see available countries.
- kon has no total (1=Mænd, 2=Kvinder only). alder is individual ages 0–103, no total — aggregate in SQL.
- This is the final (not preliminary) annual series from 2007. Preferred over van1kvt for annual questions.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.