table: fact.special2
description: Elever, grundskolen efter klassetrin, specialundervisning, herkomst, køn og tid
measure: indhold (unit Antal)
columns:
- klasse: values [TOT=I alt, U20=U20 0. klassetrin, U21=U21 1. klassetrin, U22=U22 2. klassetrin, U23=U23 3. klassetrin, U24=U24 4. klassetrin, U25=U25 5. klassetrin, U26=U26 6. klassetrin, U27=U27 7. klassetrin, U28=U28 8. klassetrin, U29=U29 9. klassetrin, U30=U30 10. klassetrin]
- elev: values [0=Elever i alt, 5=Modtager ikke specialundervisning, 6=Modtager specialundervisning, uoplyst timetal]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- elev column: 0=Elever i alt (total), 5=modtager ikke specialundervisning, 6=modtager specialundervisning uoplyst timetal. Filter to elev='0' for totals or elev='6' for specialundervisning share.
- Simpler than special1: no sktpe breakdown, covers all skoler. Use this when you don't need a school-type breakdown.
- No dim joins — all inline coded.