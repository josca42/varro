table: fact.kv2mks1
description: Udøvelse af musik efter hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110900=Sjældnere end 1-2 gange inden for 3 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Single survey year (2024) — no time series analysis possible.
- indhold is a percentage (Pct.). hyp categories are mutually exclusive: they sum to exactly 100 for any kon/alder combination. Safe to read as a frequency distribution.
- 43% of the total population (kon=10, alder='TOT') have not played music in the past 12 months (hyp=111000). Two additional non-response codes: 111100 (ønsker ikke at svare, 2%) and 111200 (ved ikke, 6%). To isolate active players, filter WHERE hyp NOT IN (111000, 111100, 111200).
- For a simple "what share plays music at least weekly": WHERE hyp IN (110100, 110300, 110400). At least monthly adds 110500.
- kon and alder have total rows (10 and 'TOT'). To get an overall population figure, filter to kon=10 AND alder='TOT'. Omitting these inflates counts by ~3x (3 kon values × 8 alder values).
- For "udøvelse efter måde" (which instruments/methods), use kv2mks2 instead — but kv2mks1 is the right table for "how often do Danes play music".