table: fact.kv2sp8
description: Forbrug af live digitale spil-events efter køn, alder og tid
measure: indhold (unit Pct.)
columns:
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for the national total.
- Single measure per kon/alder/tid: % who have attended live digital gaming events.
- 2024 data only.
