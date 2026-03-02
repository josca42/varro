table: fact.skolm02b
description: Elever på musikskoler efter kommune, alder, køn og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- alder: values [TOT=Alder i alt, 0003=0-3 år, 0406=4-6 år, 0709=7-9 år, 1014=10-14 år, 1519=15-19 år, 2024=20-24 år, 2500=25 år og derover, UOPLYST=Uoplyst alder]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- tid: date range 2021 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- komk joins dim.kommunegrupper at niveau 2 (98 kommuner). komk='0' is the national total, not in the dim.
- Counts unique students (elever), unlike skolm02a which counts aktiviteter (subject enrollments). Use this for headcounts of individual students.
- TOT rows present for alder and kon. Filter both to avoid overcounting: e.g. alder='TOT', kon='TOT' for total students.
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.