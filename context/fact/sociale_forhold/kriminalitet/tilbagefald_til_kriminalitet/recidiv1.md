table: fact.recidiv1
description: Personer efter køn, alder, varighed til tilbagefald, oprindelig straf, oprindelig lovovertrædelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- vartilbage: values [0=I alt, 0=Ingen tilbagefald, 6=I løbet af 6 måneder, 712=Efter 6 måneder og indenfor 1 år, 1324=Efter 1 år og indenfor 2 år]
- strafart: values [0=I alt, 1=Løsladt efter afsoning i fængsel mv., 2=Løsladt efter afsoning på bopæl, 3=Foranstaltningsdom ophørt/ophævet, 4=Betinget dom og samfundstjeneste, 5=Betinget dom, 6=Bødeafgørelse, 7=Tiltalefrafald med vilkår, 8=Tiltalefrafald uden vilkår]
- over: values [0=I alt, 1=Straffelov i alt, 2=Seksualforbrydelser, 3=Blodskam, voldtægt, hetero- og homoseksuelle sædelighedsforbrydelser i øvrigt, 4=Blufærdighedskrænkelser ... 39=Love vedr. dyr, jagt mv., 40=Love vedr. arbejde, transport, 41=Love vedr. forsvaret, 42=Love vedr. spil, bevilling, 99=Andet - Alt ikke nævnt i ovenstående.]
- tid: date range 2007 to 2024

notes:
- tid is rolling 3-year follow-up windows (e.g. [2007,2010) = cohort released in 2007, tracked for 2 years). Each row covers a cohort, not a calendar year. Do not sum across overlapping tid values — pick one.
- vartilbage=0 means "I alt" (everyone in cohort, including non-recidivists). ColumnValues will show id=0 twice ("I alt" and "Ingen tilbagefald") — metadata quirk; only one code 0 exists. To select only recidivists: WHERE vartilbage != 0.
- over has 42 codes mixing aggregate and leaf levels: 0=I alt, 1=Straffelov i alt, 30=Færdselslov i alt, 35=Særlov i alt are aggregates; 2-29, 31-34, 36-42 are leaf categories. Never SUM across all non-zero over values — pick aggregate or leaf level to avoid double-counting. Use ColumnValues("recidiv1", "over") to see all labels.
- strafart here is the original punishment (1=afsoning i fængsel, 6=bødeafgørelse), codes 0-8. Different from strafart1/strafart2 in other tables (codes 100-105 for recidivism punishment).
- 5 dimension columns all have total rows (TOT/0). Forgetting any one inflates the sum. Clean total: kon='TOT', alder1=0, strafart=0, over=0, vartilbage=0, single tid.