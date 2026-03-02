table: fact.fstrib1
description: Filmstribens udlån og lånere efter kommune, køn, kategori og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 2, 3]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, 6=Uoplyst køn]
- misbrug2: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2024-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- Filmstriben is the Danish public library film streaming service (online video loans), completely separate from physical library loans.
- kommunedk joins dim.nuts at all 3 levels (5 regioner niveau 1, 11 landsdele niveau 2, 97 kommuner niveau 3) + kommunedk=0 = Hele landet.
- misbrug2 is the metric selector (equivalent to dyrkat in ibib tables): 9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen. Always filter to one.
- kon: TOT=I alt, M=Mænd, K=Kvinder, 6=Uoplyst. Filter to TOT to avoid overcounting.
- Only 2024 data (single year). fstrib1 (current, includes 2025 quarters) vs fstrib1a (archive, 2024 only).
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
