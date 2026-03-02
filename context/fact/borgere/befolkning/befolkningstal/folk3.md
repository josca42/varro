table: fact.folk3
description: Befolkningen 1. januar efter fødselsdag, fødselsmåned, fødselsår og tid
measure: indhold (unit Antal)
columns:
- fdag: values [TOT=I alt, D01=1., D02=2., D03=3., D04=4. ... D27=27., D28=28., D29=29., D30=30., D31=31.]
- fmaaned: values [TOT=I alt, 001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December]
- fodaar: values [TOT=I alt, 1899=1899, 1900=1900, 1901=1901, 1902=1902 ... 2020=2020, 2021=2021, 2022=2022, 2023=2023, 2024=2024]
- tid: date range 2008-01-01 to 2025-01-01

notes:
- All three dimensions (fdag, fmaaned, fodaar) have TOT totals. Filter all non-target dimensions to TOT to avoid overcounting.
- fodaar goes back to 1899, so combined with tid you can compute e.g. "residents born in 1940" as of any January from 2008 to 2025.
- Useful for birthday distributions (days and months) and cohort analysis by birth year. No sex/region breakdown — use befolk2 or folk1a for those.
- fdag D31 has fewer people since not all months have 31 days; consider this when comparing days.