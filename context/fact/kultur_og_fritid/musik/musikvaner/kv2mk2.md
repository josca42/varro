table: fact.kv2mk2
description: Forbrug af musik efter lokation, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- lokation: values [40880=Derhjemme, 40890=Hos andre, 40900=På farten, 41920=Koncerter, 41930=Festivaler eller andre musikevents, 41940=På arbejde eller uddannelse, 42280=Andre steder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Single survey year (2024) — no time series.
- indhold is a percentage (Pct.). lokation categories are multi-select — people listen in multiple places. Categories sum to ~329 for kon=10/alder='TOT'. Never sum across lokation.
- Each row is an independent rate: "X% of respondents listen to music in this location." The highest is derhjemme (40880) at 95% for the total population.
- Notable split: passive everyday locations (40880 derhjemme, 40890 hos andre, 40900 på farten, 41940 arbejde/uddannelse) vs. live events (41920 koncerter, 41930 festivaler). These are different in character — everyday listening vs. attendance behaviour.
- Filter to kon=10 AND alder='TOT' for population totals.