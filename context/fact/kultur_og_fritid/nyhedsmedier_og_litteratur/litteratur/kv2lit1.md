table: fact.kv2lit1
description: Forbrug af litteratur efter genre, hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- genre: values [40700=Skønlitteratur, 40710=Faglitteratur]
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110900=Sjældnere end 1-2 gange inden for 3 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is a percentage (Pct.).
- genre has 2 values: 40700=Skønlitteratur, 40710=Faglitteratur. These are independent survey questions — a person can read both. Never sum across genres; always filter to one.
- hyp (hyppighed/frequency) values are mutually exclusive and sum to ~100% for a given genre+kon+alder. They represent a full frequency distribution (how often the respondent reads that genre). Safe to compare values within a genre slice.
- kon=10 ("Køn i alt") and alder='TOT' ("Alder i alt") are totals. Filter to one value for each to avoid overcounting.
- Single time point (2024). No trend analysis possible.