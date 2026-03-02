table: fact.oliepris
description: Gennemsnitlig pris på nordsøolie efter enhed og tid
measure: indhold (unit USD)
columns:
- enhed: values [OLIE=Gennemsnitlig oliepris per tønde]
- tid: date range 2022-01-01 to 2024-01-01

notes:
- Extremely small table: only 3 rows (one per year, 2022–2024). Annual frequency.
- enhed='OLIE' is a constant label — not a selector. Every query should include it but there is no choice to make; it simply means the measure is average North Sea crude oil price per barrel in USD.
- No filtering traps: each row is a unique (enhed, tid) pair with a single indhold value.
- Use for context or cross-referencing when analysing Danish energy prices. Very limited time coverage (only 3 years).