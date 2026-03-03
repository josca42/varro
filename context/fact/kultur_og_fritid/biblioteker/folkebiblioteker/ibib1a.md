table: fact.ibib1a
description: Udlån og lånere efter område, udlånssted, køn, kategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- udlanssted: values [9000=Samlet udlån, 9005=Folkebibliotekerne, 9010=eReolen]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, 6=Uoplyst køn]
- dyrkat: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2020-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Archive version of ibib1 — same structure but only up to 2024. Use ibib1 for current analysis; this table is retained for stability in dashboards referencing a fixed year range.
- See ibib1.md for full notes on omrade, udlanssted, dyrkat, and kon filters.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
