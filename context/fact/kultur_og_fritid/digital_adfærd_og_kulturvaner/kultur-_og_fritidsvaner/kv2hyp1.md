table: fact.kv2hyp1
description: Forbrug af medier, sociale medier, musik, litteratur, digitale spil, og sport og motion efter kulturaktivitet, køn, alder, hyppighed og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110650=2-5 gange hvert halve år, 110950=1-3 gange inden for de seneste 12 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111050=Det har jeg aldrig gjort (2025-), 111100=Ønsker ikke at svare, 111200=Ved ikke]
- tid: date range 2024-01-01 to 2025-04-01
notes:
- Covers digital/home consumption activities only (101xx kultur codes). For venue activities see kv2hyp2.
- hyp values are mutually exclusive frequency bands for each respondent per activity — they sum to ~100% for a given kultur+kon+alder. To find "% who did X at all in past 12 months", sum hyp 110100 through 110950 (exclude 111000=not done past 12m, 111050=never done, 111100=no answer, 111200=don't know). To get a single rate for the whole population: filter kon='10' AND alder='TOT'.
- Note: kv2hyp1 (quarterly) has a finer hyp scale (includes "2-5 gange hvert halve år" and "1-3 gange inden for 12 måneder") than kv2ahyp1 (annual, coarser bands). The hyp codes differ between the two — do not mix them.
- Annual counterpart: kv2ahyp1.
