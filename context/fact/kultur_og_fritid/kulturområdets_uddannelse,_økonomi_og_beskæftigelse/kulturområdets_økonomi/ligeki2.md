table: fact.ligeki2
description: Ligestillingsindikator for Kulturministeriets udbetalinger til personer efter indikator, bopælsområde, kulturemne, aldersgrupper og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 12=KULTURARV, 1=MEDIER, BIBLIOTEKER OG LITTERATUR, 20=SCENE OG MUSIK, 23=VISUEL KUNST OG DESIGN, 29=ANDEN KULTUREL AKTIVITET]
- aldgrp: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- Same structure and same `indikator` rate-only semantics as ligeki1. NEVER sum across LA1/LA2/LA3 — filter to exactly one.
- Difference from ligeki1: this table covers disbursement amounts (kr.); ligeki1 covers recipient counts. Use ligeki2 for "what share of cultural funding goes to men/women", use ligeki1 for "what share of recipients are men/women".
- `bopomr=0` is national aggregate (not in dim). Filter d.niveau for geographic granularity.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.