table: fact.recidiv9
description: Personer efter køn, alder, uddannelse, recidiv hændelser og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- rechen: values [0=I alt, 106=Ingen tilbagefald, 107=1 tilbagefald, 108=2 tilbagefald, 109=3 tilbagefald, 110=4-9 tilbagefald, 111=10 eller flere tilbagefald]
- tid: date range 2008 to 2024
notes:
- tid is rolling 3-year follow-up windows (starts 2008). Do not sum across overlapping tid values.
- uddannelse: 6 codes (TOT=I alt, 10=Grundskole, 20=Gymnasial, 35=Erhvervsuddannelse, 40=Videregående, 00=Uoplyst).
- rechen: 0=I alt, 106=Ingen tilbagefald, 107-111=1/2/3/4-9/10+ recidivisms. rechen=0 is exactly the sum of 106-111. To select recidivists: WHERE rechen NOT IN (0, 106).
- 4 dimension columns all have total rows (TOT/0). Clean total: kon='TOT', alder1=0, uddannelse='TOT', rechen=0, single tid.
