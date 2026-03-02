table: fact.vie9
description: Vielser efter vielsesmyndighed, vielsesmåned og tid
measure: indhold (unit Antal)
columns:
- vimyn: values [TOT=I alt, 1=Kirkelig, 2=Borgerlig, 3=Gift i udlandet, 4=Uoplyst vielsesmyndighed]
- vimdr: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Both `vimyn` and `vimdr` have aggregate total codes (TOT). For annual total marriages: `vimyn='TOT' AND vimdr='TOT'`. To avoid overcounting, always filter each dimension to either its TOT or a specific subset — never mix TOT and individual values in the same result.
- Month codes are zero-padded 3-digit strings: '001'='Januar' … '012'='December'. This differs from vie325/vie825k which use plain integers (1-12).
- For monthly breakdown across all authority types: `WHERE vimyn='TOT' AND vimdr != 'TOT'`.
- For authority type breakdown across the full year: `WHERE vimdr='TOT' AND vimyn != 'TOT'`.