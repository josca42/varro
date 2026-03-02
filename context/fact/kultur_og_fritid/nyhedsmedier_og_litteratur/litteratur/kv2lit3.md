table: fact.kv2lit3
description: Forbrug af skønlitteratur efter adgang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- adgang: values [40760=Abonnementstjenester, 40770=Digitalt køb eller leje, 40780=Digitalt lån eller gratis tjenester, 40790=Køb af fysiske bøger eller CD, 40800=Lån på bibliotek, 40810=Lån af familie, venner eller bekendte, 40820=Får i gave, 40830=Bogbytte, 41880=Andre adgange]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only), scoped to skønlitteratur readers. indhold is a percentage (Pct.).
- adgang values are NON-mutually exclusive — respondents can access books through multiple channels. The 9 values sum to >170%. Never sum across adgang values; each is an independent rate.
- kon=10 ("Køn i alt") and alder='TOT' are totals. Filter to one value for each.
- Single time point (2024). No trend analysis possible.