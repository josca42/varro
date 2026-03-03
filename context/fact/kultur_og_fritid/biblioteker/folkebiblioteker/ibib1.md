table: fact.ibib1
description: Udlån og lånere efter område, udlånssted, køn, kategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- udlanssted: values [9000=Samlet udlån, 9005=Folkebibliotekerne, 9010=eReolen]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, 6=Uoplyst køn]
- dyrkat: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2020-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all 3 levels: niveau 1 (5 regioner), niveau 2 (11 landsdele), niveau 3 (97 kommuner). omrade=0 = Hele landet. Use ColumnValues("nuts", "titel", for_table="ibib1") to browse all areas.
- dyrkat is the key metric selector: 9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen. Always filter to one. Note: 9025 (persons in population) is available for omrade=0 only with udlanssted=9000, not for all combinations.
- udlanssted must be filtered: 9000=Samlet udlån (total), 9005=Folkebibliotekerne only, 9010=eReolen only. For totals, use 9000.
- kon: TOT=I alt, M=Mænd, K=Kvinder, 6=Uoplyst. Filter to TOT to avoid summing over gender.
- ibib1 (current, to 2025) vs ibib1a (archive, to 2024): use ibib1 for current analysis.
- Combining dyrkat=9020 (lånere) with 9025 (population) lets you calculate library borrower penetration rate.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
