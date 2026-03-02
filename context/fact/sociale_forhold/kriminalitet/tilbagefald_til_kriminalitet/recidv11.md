table: fact.recidv11
description: Personer efter køn, alder, tidligere domme, recidiv hændelser, straf ved første tilbagefald og tid
measure: indhold (unit Antal)
columns:
- konams: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [00=I alt, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- tidldom: values [0=I alt, 0=Ingen tidligere domme, 1=1 tidligere dom, 2=2 tidligere domme, 3=3 tidligere domme, 4=4 tidligere domme, 5=5-9 tidligere domme, 10=10 eller flere tidligere domme]
- rechen: values [0=I alt, 106=Ingen tilbagefald, 107=1 tilbagefald, 108=2 tilbagefald, 109=3 tilbagefald, 110=4-9 tilbagefald, 111=10 eller flere tilbagefald]
- strafart1: values [0=I alt, 100=Ubetinget dom, 101=Betinget dom og samfundstjeneste, 102=Betinget dom, 103=Bødeafgørelse, 104=Tiltalefrafald med vilkår, 105=Tiltalefrafald uden vilkår, 0=Ingen tilbagefald]
- tid: date range 2009 to 2024
notes:
- Uses konams (not kon) and alder (varchar, starts at 2024/20-24 år, no 15-19 group). tid starts 2009, rolling 3-year windows.
- tidldom: ColumnValues shows id=0 twice — metadata quirk; only one code 0 = I alt. To filter to those with no prior convictions: tidldom=1 (1 previous dom = actually first-timers if interpreting "Ingen" as 0, but confirm: tidldom=0 is I alt, so use specific codes 1-10 for granular analysis).
- strafart1 is punishment at first recidivism (codes 0/100-105). strafart1=0 in data = I alt. ColumnValues shows id=0 twice ("I alt" and "Ingen tilbagefald").
- rechen: 0=I alt, 106=Ingen tilbagefald, 107-111=recidivism counts.
- 5 dimension columns all have total rows. Clean total: konams='TOT', alder='0', tidldom=0, rechen=0, strafart1=0, single tid.
