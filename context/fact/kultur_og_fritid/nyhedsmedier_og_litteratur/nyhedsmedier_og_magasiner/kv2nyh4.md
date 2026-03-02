table: fact.kv2nyh4
description: Oplevelse af mis- eller desinformerende nyhedsindhold efter hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- hyp: values [40510=Har ofte oplevet mis- eller desinformerende nyhedsindhold online, 40520=Har ind imellem oplevet mis- eller desinformerende nyhedsindhold online, 40530=Har kun sjældent oplevet mis- eller desinformerende nyhedsindhold online, 40540=Har ikke oplevet mis- eller desinformerende nyhedsindhold online, 40550=Ved ikke]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is Pct. of people who fall in each experience frequency category.
- hyp values ARE mutually exclusive — they are responses to a single question about frequency of encountering mis/disinformation. The 5 values sum to ~99% (koen='10'/alder='TOT'). Each person is in exactly one category.
- koen='10' = Køn i alt (total); alder='TOT' = Alder i alt (total). Filter to these for overall rates.
- To get "share who has ever experienced mis/disinformation", sum 40510 (ofte) + 40520 (ind imellem) + 40530 (sjældent).