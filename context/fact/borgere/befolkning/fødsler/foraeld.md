table: fact.foraeld
description: Antal forældre 1. januar efter køn, alder, antal børn og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 96=96 år, 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover]
- antborn: values [1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5=5 børn ... 21=21 børn, 22=22 børn, 23=23 børn, 24=24 børn, 25=25 børn]
- tid: date range 1986-01-01 to 2025-01-01
notes:
- kon has a TOT total row. alder has no IALT — use SUM across individual ages for a total. antborn has no IALT — each parent appears in exactly one antborn category, so SUM across antborn gives total count of parents.
- antborn actual range is 1–21 (the listed 22–25 are not in the data).
- alder special codes: 9915=Under 15 år, 100=100 år og derover (the doc shows "100-" but the actual code is 100). These sort oddly — cast carefully.
- This table counts parents alive on 1 January each year, not new parents per year. To find new parents (first-time), see fodpm/fodpf (lfnr=1).
