table: fact.vie825k
description: Vielser efter mandens eller ældste persons alder, kvindens eller yngste persons alder, vielsesmyndighed, vielsesmåned og tid
measure: indhold (unit Antal)
columns:
- alderaegt1: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover, 999=Uoplyst alder]
- alderaegt2: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover, 999=Uoplyst alder]
- vimyn: values [1=Kirkelig, 2=Borgerlig, 3=Gift i udlandet, 4=Uoplyst vielsesmyndighed]
- vimdr: values [1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December, 999=Uoplyst måned]
- tid: date range 2020-01-01 to 2024-01-01

notes:
- Extended version of vie825 that adds `vimdr` (month). Limited to 2020–2024.
- `vimdr` uses plain integers 1–12 plus 999='Uoplyst måned' — same integer style as vie825k's vimyn (1–4), not the zero-padded 001–012 of vie9/viedag.
- Neither `vimyn` nor `vimdr` has an aggregate total code. To get annual totals, SUM across all months including vimdr=999.
- Use vie825 (2007–2024) for longer time series; use this table only when you need the month × authority × age cross-tabulation.