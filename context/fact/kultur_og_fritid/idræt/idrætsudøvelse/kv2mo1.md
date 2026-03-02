table: fact.kv2mo1
description: Forbrug af sport og motion efter sted, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- sted: values [41420=I forening eller klub, 41430=I kommercielt motions- eller fitnesscenter, 41440=I offentligt motionstilbud eller træningscenter, 41450=I centre eller anlæg, hvor man booker baner eller plads fra gang til gang, 41460=På arbejde eller uddannelse, 41470=På aftenskole, 41480=Andre steder uden for hjemmet, 41490=Derhjemme, 41500=Derhjemme via en onlineplatform, 41510=Under transport, 42280=Andre steder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- sted values are NOT mutually exclusive — respondents can exercise in multiple locations. Values sum to ~199% for kon=10, alder=TOT. Each row = "X% of sport/motion consumers use this location".
- Single time point (2024 only) — no time series possible.
- kon 10=i alt, alder TOT=i alt. Filter to avoid overlapping populations.