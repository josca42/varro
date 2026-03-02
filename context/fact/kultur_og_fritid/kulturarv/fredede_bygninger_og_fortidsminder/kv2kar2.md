table: fact.kv2kar2
description: Besøg på dansk kulturarv efter formål, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- formal: values [30670=At opleve den specifikke kulturarv, 30680=En kulturel begivenhed på stedet, 30690=En privat udflugt, 40180=Andre formål]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is percentage (Pct.) of kulturarv visitors citing each formal (purpose). Categories are NOT mutually exclusive — respondents can select multiple purposes, values sum to 89% across all formal. Do not sum; compare individual category rates.
- formal has 4 values: 30670=oplevelse af kulturarven, 30680=kulturel begivenhed, 30690=privat udflugt (largest at 49%), 40180=andre formål.
- Single year only (2024) — no trend analysis possible.