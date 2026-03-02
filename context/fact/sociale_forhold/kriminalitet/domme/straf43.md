table: fact.straf43
description: Strafferetlige afgørelser pr. 100.000 indbyggere efter afgørelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- afgorelse: values [000=Afgørelsestype i alt, 1=1 Dom til frihedsstraf, 11=11 Ubetinget frihedsstraf, 111=111 Ubetinget dom alene, 112=112 Delvis betinget dom ... 514=514 Frifindelse, 515=515 Straf bortfaldet, 516=516 Militær straf, 517=517 Ingen tillægsstraf (§89), 518=518 Anden afgørelse i øvrigt]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- tid: date range 2018-01-01 to 2024-01-01

notes:
- indhold is a RATE (per 100,000 inhabitants), not a raw count. Do NOT sum across rows — each value is already population-normalised.
- No overtraed breakdown — only verdict type, gender, and age.
- afgorelse is hierarchical (same coding as straf40): 000 = all, 1/2/3/4/5 = main types, 11/12 = subtypes, 111-118/121-124 = specific forms. Filter to one level.
- kon does NOT include VIRKSOMHEDER (only M/K/TOT — persons only, unlike straf40/42/44).
- Only covers 2018-2024. Use straf40 for raw counts or longer time series.