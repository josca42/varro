table: fact.doddag
description: Døde efter dødsdag, dødsmåned og tid
measure: indhold (unit Antal)
columns:
- ddag: values [TOT=I alt, D01=1., D02=2., D03=3., D04=4. ... D27=27., D28=28., D29=29., D30=30., D31=31.]
- dman: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Both ddag and dman have total rows (ddag='TOT', dman='TOT'). Summing all rows for a given year counts each death multiple times — filter both to non-TOT for cross-tabulations, or filter one to TOT when looking at a single dimension.
- To get deaths by day-of-month across all months: WHERE dman='TOT' AND ddag != 'TOT'.
- To get deaths by month across all days: WHERE ddag='TOT' AND dman != 'TOT'.
- Useful for seasonality analysis: monthly deaths from 001=Januar to 012=December.