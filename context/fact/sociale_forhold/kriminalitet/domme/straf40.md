table: fact.straf40
description: Strafferetlige afgørelser efter overtrædelsens art, afgørelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- overtraed: values [TOT=Overtrædelsens art i alt, 1=Straffelov i alt, 1000=Uoplyst straffelov, 11=Seksualforbrydelser i alt, 1110=Blodskam mv. ... 3845=Love vedrørende forsvaret o.l., 3850=Love vedrørende offentlige forsyninger, 3855=Love vedrørende spil, bevilling, næring, 3865=Særlovgivning i øvrigt, 3870=Uoplyst særlovgivning]
- afgorelse: values [000=Afgørelsestype i alt, 1=1 Dom til frihedsstraf, 11=11 Ubetinget frihedsstraf, 111=111 Ubetinget dom alene, 112=112 Delvis betinget dom ... 514=514 Frifindelse, 515=515 Straf bortfaldet, 516=516 Militær straf, 517=517 Ingen tillægsstraf (§89), 518=518 Anden afgørelse i øvrigt]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, VIRKSOMHEDER=Virksomheder]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- overtraed uses inline hierarchical codes (same coding scheme as dim.overtraedtype niveaux 1-3, but no dim join): TOT = grand total, 1/2/3 = top-level (straffelov/færdselslov/særlov), 11/12/21... = subcategories, 4-digit codes = detailed types. The table contains codes at multiple levels mixed — filter to one level to avoid double-counting. E.g. WHERE overtraed IN ('1','2','3') for top-level breakdown.
- afgorelse is also inline hierarchical: 000 = all, 1/2/3/4/5 = main verdict types, 11/12 = subtypes of 1 (ubetinget/betinget frihedsstraf), 111-118/121-124 = specific sentence forms. Pick one level and filter consistently.
- alder: individual years 15-24 coexist with grouped bands (25-29, 30-39, ..., 80-). Mixing them overlaps. TOT = all ages, UA = uoplyst.
- kon includes VIRKSOMHEDER (companies) in addition to M/K/TOT — remember to filter kon='TOT' or exclude VIRKSOMHEDER when counting persons.
- To get simple total count by year: WHERE overtraed='TOT' AND afgorelse='000' AND alder='TOT' AND kon='TOT'. Omitting any one of these silently multiplies the sum.