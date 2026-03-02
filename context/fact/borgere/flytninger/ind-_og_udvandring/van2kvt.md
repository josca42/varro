table: fact.van2kvt
description: Udvandringer (foreløbig opgørelse) efter område, køn, alder, udvandringsland, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- udvland: join dim.lande_psd on udvland=kode; levels [3]
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- tid: date range 2007-04-01 to 2025-04-01
dim docs: /dim/lande_psd.md, /dim/nuts.md

notes:
- Emigration mirror of van1kvt. Same omrade structure: omrade=0 is national total (not in dim.nuts), niveau 1 = 5 regioner, niveau 3 = 99 kommuner. Always filter WHERE d.niveau = 1 or 3 when joining dim.nuts.
- udvland and statsb only use niveau 3 (~211/202 countries). ColumnValues("lande_psd", "titel", for_table="van2kvt") for available countries.
- kon has no total (1=Mænd, 2=Kvinder). alder is individual ages, no total — aggregate in SQL.
- Preliminary data (foreløbig). For final annual emigration figures use van2aar.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.