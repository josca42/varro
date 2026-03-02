table: fact.folk3fod
description: Befolkningen 1. januar efter fødselsdag, fødselsmåned, fødeland og tid
measure: indhold (unit Antal)
columns:
- fdag: values [TOT=I alt, D01=1., D02=2., D03=3., D04=4. ... D27=27., D28=28., D29=29., D30=30., D31=31.]
- fmaaned: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- fodland: values [DANSK=Dansk, UDLAND=Udenlandsk]
- tid: date range 2008-01-01 to 2025-01-01

notes:
- Like folk3 but cross-tabulated with birth country (only DANSK vs UDLAND — not individual countries). Use bef5 for specific birth countries.
- All of fdag, fmaaned have TOT totals. No total for fodland — to get all residents, sum DANSK+UDLAND or don't filter fodland.
- Filter non-target dims to TOT (fdag=TOT, fmaaned=TOT) for totals by birth country.