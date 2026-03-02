table: fact.kv2mk7
description: Forbrug af koncerter efter ledsager, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- ledsag: values [42370=Partner eller ægtefælle, 42380=Forældre eller bedsteforældre, 42390=Børn i hjemmet, 42400=Børnebørn eller oldebørn, 42410=Andre familiemedlemmer, 42420=Venner eller bekendte, 42430=Kollegaer eller studiekammerater, 42440=Alene, 42450=Andre ledsagere]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey percentages (single year 2024). ledsag values are NOT mutually exclusive — a respondent can attend concerts with multiple companion types on different occasions. Values sum to ~198%. Never sum across ledsag.
- Each row answers: "what % of concert-goers attended with this type of companion (at least once)?"
- kon='10' and alder='TOT' give the overall totals.