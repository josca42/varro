table: fact.recidiv8
description: Personer efter køn, alder, uddannelse, straf (ved strengeste straf i opfølgningsperioden) og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder1: values [0=I alt, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- strafart2: values [0=I alt, 100=Ubetinget dom, 101=Betinget dom og samfundstjeneste, 102=Betinget dom, 103=Bødeafgørelse, 104=Tiltalefrafald med vilkår, 105=Tiltalefrafald uden vilkår, 0=Ingen tilbagefald]
- tid: date range 2008 to 2024
notes:
- tid is rolling 3-year follow-up windows (starts 2008). Do not sum across overlapping tid values.
- uddannelse: 6 codes (TOT=I alt, 10=Grundskole, 20=Gymnasial, 35=Erhvervsuddannelse, 40=Videregående, 00=Uoplyst).
- strafart2 is punishment at the strictest sentence in the follow-up period (codes 0/100-105). strafart2=0 in data means I alt. ColumnValues shows id=0 twice ("I alt" and "Ingen tilbagefald") — metadata quirk.
- 4 dimension columns all have total rows (TOT/0). Clean total: kon='TOT', alder1=0, uddannelse='TOT', strafart2=0, single tid.
