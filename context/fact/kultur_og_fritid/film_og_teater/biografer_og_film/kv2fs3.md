table: fact.kv2fs3
description: Forbrug af film og serier efter adgang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- adgang: values [40950=Betalte tv-kanaler eller tv-pakker, 40960=Gratis tv-kanaler, 40970=Betalte streamingtjenester, 40980=Gratis streamingtjenester, 40990=Digitalt køb eller leje, 41000=Sociale medier, 41010=DVD, Blu-ray eller VHS, 41880=Andre adgange]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data, single year (2024 only). Values are percentages of respondents.
- adgang values are NOT mutually exclusive — a person can use paid streaming AND free TV AND buy digital. Do not sum across adgang; each value is an independent percentage.
- kon=10 and alder=TOT are totals.
- Use for questions like "what share of Danes use paid streaming vs. free TV channels for film consumption".