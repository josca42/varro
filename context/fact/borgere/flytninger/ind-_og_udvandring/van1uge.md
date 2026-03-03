table: fact.van1uge
description: Indvandringer efter område, køn, alder, indvandringsland, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- indvland: join dim.lande_psd on indvland=kode; levels [3]
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- tid: date range 2021U52 to 2025U39
dim docs: /dim/lande_psd.md, /dim/nuts.md

notes:
- tid is ISO week format: e.g. '2021U52'. This is not a date — filter with exact string matches or LIKE '2024U%' for a full year.
- Same omrade/indvland/statsb structure as van1kvt: omrade=0 is national total (not in dim.nuts), niveau 1 = 5 regioner, niveau 3 = 99 kommuner. Always add WHERE d.niveau = 1 or 3 when joining dim.nuts.
- indvland and statsb only use niveau 3 (~195/186 countries). ColumnValues("lande_psd", "titel", for_table="van1uge") for available countries.
- Covers 2021–present only. For longer series use van1kvt (quarterly from 2007) or van1aar (annual from 2007).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.