table: fact.gasbrug
description: Naturgasforbrug ekskl. bionaturgas pr. uge (eksperimentel statistik) efter uger og tid
measure: indhold (unit TJ (terajoule))
columns:
- uger: values [U01=Uge 1, U02=Uge 2, U03=Uge 3, U04=Uge 4, U05=Uge 5 ... U49=Uge 49, U50=Uge 50, U51=Uge 51, U52=Uge 52, U53=Uge 53]
- tid: date range 2019-01-01 to 2025-01-01

notes:
- Two-dimensional time index: tid is the year and uger is the week (U01-U53). To select a specific week use both: WHERE tid = '2023-01-01' AND uger = 'U10'. To get annual total consumption: SUM(indhold) WHERE tid = '2023-01-01'.
- indhold is weekly gas consumption in TJ — a flow measure (per-week amount). Summing across all weeks in a year gives annual consumption.
- Excludes bionaturgas. Experimental statistics (eksperimentel statistik).
- Compare with gaslager (same weekly structure) for storage level context.