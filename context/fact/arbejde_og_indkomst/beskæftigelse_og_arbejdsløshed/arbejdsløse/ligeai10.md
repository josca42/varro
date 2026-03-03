table: fact.ligeai10
description: Ligestillingsindikator for langtidsledige efter indikator, alder, område og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- tid: date range 2009-01-01 to 2025-05-01
dim docs: /dim/nuts.md

notes:
- indikator selects between LA1/LA2/LA3. Never sum — pre-computed rates and difference.
- For langtidsledige (long-term unemployed ≥26 weeks), not all fuldtidsledige. Monthly, from 2009.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Companion to ligeai9a (same indicator structure, but for long-term unemployed).
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.