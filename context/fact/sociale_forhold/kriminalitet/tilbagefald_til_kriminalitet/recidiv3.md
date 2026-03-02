table: fact.recidiv3
description: Personer efter køn, alder, oprindelig straf, oprindelig lovovertrædelse, lovovertrædelse ved første tilbagefald, straf ved første tilbagefald og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- strafart: values [0=I alt, 1=Løsladt efter afsoning i fængsel mv., 2=Løsladt efter afsoning på bopæl, 3=Foranstaltningsdom ophørt/ophævet, 4=Betinget dom og samfundstjeneste, 5=Betinget dom, 6=Bødeafgørelse, 7=Tiltalefrafald med vilkår, 8=Tiltalefrafald uden vilkår]
- over: values [0=I alt, 1=Straffelov i alt, 2=Seksualforbrydelser, 3=Blodskam, voldtægt, hetero- og homoseksuelle sædelighedsforbrydelser i øvrigt, 4=Blufærdighedskrænkelser ... 39=Love vedr. dyr, jagt mv., 40=Love vedr. arbejde, transport, 41=Love vedr. forsvaret, 42=Love vedr. spil, bevilling, 99=Andet - Alt ikke nævnt i ovenstående.]
- over1: values [0=I alt, 11=Tilbagefald i alt, 2=Seksualforbrydelser, 5=Voldsforbrydelser i alt, 11=Ejendomsforbrydelser, i alt, 24=Andre straffelovsforbrydelser i alt, 30=Færdselslovsovertrædelser i alt, 35=Særlovsovertrædelser i alt, 0=Ingen tilbagefald]
- strafart1: values [0=I alt, 100=Ubetinget dom, 101=Betinget dom og samfundstjeneste, 102=Betinget dom, 103=Bødeafgørelse, 104=Tiltalefrafald med vilkår, 105=Tiltalefrafald uden vilkår, 0=Ingen tilbagefald]
- tid: date range 2007 to 2024
notes:
- tid is rolling 3-year follow-up windows. Do not sum across overlapping tid values.
- strafart (original punishment, codes 0-8) and strafart1 (punishment at first recidivism, codes 0/100-105) use different coding schemes. strafart1=0 means "Ingen tilbagefald" (not I alt — it maps to the "no recidivism" group). To select those who recidivated: WHERE strafart1 != 0.
- over (original offense) has 42 codes with hierarchy — filter to aggregate or leaf level, never sum all.
- over1 (recidivism offense at first recidivism) has 7 codes (0, 2, 5, 11, 24, 30, 35). over1=0 is I alt.
- 6 dimension columns all have total rows (TOT/0). Clean total: kon='TOT', alder1=0, strafart=0, over=0, over1=0, strafart1=0, single tid.
