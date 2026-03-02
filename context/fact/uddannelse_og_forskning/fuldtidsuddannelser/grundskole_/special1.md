table: fact.special1
description: Elever, grundskolen efter klassetrin, skoletype, specialundervisning, herkomst, køn og tid
measure: indhold (unit Antal)
columns:
- klasse: values [TOT=I alt, U20=U20 0. klassetrin, U21=U21 1. klassetrin, U22=U22 2. klassetrin, U23=U23 3. klassetrin, U24=U24 4. klassetrin, U25=U25 5. klassetrin, U26=U26 6. klassetrin, U27=U27 7. klassetrin, U28=U28 8. klassetrin, U29=U29 9. klassetrin, U30=U30 10. klassetrin]
- sktpe: values [0=I alt, 1012=FOLKESKOLER, 1012404155=Folkeskoler, normalklasser, 101250=Folkeskoler, specialklasser, 1014=UNGDOMSSKOLER OG ANDRE SKOLER, 1015=SPECIALSKOLER, 1016=DAGBEHANDLINGSCENTRE MV.]
- elev: values [0=Elever i alt, 5=Modtager ikke specialundervisning, 2=Modtager specialundervisning under 9 timer, 3=Modtager specialundervisning 9-20 timer, 4=Modtager specialundervisning over 20 timer, 6=Modtager specialundervisning, uoplyst timetal]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- sktpe has two hierarchy levels mixed together. Aggregate codes: 0=I alt, 1012=FOLKESKOLER (total), 1014=UNGDOMSSKOLER OG ANDRE, 1015=SPECIALSKOLER, 1016=DAGBEHANDLINGSCENTRE. Fine codes: 1012404155=Folkeskoler normalklasser, 101250=Folkeskoler specialklasser. Code 1012 = sum of 1012404155 + 101250. Filter to one level to avoid double-counting.
- elev column: 0=Elever i alt is the total of categories 2+3+4+5+6. Do not sum across all elev values. Filter to elev='0' for a total headcount, or pick individual categories for a breakdown.
- No dim joins — all columns are inline coded.