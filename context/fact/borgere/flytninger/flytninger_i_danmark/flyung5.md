table: fact.flyung5
description: Flytninger blandt unge (15-29-årige) efter flyttetype, fraflytningslandsdel, tilflytningslandsdel og tid
measure: indhold (unit Antal)
columns:
- flyttetype: values [0=Flyttetype i alt, 101=Flyttet fra forældre, 102=Flyttet til forældre, 103=Flyttet med/mellem forældre, 104=Øvrige flytninger]
- fraflytland: join dim.nuts on fraflytland=kode::text [approx]; levels [2]
- tilflytland: join dim.nuts on tilflytland=kode::text [approx]; levels [2]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Origin-destination matrix at landsdel level for young people 15–29. Both fraflytland and tilflytland use zero-padded codes (01–09, 10, 11) that don't match dim.nuts niveau 2 (1–11). Use integer cast for both joins: `JOIN dim.nuts fra ON f.fraflytland::int = fra.kode::int AND fra.niveau = 2` and same for tilflytland.
- TOTFL and TOTTL are aggregate codes — exclude both when you want the fra/til breakdown.
- flyttetype has `0` = total. All three non-tid columns have aggregates.
- To get e.g. "moves from Landsdel Byen København to all destinations": filter `fraflytland = '01'` and `tilflytland != 'TOTTL'` and `flyttetype != '0'`.
- Map: /geo/landsdele.parquet — OD matrix; merge on fraflytland::int=dim_kode (origin) or tilflytland::int=dim_kode (destination). Exclude TOTFL/TOTTL before casting.