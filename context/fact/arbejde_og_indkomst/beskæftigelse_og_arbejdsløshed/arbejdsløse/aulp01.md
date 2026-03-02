table: fact.aulp01
description: Fuldtidsledige i pct. af arbejdsstyrken efter område, alder, køn og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is a percentage (pct. of workforce). Do not sum.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Finer alder bands than aup01/aup02 (30-34, 35-39, etc. vs 30-39). Stopped 2024-01; use aulkp01 for current data.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.