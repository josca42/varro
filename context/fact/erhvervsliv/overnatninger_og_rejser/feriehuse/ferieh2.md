table: fact.ferieh2
description: Fremtidige bookede hus-uger, feriehuse efter gæstens nationalitet, fremtidig år, fremtidig måned og tid
measure: indhold (unit Antal)
columns:
- nation1: values [TOT=I alt, DAN=Danmark, HOL=Nederlandene, SVE=Sverige, NOR=Norge, TYS=Tyskland, ANDRE=Uoplyst land]
- fremar: values [2005=2005, 2006=2006, 2007=2007, 2008=2008, 2009=2009 ... 2021=2021, 2022=2022, 2023=2023, 2024=2024, 2025=2025]
- fremmd: values [1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 2005-01-01 to 2025-08-01

notes:
- This is a forward-looking bookings table. tid = the "as-of" date (monthly snapshot), fremar+fremmd = the future holiday month being tracked. Use it to see how advance bookings for a future month accumulate over time.
- To get the latest booking state for all future months: filter tid = (SELECT MAX(tid) FROM fact.ferieh2) then group by fremar, fremmd.
- To track how bookings for a specific future period grew: filter fremar=2025 AND fremmd=7 and show indhold by tid — each row shows the booking count at that reporting point.
- nation1=TOT covers all nationalities. Do not sum across all nation1 values. Do not sum across fremar+fremmd combinations unless you want total booked weeks for an entire year.
- fremar goes 2005–2025 and fremmd is 1–12 (Jan–Dec). Not all future combinations have data — only months for which bookings exist at the time of the snapshot.