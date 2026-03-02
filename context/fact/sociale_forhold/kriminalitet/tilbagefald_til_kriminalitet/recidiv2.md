table: fact.recidiv2
description: Personer efter køn, alder, oprindelig lovovertrædelse, lovovertrædelse ved første tilbagefald og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- over: values [0=I alt, 1=Straffelov i alt, 2=Seksualforbrydelser, 3=Blodskam, voldtægt, hetero- og homoseksuelle sædelighedsforbrydelser i øvrigt, 4=Blufærdighedskrænkelser ... 39=Love vedr. dyr, jagt mv., 40=Love vedr. arbejde, transport, 41=Love vedr. forsvaret, 42=Love vedr. spil, bevilling, 99=Andet - Alt ikke nævnt i ovenstående.]
- over1: values [0=I alt, 11=Tilbagefald i alt, 2=Seksualforbrydelser, 5=Voldsforbrydelser i alt, 11=Ejendomsforbrydelser, i alt, 24=Andre straffelovsforbrydelser i alt, 30=Færdselslovsovertrædelser i alt, 35=Særlovsovertrædelser i alt, 0=Ingen tilbagefald]
- tid: date range 2007 to 2024
notes:
- tid is rolling 3-year follow-up windows (e.g. [2007,2010) = 2007 cohort). Do not sum across overlapping tid values.
- over1=0 means "I alt" (includes non-recidivists). over1 has only 7 codes (0, 2, 5, 11, 24, 30, 35): broad offense categories at first recidivism. Code 11 = Ejendomsforbrydelser i alt. ColumnValues shows id=0 twice and id=11 twice — metadata quirk; only one of each exists in the data. To see only recidivists: WHERE over1 != 0.
- over (original offense) has 42 codes with hierarchy — 0=I alt, 1=Straffelov i alt, 30=Færdselslov i alt, 35=Særlov i alt are aggregates. Never SUM across all non-zero over values.
- 4 dimension columns all have total rows (TOT/0). Clean total: kon='TOT', alder1=0, over=0, over1=0, single tid.
