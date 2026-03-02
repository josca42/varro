table: fact.gaslager
description: Naturgaslagre  (eksperimentel statistik) efter uger og tid
measure: indhold (unit TJ (terajoule))
columns:
- uger: values [U01=Uge 1, U02=Uge 2, U03=Uge 3, U04=Uge 4, U05=Uge 5 ... U49=Uge 49, U50=Uge 50, U51=Uge 51, U52=Uge 52, U53=Uge 53]
- tid: date range 2019-01-01 to 2025-01-01

notes:
- Two-dimensional time index: tid is the year (as a date, e.g. 2023-01-01) and uger is the week within that year (U01-U53). To select a specific calendar week use both: WHERE tid = '2023-01-01' AND uger = 'U10'.
- indhold is the gas storage level in TJ at that week — a stock measure (snapshot), not a flow. Do not sum across weeks.
- Experimental statistics (eksperimentel statistik) — subject to revision.
- Compare with gasbrug (same weekly structure) for storage vs. consumption context.