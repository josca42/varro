table: fact.fstrib2
description: Filmstribens udlån og lånere efter kommune, alder, kategori og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover, 9999=Uoplyst alder]
- misbrug2: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2024-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- Filmstriben loans/borrowers by age. Same structure as fstrib1 but with alder instead of kon.
- alder: TOT=Alder i alt, 10-year bands (0-9 through 70+), 9999=Uoplyst. Filter to TOT to avoid double-counting.
- kommunedk at all 3 nuts levels + kommunedk=0. misbrug2 must be filtered to one metric.
- fstrib2 (to 2025) vs fstrib2a (archive, 2024 only).
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
