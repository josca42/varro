table: fact.frld125
description: Befolkningsfremskrivning 2025 efter region/landsdel, alder, køn og tid
measure: indhold (unit Antal)
columns:
- regland: join dim.nuts on regland=kode; levels [1, 2]
- alder: values [TOT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 96=96 år, 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2025-01-01 to 2050-01-01
dim docs: /dim/nuts.md

notes:
- regland joins dim.nuts OK (16/16). The column mixes niveau 1 (5 regioner, kode 81-85) and niveau 2 (11 landsdele, kode 1-11). JOIN with WHERE d.niveau=1 for regions or WHERE d.niveau=2 for landsdele — mixing both will double-count.
- alder includes TOT. Filter alder='TOT' for overall totals, or individual ages (0-100+). No intermediate age groups — aggregate with CASE in SQL if needed.
- kon has M and K only, no total. SUM to get all-gender figures.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on regland=dim_kode. Exclude regland=0.