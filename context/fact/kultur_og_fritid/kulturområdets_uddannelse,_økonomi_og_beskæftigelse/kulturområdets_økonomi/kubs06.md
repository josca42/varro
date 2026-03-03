table: fact.kubs06
description: Kulturministeriet udbetalinger til personer efter bopælsområde, kulturemne, køn, aldersgrupper og tid
measure: indhold (unit 1.000 kr.)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler, 99=Uoplyst]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- aldgrp: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as kubs05 but measures disbursements (1.000 kr.) rather than person count (Antal). See kubs05 notes for join and filter guidance.
- `bopomr=0` is national aggregate (not in dim). Three hierarchy levels: niveau 1=regioner, 2=landsdele, 3=kommuner — filter d.niveau.
- Filter `kon=TOT`, `aldgrp=TOT`, and `kulturemne=0` for national totals.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.