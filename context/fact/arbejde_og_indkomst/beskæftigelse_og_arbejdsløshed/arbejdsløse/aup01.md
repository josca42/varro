table: fact.aup01
description: Fuldtidsledige i pct. af arbejdsstyrken (foreløbig opgørelse) efter område, alder, køn og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2017-07-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- indhold is a percentage (pct. of workforce). Do not sum across omrade or alder — these are rates, not counts.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Preliminary (foreløbig) counterpart to aup02, from Jul 2017. For longer history from 2007 use aup02. For rates by a-kasse (pct. of insured) use aup03 instead.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.