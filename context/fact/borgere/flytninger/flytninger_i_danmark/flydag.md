table: fact.flydag
description: Flytninger efter flyttedag, flyttemåned og tid
measure: indhold (unit Antal)
columns:
- flyttedag: values [TOT=I alt, D01=1., D02=2., D03=3., D04=4. ... D27=27., D28=28., D29=29., D30=30., D31=31.]
- flyttedmaned: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Both columns have aggregate codes: `flyttedag=TOT` (all days) and `flyttedmaned=TOT` (all months). Failing to filter these inflates counts.
- To get moves by month: filter `WHERE flyttedag = 'TOT'` and group by `flyttedmaned`. To get moves by day-of-month: filter `WHERE flyttedmaned = 'TOT'` and group by `flyttedag`. For a specific month+day cell: filter both to non-TOT values.
- tid is annual (yearly rows). The month/day columns slice within a year, not across years.
- No geographic or demographic breakdown — national totals only.