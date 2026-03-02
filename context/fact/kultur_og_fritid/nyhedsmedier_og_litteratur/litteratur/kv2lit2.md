table: fact.kv2lit2
description: Forbrug af skønlitteratur efter format, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- format: values [40720=Fysiske bøger, 40730=E-bøger, 40740=Lydbøger, 40750=Andre formater]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only), scoped to skønlitteratur readers. indhold is a percentage (Pct.).
- format values are NON-mutually exclusive — respondents can read in multiple formats. The 4 values sum to >100%. Never sum across format values; each is an independent rate.
- kon=10 ("Køn i alt") and alder='TOT' are totals. Filter to one value for each.
- Single time point (2024). No trend analysis possible.