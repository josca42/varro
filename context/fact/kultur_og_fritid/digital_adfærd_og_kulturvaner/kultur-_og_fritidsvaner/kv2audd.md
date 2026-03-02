table: fact.kv2audd
description: Forbrug af kulturaktiviteter (år) efter kulturaktivitet, køn, højest fuldførte uddannelse og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion, 20100=Har været i biografen, 20200=Har været til koncert eller musikfestival, 20300=Har set scenekunst eller sceneforestillinger live, på internettet eller i TV, 20400=Har opsøgt billedkunst fysisk eller digitalt, 20500=Har været fysisk på biblioteket, 20600=Har benyttet bibliotekernes digitale tjenester, 20700=Har overværet sportsbegivenhed som tilskuer, 20800=Har været på museum, 20900=Har besøgt dansk kulturarv]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- hfudd2: values [1000=Uddannelse i alt, 1010=Ingen eller uoplyst uddannelse, 1020=Grundskole, 1030=Gymnasiale uddannelser, 1040=Erhvervsfaglige uddannelser, 1050=Korte og mellemlange videregående uddannelser, 1060=Bacheloruddannelser, lange videregående uddannelser, og ph.d.- og forskeruddannelser]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Annual counterpart to kv2udd. Identical structure (kultur, kon, hfudd2) but only 2024 data. Use kv2udd for quarterly updates.
- Filter kon='10' AND hfudd2='1000' for national totals.
