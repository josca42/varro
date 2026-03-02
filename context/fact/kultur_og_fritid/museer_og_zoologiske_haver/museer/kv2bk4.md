table: fact.kv2bk4
description: Selvudøvelse af billedkunst efter udøvelsessted, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- udoested: values [30280=Skaber billedkunst derhjemme, 30290=Skaber billedkunst uden for hjemmet]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who create visual art at that location. udoested has only 2 values (home vs. outside home) — a person can do both. Values are independent; do not sum.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).