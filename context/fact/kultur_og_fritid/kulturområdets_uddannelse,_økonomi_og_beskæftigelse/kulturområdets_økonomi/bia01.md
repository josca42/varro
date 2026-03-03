table: fact.bia01
description: Personlige modtagere af biblioteksafgiften efter bopælsområde, køn, alder og tid
measure: indhold (unit Antal)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `bopomr=0` is national aggregate (not in dim). Three hierarchy levels in dim.nuts: niveau 1=regioner, 2=landsdele, 3=kommuner. Filter d.niveau to pick one level.
- `kon=TOT` and `alder=TOT` are aggregate totals. Filter both to totals for a simple national count of biblioteksafgift recipients.
- Parallel to bia02 which measures disbursement amounts (1.000 kr.) rather than person count.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.