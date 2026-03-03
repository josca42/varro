table: fact.ligeai9a
description: Ligestillingsindikator for fuldtidsledige efter indikator, alder, område og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- tid: date range 2007-01-01 to 2025-03-01
dim docs: /dim/nuts.md

notes:
- indikator selects between pre-computed values: LA1=unemployment rate for men (pct), LA2=for women (pct), LA3=gender gap (LA1-LA2, procentpoint). Never sum across indikator values.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Annual data (ultimo november). For seasonally adjusted monthly gender indicators use ligeai9b (no region/age). For long-term unemployed gender indicators use ligeai10.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.