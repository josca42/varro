table: fact.kv2sp2
description: Forbrug af digitale spil efter genre, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- genre: values [42290=Puzzlespil, 42300=Platformsspil, 42310=Sportsspil, 42320=Actionspil, 42330=Adventurespil, 42340=Strategispil, 42350=Kreative spil, simulationsspil eller sandkassespil, 42360=Andre typer spil]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- genre values are NOT mutually exclusive — a gamer plays multiple genres. Never sum across genre values.
- 2024 data only.
