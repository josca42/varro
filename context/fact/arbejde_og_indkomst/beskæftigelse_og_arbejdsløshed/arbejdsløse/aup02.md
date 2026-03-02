table: fact.aup02
description: Fuldtidsledige i pct. af arbejdsstyrken efter område, alder, køn og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-03-01
dim docs: /dim/nuts.md

notes:
- indhold is a percentage (pct. of workforce). Do not sum across omrade or alder.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- From 2007, slightly behind aup01 in recency. Same structure as aup01. No akasse — for a-kasse-specific rates use aup03.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.