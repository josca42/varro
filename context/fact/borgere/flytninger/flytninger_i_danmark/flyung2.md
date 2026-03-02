table: fact.flyung2
description: Flytninger blandt unge (15-29-årige) efter flyttetype, tilflytningskommune, tilflytningssted og tid
measure: indhold (unit Antal)
columns:
- flyttetype: values [0=Flyttetype i alt, 101=Flyttet fra forældre, 102=Flyttet til forældre, 103=Flyttet med/mellem forældre, 104=Øvrige flytninger]
- tilkommune: join dim.nuts on tilkommune=kode::text [approx]; levels [3]
- tilflytomr: values [TOT=Tilflytningssted i alt, 50=Inden for kommunen, 51=Mellem kommuner]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as flyung1, but with tilkommune (destination municipality) instead of frakommune.
- tilkommune joins dim.nuts niveau 3 (99 kommuner), but has aggregate code `TOTTK` (all til-kommuner). Filter `WHERE f.tilkommune != 'TOTTK'` before joining.
- tilflytomr has `TOT` and flyttetype has `0` as aggregates. Must filter all three to avoid overcounting — same pattern as flyung1.
- Covers only young people aged 15–29.
- Map: context/geo/kommuner.parquet — merge on tilkommune::int=dim_kode. Exclude tilkommune='TOTTK' before casting.