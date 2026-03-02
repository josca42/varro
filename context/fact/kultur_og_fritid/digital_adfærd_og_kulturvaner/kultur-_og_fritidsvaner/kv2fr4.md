table: fact.kv2fr4
description: Forbrug af fritidsbegivenheder efter begivenhed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- begivenhed: values [43200=Foredrag eller debatarrangementer, 43210=Aftenskoleundervisning, 43220=Kulturel forening, 43230=Privatundervisning, 43240=Anden fritidsundervisning, 43250=Spejder, 43260=Højskoleophold, 43270=Madfestival, 43280=Kulturmøde eller folkemøde, 43290=Litteraturfestival, 43300=Kulturel festival, 43310=Andre begivenheder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Each begivenhed row is the percentage who attended that leisure event type in the past year. Events are NOT mutually exclusive — a person can have attended multiple types. DO NOT sum across begivenhed values.
- For the national rate per event type: filter kon='10' AND alder='TOT'. Single 2024 annual observation.
