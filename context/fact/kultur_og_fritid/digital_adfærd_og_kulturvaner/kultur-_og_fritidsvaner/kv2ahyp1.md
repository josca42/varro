table: fact.kv2ahyp1
description: Forbrug af medier, sociale medier, musik, litteratur, digitale spil, og sport og motion (år) efter kulturaktivitet, køn, alder, hyppighed og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110900=Sjældnere end 1-2 gange inden for 3 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Annual counterpart to kv2hyp1 (same digital/home 101xx kultur codes). Single 2024 observation with a coarser hyp scale than the quarterly version — notably missing the sub-weekly fine-grained bands; uses 110600 (1-2 gange inden for 3 måneder) and 110900 (sjældnere) instead.
- To get "% who did X at all in past 12 months": sum hyp 110100 through 110900 (exclude 111000, 111100, 111200).
- Use kv2hyp1 for quarterly updates.
