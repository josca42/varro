table: fact.frkm125
description: Befolkningsfremskrivning 2025 efter kommune, alder, køn og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- alder: values [TOT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 96=96 år, 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2025-01-01 to 2050-01-01
dim docs: /dim/nuts.md

notes:
- kommunedk joins dim.nuts at niveau 3 only (99 kommuner). No aggregate geographic codes — each row is a single kommune.
- alder includes TOT. Filter alder='TOT' for overall totals. Individual ages go 0-100+.
- kon has M and K only, no total. SUM to get all-gender figures.
- Horizon is 2025-2050. For national-level herkomst breakdown, use frdk125 instead.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.