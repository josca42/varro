table: fact.van1kvt
description: Indvandringer (foreløbig opgørelse) efter område, køn, alder, indvandringsland, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- indvland: join dim.lande_psd on indvland=kode; levels [3]
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- tid: date range 2007-04-01 to 2025-04-01
dim docs: /dim/lande_psd.md, /dim/nuts.md

notes:
- omrade=0 is the national total (Danmark) — not in dim.nuts. Use it directly or filter omrade != '0' for regional breakdown. When joining dim.nuts, filter WHERE d.niveau = 1 for 5 regioner or d.niveau = 3 for 99 kommuner. Never join without a niveau filter — both levels are present and summing them double-counts.
- indvland and statsb only use niveau 3 (individual countries, ~212 each). Use ColumnValues("lande_psd", "titel", for_table="van1kvt") to see which countries appear.
- kon has no total row (only 1=Mænd, 2=Kvinder). alder has individual ages 0–103, no total row — aggregate in SQL if needed.
- This table is preliminary (foreløbig). For final annual figures use van1aar; for quarterly finals prefer van1aar grouped by year.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.