table: fact.kv2ahyp2
description: Forbrug af biograf, udøvende kunstarter, udstilling, bibliotek, sportsbegivenheder og kulturarv (år) efter kulturaktivitet, køn, alder, hyppighed og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [20100=Har været i biografen, 20200=Har været til koncert eller musikfestival, 20300=Har set scenekunst eller sceneforestillinger live, på internettet eller i TV, 20400=Har opsøgt billedkunst fysisk eller digitalt, 20500=Har været fysisk på biblioteket, 20600=Har benyttet bibliotekernes digitale tjenester, 20700=Har overværet sportsbegivenhed som tilskuer, 20800=Har været på museum, 20900=Har besøgt dansk kulturarv]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- hyp: values [110200=1 eller flere gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110700=2-3 gange inden for de seneste 12 måneder, 110800=1 gang inden for de seneste 12 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Annual counterpart to kv2hyp2 (same 201xx venue kultur codes). Single 2024 observation; hyp scale slightly different from quarterly version (uses 110600 instead of 110650, no 111050 "never done" code).
- To get "% who visited in past 12 months": sum hyp 110200 through 110800 (exclude 111000, 111100, 111200).
- Use kv2hyp2 for quarterly updates.
