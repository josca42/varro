table: fact.viedag
description: Vielser efter vielsesdag, vielsesmåned og tid
measure: indhold (unit Antal)
columns:
- vdag: values [TOT=I alt, D01=1., D02=2., D03=3., D04=4. ... D27=27., D28=28., D29=29., D30=30., D31=31.]
- vimdr: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Both `vdag` and `vimdr` have TOT aggregate codes. For a total by day-of-month across all months, use `vimdr='TOT'`. For totals by month across all days, use `vdag='TOT'`. For a specific day in a specific month, filter both.
- `vdag` codes are D01–D31 (uppercase D prefix + zero-padded day). `vimdr` uses zero-padded 001–012 + TOT — same coding as vie9, not the plain-integer style of vie325/vie825k.
- Useful for finding popular marriage dates (e.g. weekends, specific dates like 07-07-07).