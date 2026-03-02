table: fact.kv2mk3
description: Forbrug af musik efter genre, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- genre: values [41960=Klassisk musik, 41970=Jazz, 41980=Rock, 41990=Pop, 42000=Hiphop, 42010=Folkemusik og viser, 42020=Dansktop, 42030=Elektronisk musik, 42040=Soul, R&B, blues eller funk, 42050=Børnemusik, 42060=Andre genrer]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Single survey year (2024) — no time series.
- indhold is a percentage (Pct.). genre categories are multi-select — people listen to multiple genres. Categories sum to ~328 for kon=10/alder='TOT'. Never sum across genre.
- Each row is an independent rate: "X% of respondents listen to this genre." Compare genres directly for popularity rankings.
- 11 genre categories including "Andre genrer" (42060). The main named genres cover classical, jazz, rock, pop, hiphop, folkemusik, dansktop, elektronisk, soul/R&B, børnemusik.
- Filter to kon=10 AND alder='TOT' for population totals. Age breakdowns are particularly meaningful here (genre preferences differ strongly by age group).