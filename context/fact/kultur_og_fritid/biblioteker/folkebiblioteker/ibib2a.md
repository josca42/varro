table: fact.ibib2a
description: Udlån og lånere efter område, udlånssted, alder, kategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- udlanssted: values [9000=Samlet udlån, 9005=Folkebibliotekerne, 9010=eReolen]
- alder: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover, 9999=Uoplyst alder]
- dyrkat: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2020-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Archive version of ibib2 (age breakdown) — only to 2024. See ibib2.md for full notes.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
