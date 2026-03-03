table: fact.kubs05
description: Personlige modtagere af Kulturministeriets udbetalinger efter bopælsområde, kulturemne, køn, aldersgrupper og tid
measure: indhold (unit Antal)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler, 99=Uoplyst]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- aldgrp: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `bopomr` joins dim.nuts. bopomr=0 is national aggregate (not in dim). Three hierarchy levels present: niveau 1=regioner (81–85), niveau 2=landsdele (1–11), niveau 3=kommuner (101+). Filter `d.niveau` to pick one geographic level.
- `kon=TOT`, `aldgrp=TOT`, `kulturemne=0` are aggregate totals. Filter all three to their totals for a national headcount, or pick specific values for breakdowns.
- Parallel to kubs06 which counts money (1.000 kr.) rather than persons (Antal).
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.