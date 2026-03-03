table: fact.ligeki1
description: Ligestillingsindikator for personlige modtagere af Kulturministeriets udbetalinger efter indikator, bopælsområde, kulturemne, aldersgrupper og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 12=KULTURARV, 1=MEDIER, BIBLIOTEKER OG LITTERATUR, 20=SCENE OG MUSIK, 23=VISUEL KUNST OG DESIGN, 29=ANDEN KULTUREL AKTIVITET]
- aldgrp: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `indikator` is CRITICAL: LA1=Mænd %, LA2=Kvinder %, LA3=Forskel (procentpoint). These are rates, not counts. NEVER sum across indicators — filter to exactly one per query.
- LA1 + LA2 always = 100; LA3 = LA1 - LA2. Only LA3 is needed for a gender gap question; only LA1 or LA2 is needed for a share question.
- `bopomr=0` is national aggregate (not in dim). Three hierarchy levels in dim.nuts — filter d.niveau.
- `kulturemne` here uses broad-category codes only (no sub-categories). `kulturemne=0` is the overall total.
- Parallel to ligeki2 which reports the gender split of disbursement amounts rather than person counts.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.