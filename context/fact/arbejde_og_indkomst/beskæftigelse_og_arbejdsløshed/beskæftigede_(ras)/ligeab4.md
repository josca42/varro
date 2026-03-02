table: fact.ligeab4
description: Beskæftigede (16-64 år) efter område, branche (DB07), forsikringskategori, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- branche07: join dim.db on branche07=kode::text
- fkategori: values [TOT=I alt, HF=Heltidsforsikrede, DF=Deltidsforsikrede, 980=Ikke forsikrede]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-17=16-17 år, 18-19=18-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md, /dim/nuts.md
notes:
- omrade joins dim.nuts at 99%. Code 0=Hele landet is an aggregate not in dim.nuts. Use ColumnValues("nuts", "titel", for_table="ligeab4") to see the available regions.
- branche07 uses DB07-37-group letter codes (A, B, CA...) — does NOT join dim.db. Use ColumnValues("ligeab4", "branche07") for labels.
- fkategori has TOT (I alt), HF=Heltidsforsikrede, DF=Deltidsforsikrede, 980=Ikke forsikrede. Filter to TOT for all together.
- alder has TOT and ranges from 16-17 to 60-64 (only age 16-64 covered per the table description).
- kon has TOT, M, K.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
