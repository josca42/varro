table: fact.kv2nyh3
description: Forbrug af nyheder efter nyhedsmedie, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- nymedie: values [40350=Lokale eller regionale kommercielle nyhedsmedier, 40360=Regionale public servicemedier, 40370=Nationale kommercielle nyhedsmedier, landsdækkende aviser eller tv-stationer, 40380=Nationale public servicenyhedsmedier, 40390=Udenlandske nyhedsmedier]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is Pct. of people who consume news from each media type.
- nymedie values are NOT mutually exclusive — a person can consume news from multiple media types. The 5 nymedie values sum to 231% for koen='10'/alder='TOT'. Never sum across nymedie.
- koen='10' = Køn i alt (total); alder='TOT' = Alder i alt (total). Filter to these for overall rates.
- Use for questions like "what share uses public service vs commercial media" — compare individual nymedie rows side by side.