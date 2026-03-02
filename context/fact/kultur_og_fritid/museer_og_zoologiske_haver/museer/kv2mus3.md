table: fact.kv2mus3
description: Besøg på museum efter ledsager, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- ledsag: values [42370=Partner eller ægtefælle, 42380=Forældre eller bedsteforældre, 42390=Børn i hjemmet, 42400=Børnebørn eller oldebørn, 42410=Andre familiemedlemmer, 42420=Venner eller bekendte, 42430=Kollegaer eller studiekammerater, 42440=Alene, 42450=Andre ledsagere]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who visited a museum with that companion type. ledsag values are independent — a person can visit with multiple companions on different occasions. Sums exceed 100%, so never aggregate across ledsag.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).