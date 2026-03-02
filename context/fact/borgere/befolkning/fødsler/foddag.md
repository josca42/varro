table: fact.foddag
description: Levendefødte efter fødselsdag, fødselsmåned og tid
measure: indhold (unit Antal)
columns:
- fdag: values [TOT=I alt, D01=1., D02=2., D03=3., D04=4. ... D27=27., D28=28., D29=29., D30=30., D31=31.]
- fmaaned: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- Both fdag and fmaaned have a TOT total row. fdag='TOT' collapses days into monthly totals; fmaaned='TOT' collapses months into day-of-month pattern. Filter fdag='TOT' AND fmaaned='TOT' for a single annual total per year.
- To count births by day of week you need an external calendar — the table only gives day-of-month (D01–D31) and month (001–012), not weekday.
