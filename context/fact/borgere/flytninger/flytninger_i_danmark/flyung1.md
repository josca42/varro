table: fact.flyung1
description: Flytninger blandt unge (15-29-årige) efter flyttetype, fraflytningskommune, tilflytningssted og tid
measure: indhold (unit Antal)
columns:
- flyttetype: values [0=Flyttetype i alt, 101=Flyttet fra forældre, 102=Flyttet til forældre, 103=Flyttet med/mellem forældre, 104=Øvrige flytninger]
- frakommune: join dim.nuts on frakommune=kode::text [approx]; levels [3]
- tilflytomr: values [TOT=Tilflytningssted i alt, 50=Inden for kommunen, 51=Mellem kommuner]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- frakommune joins dim.nuts niveau 3 (99 kommuner), but the fact table also has aggregate code `TOTFK` (all fra-kommuner) which has no dim row. Filter `WHERE f.frakommune != 'TOTFK'` before joining, or use a LEFT JOIN.
- tilflytomr has a `TOT` aggregate. Filter `WHERE tilflytomr != 'TOT'` when you want the within/between split; use `TOT` for overall kommune totals.
- flyttetype has `0` = total. Filter to `IN (101, 102, 103, 104)` for move-type breakdown.
- All three non-tid columns have aggregates — failing to filter any one of them inflates counts. For totals by frakommune: filter `tilflytomr = 'TOT'` and `flyttetype = '0'`.
- Covers only young people aged 15–29.
- Map: /geo/kommuner.parquet — merge on frakommune::int=dim_kode. Exclude frakommune='TOTFK' before casting.