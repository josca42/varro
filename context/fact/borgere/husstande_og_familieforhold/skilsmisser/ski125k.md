table: fact.ski125k
description: Skilsmisser efter mandens eller ældste persons alder, kvindens eller yngste persons alder, ægteskabets varighed, skilsmissemåned og tid
measure: indhold (unit Antal)
columns:
- alderaegt1: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover, 999=Uoplyst alder]
- alderaegt2: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover, 999=Uoplyst alder]
- agtvar: values [0=Under 1 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 47=47 år, 48=48 år, 49=49 år, 50=50 år og derover, 99=Uoplyst varighed]
- skmdr: values [1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December, 999=Uoplyst måned]
- tid: date range 2020-01-01 to 2024-01-01

notes:
- Same age and duration columns as ski125 (alderaegt1, alderaegt2, agtvar) but without geography (no bopaegt). Adds skmdr (month of divorce, 1–12, 999=Uoplyst).
- alderaegt1/alderaegt2: individual ages, no aggregate total — build age groups with CASE in SQL.
- agtvar: duration 0–50 years + 99=Uoplyst, no aggregate total.
- Annual data (2020–2024), limited range. Use for age × duration × month-of-year analysis at national level.