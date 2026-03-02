table: fact.fstrib2a
description: Filmstribens udlån og lånere efter kommune, alder, kategori og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover, 9999=Uoplyst alder]
- misbrug2: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Archive version of fstrib2 (Filmstriben, age breakdown) — only 2024. See fstrib2.md for full notes.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
