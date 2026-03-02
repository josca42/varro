table: fact.kv2ai1
description: Brug af kunstig intelligens efter hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110900=Sjældnere end 1-2 gange inden for 3 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- hyp (frequency) values are mutually exclusive — one frequency bucket per person. '111000' = har ikke brugt kunstig intelligens i seneste 12 måneder. To get share of AI users, filter hyp != '111000' (also exclude '111100','111200') and sum.
- 2024 data only.
