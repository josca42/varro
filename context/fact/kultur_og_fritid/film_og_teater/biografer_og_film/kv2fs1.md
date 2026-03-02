table: fact.kv2fs1
description: Forbrug af film og serier efter oprindelsesland, hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- oprindland: values [40840=Dansk film, 40850=Udenlandsk film, 40860=Dansk serie, 40870=Udenlandsk serie]
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110900=Sjældnere end 1-2 gange inden for 3 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data, single year (2024 only). Values are percentages of respondents in each group.
- oprindland values (Dansk film, Udenlandsk film, Dansk serie, Udenlandsk serie) are NOT mutually exclusive — a person can watch all four types. Do not sum across oprindland.
- hyp values within a given oprindland are exhaustive frequency categories and do sum to ~100%. They represent the full distribution of viewing frequency for that content type.
- kon=10 and alder=TOT are totals. Age breakdown goes from 16–24 to 75+.
- Useful for comparing how frequently Danes watch domestic vs. foreign films/series.