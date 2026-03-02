table: fact.kv2hoved
description: Forbrug af kulturaktiviteter efter kulturaktivitet, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion, 20100=Har været i biografen, 20200=Har været til koncert eller musikfestival, 20300=Har set scenekunst eller sceneforestillinger live, på internettet eller i TV, 20400=Har opsøgt billedkunst fysisk eller digitalt, 20500=Har været fysisk på biblioteket, 20600=Har benyttet bibliotekernes digitale tjenester, 20700=Har overværet sportsbegivenhed som tilskuer, 20800=Har været på museum, 20900=Har besøgt dansk kulturarv]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2025-04-01
notes:
- indhold is a percentage — the share of respondents who did that activity in the past 12 months. DO NOT sum across kultur values; each is an independent yes/no question.
- kultur splits into two groups: 101xx = digital/home consumption (film, serier, musik, bøger, nyheder, sociale medier, digitale spil, sport/motion); 201xx = physical/venue activities (biograf, koncert, scenekunst, billedkunst, bibliotek, sportsbegivenhed, museum, kulturarv).
- To get one activity rate for the whole population: filter kon='10' AND alder='TOT'. Forgetting either dimension doubles/multiplies the result set.
- This is the quarterly-updated table (from 2024). For annual figures use kv2ahov (identical structure, single 2024 observation). For education breakdown use kv2udd. For urbanisation breakdown use kv2urb. For geographic breakdown by kommune use kv2geo.
