table: fact.fstrib1a
description: Filmstribens udlån og lånere efter kommune, køn, kategori og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 2, 3]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, 6=Uoplyst køn]
- misbrug2: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Archive version of fstrib1 (Filmstriben, gender breakdown) — only 2024. See fstrib1.md for full notes.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
