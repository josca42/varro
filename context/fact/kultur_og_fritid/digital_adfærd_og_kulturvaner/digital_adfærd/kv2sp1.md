table: fact.kv2sp1
description: Forbrug af digitale spil efter lokation, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- lokation: values [40880=Derhjemme, 40890=Hos andre, 40900=På farten, 42250=Til spilleevents eller formelle spillearrangementer, 42260=På arbejde eller uddannelse, 42270=I klub eller forening som esport, 42280=Andre steder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- lokation values are NOT mutually exclusive — a gamer plays in multiple locations. Values sum to ~117%. Each row is an independent % of population who play games at that location. Never sum across lokation values.
- 2024 data only.
