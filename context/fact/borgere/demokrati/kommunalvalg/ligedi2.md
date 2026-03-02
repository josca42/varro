table: fact.ligedi2
description: Ligestillingsindikator for opstillede og valgte kandidater til kommunalvalg efter kandidater, indikator, alder, kommune og tid
measure: indhold (unit -)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [TOT=Alder i alt, U20=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 70OV=70 år og derover]
- komk: join dim.nuts on komk=kode; levels [1, 2, 3]
- tid: date range 2005-01-01 to 2021-01-01
dim docs: /dim/nuts.md

notes:
- indikator has three semantically independent values: LA1=Mænd (%), LA2=Kvinder (%), LA3=Forskel (procentpoint). Never sum or aggregate across indikator values — each is a different measure of the same population.
- komk joins dim.nuts at niveau 1 (5 regioner), 2 (11 landsdele), 3 (98 kommuner), plus '0' = national aggregate not in dim. Filter to one niveau.
- kandidat distinguishes OK (nominated) vs VK (elected). Pick one per query.
- For raw counts rather than derived indicators, use ligedb2 instead.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on komk=dim_kode. Exclude komk=0.