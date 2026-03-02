table: fact.pris9
description: Forbrugerprisindeks, gennemsnitlig årlig inflation efter type og tid
measure: indhold (unit Pct.)
columns:
- type: values [STIG=Årsstigning i procent]
- tid: date range 1901-01-01 to 2024-01-01

notes:
- Single-series table: type=STIG is the only value, no filtering needed.
- Annual average inflation rate (% change in CPI) from 1901. Complement to pris8 (the index level series).
- No dimension joins, no measurement-selector pitfalls. Just SELECT indhold, tid FROM fact.pris9.
- For the index level (not % change) use pris8; for monthly data use pris113.