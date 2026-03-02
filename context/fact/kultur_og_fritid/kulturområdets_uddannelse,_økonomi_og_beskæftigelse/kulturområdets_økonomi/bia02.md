table: fact.bia02
description: Udbetalinger af biblioteksafgiften efter bopælsområde, køn, alder og tid
measure: indhold (unit 1.000 kr.)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as bia01 but measures disbursements (1.000 kr.) rather than person count (Antal). See bia01 notes for join and filter guidance.
- `bopomr=0` is national aggregate (not in dim). Filter `d.niveau` for geographic granularity.
- `kon=TOT` and `alder=TOT` are aggregate totals — filter both for a simple total.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.