table: fact.aulkp01
description: Fuldtidsledige i pct. af arbejdsstyrken efter område, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- Despite "unit Antal" in the measure line, indhold is a percentage (pct. af arbejdsstyrken) — the unit annotation is wrong. Values are ~2-5%.
- Do not sum across omrade or alder — these are rates.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Current monthly series superseding aulp01, with finer alder bands (30-34, 35-39, etc.).
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.