table: fact.flyung4
description: Flytninger blandt unge (15-29-årige) efter flyttetype, tilflytningslandsdel, aldersgruppe og tid
measure: indhold (unit Antal)
columns:
- flyttetype: values [0=Flyttetype i alt, 101=Flyttet fra forældre, 102=Flyttet til forældre, 103=Flyttet med/mellem forældre, 104=Øvrige flytninger]
- tilflytland: join dim.nuts on tilflytland=kode::text [approx]; levels [2]
- agebygroup: values [TOT1529=15-29 år i alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Same as flyung3 but for tilflytland (destination landsdel) instead of fraflytland.
- tilflytland uses zero-padded codes (01–09, 10, 11). Standard join fails for codes 01–09. Use: `JOIN dim.nuts d ON f.tilflytland::int = d.kode::int AND d.niveau = 2`.
- TOTTL is the aggregate code for all destination landsdele.
- agebygroup has `TOT1529` as aggregate; flyttetype has `0` as total. Filter appropriately.
- Covers only young people aged 15–29.
- Map: context/geo/landsdele.parquet — merge on tilflytland::int=dim_kode. Exclude tilflytland='TOTTL' before casting.