table: fact.flyung3
description: Flytninger blandt unge (15-29-årige) efter flyttetype, fraflytningslandsdel, aldersgruppe og tid
measure: indhold (unit Antal)
columns:
- flyttetype: values [0=Flyttetype i alt, 101=Flyttet fra forældre, 102=Flyttet til forældre, 103=Flyttet med/mellem forældre, 104=Øvrige flytninger]
- fraflytland: join dim.nuts on fraflytland=kode::text [approx]; levels [2]
- agebygroup: values [TOT1529=15-29 år i alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- fraflytland uses zero-padded codes (01–09, 10, 11) for the 11 landsdele, but dim.nuts niveau 2 uses unpadded integers (1–11). Standard join fails for codes 01–09. Use: `JOIN dim.nuts d ON f.fraflytland::int = d.kode::int AND d.niveau = 2`.
- TOTFL is the aggregate code for all landsdele — exclude when joining to dim or when you don't want the national total.
- agebygroup has `TOT1529` as aggregate. Filter to `IN ('1519', '2024', '2529')` for age group breakdown.
- flyttetype has `0` = total. All three non-tid columns have aggregates — filter appropriately.
- Covers only young people aged 15–29.
- Map: /geo/landsdele.parquet — merge on fraflytland::int=dim_kode. Exclude fraflytland='TOTFL' before casting.