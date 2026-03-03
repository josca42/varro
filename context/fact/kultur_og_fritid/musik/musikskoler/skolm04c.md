table: fact.skolm04c
description: Ansatte på musikskolerne efter køn, alder, arbejdsstedsregion og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0049=49 år og derunder, 5099=50 år og derover]
- arbreg: join dim.nuts on arbreg=kode; levels [1]
- tid: date range 2021 to 2025
dim docs: /dim/nuts.md

notes:
- Counts individual employees (headcount) by work region, not FTE. Use skolm04a for FTE.
- arbreg joins dim.nuts at niveau 1 only (5 regioner). arbreg='0' is the national total, not in the dim.
- TOT rows present for kon and alder. Filter both to avoid overcounting.
- Map: /geo/regioner.parquet — merge on arbreg=dim_kode. Exclude arbreg=0.