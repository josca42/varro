table: fact.recidiv5
description: Personer efter køn, alder, oprindelig straf, oprindelig lovovertrædelse, recidiv hændelser og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- strafart: values [0=I alt, 1=Løsladt efter afsoning i fængsel mv., 2=Løsladt efter afsoning på bopæl, 3=Foranstaltningsdom ophørt/ophævet, 4=Betinget dom og samfundstjeneste, 5=Betinget dom, 6=Bødeafgørelse, 7=Tiltalefrafald med vilkår, 8=Tiltalefrafald uden vilkår]
- over: values [0=I alt, 1=Straffelov i alt, 2=Seksualforbrydelser, 3=Blodskam, voldtægt, hetero- og homoseksuelle sædelighedsforbrydelser i øvrigt, 4=Blufærdighedskrænkelser ... 39=Love vedr. dyr, jagt mv., 40=Love vedr. arbejde, transport, 41=Love vedr. forsvaret, 42=Love vedr. spil, bevilling, 99=Andet - Alt ikke nævnt i ovenstående.]
- rechen: values [0=I alt, 106=Ingen tilbagefald, 107=1 tilbagefald, 108=2 tilbagefald, 109=3 tilbagefald, 110=4-9 tilbagefald, 111=10 eller flere tilbagefald]
- tid: date range 2007 to 2024
notes:
- tid is rolling 3-year follow-up windows. Do not sum across overlapping tid values.
- rechen counts recidivism events per person: 0=I alt, 106=Ingen tilbagefald, 107=1 tilbagefald, ..., 111=10+. rechen=0 is exactly the sum of codes 106-111 (verified). To select recidivists: WHERE rechen NOT IN (0, 106).
- over (original offense) has 42 codes with hierarchy — never sum all non-zero values.
- strafart (original punishment, codes 0-8) has total row strafart=0.
- 5 dimension columns all have total rows (TOT/0). Clean total: kon='TOT', alder1=0, strafart=0, over=0, rechen=0, single tid.
