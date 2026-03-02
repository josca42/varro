table: fact.kv2fr1
description: Frivilligt arbejde efter hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- hyp: values [110200=1 eller flere gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110700=2-3 gange inden for de seneste 12 måneder, 110800=1 gang inden for de seneste 12 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Percentage of people who do voluntary work at each frequency level. hyp values are mutually exclusive for each respondent and sum to ~100% per kon+alder.
- To get "% who do any voluntary work": sum hyp 110200 through 110800 (exclude 111000=not done, 111100=no answer, 111200=don't know).
- For the national rate: filter kon='10' AND alder='TOT'. Single 2024 annual observation.
