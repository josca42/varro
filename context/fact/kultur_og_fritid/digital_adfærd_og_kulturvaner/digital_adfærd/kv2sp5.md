table: fact.kv2sp5
description: Forbrug af digitale spil efter medspillere, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- medspil: values [42370=Partner eller ægtefælle, 42380=Forældre eller bedsteforældre, 42390=Børn i hjemmet, 42400=Børnebørn eller oldebørn, 42410=Andre familiemedlemmer, 42460=Venner som jeg kendte i forvejen og ser fysisk, 42470=Venner som jeg kun kender via onlinespil, 42480=Venner som jeg har lært at kende ved at spille onlinespil men nu også ser fysisk, 42490=Personer, jeg ikke kender, 42500=Andre medspillere]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- medspil (co-player type) values are NOT mutually exclusive — a gamer plays with multiple types of co-players. Never sum across medspil values.
- 2024 data only.
