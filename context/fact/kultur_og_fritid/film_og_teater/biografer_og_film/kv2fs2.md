table: fact.kv2fs2
description: Forbrug af film og serier efter lokation, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- lokation: values [40880=Derhjemme, 40890=Hos andre, 40900=På farten, 40910=I biografen, 40920=På filmfestivaler eller andre filmevents, 40930=Open air eller drive in bio, 42280=Andre steder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data, single year (2024 only). Values are percentages of respondents.
- lokation values are NOT mutually exclusive — a person can watch films at home AND in a cinema AND on-the-go. Do not sum across lokation; each value is an independent percentage.
- kon=10 and alder=TOT are totals.
- Use for questions like "what share of Danes watch films in cinemas vs. at home".