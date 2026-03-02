table: fact.ski55
description: Skilsmisseprocent efter enhed og tid
measure: indhold (unit Pct.)
columns:
- tal: values [5=Skilsmisseprocent (pct.)]
- tid: date range 1986-01-01 to 2024-01-01

notes:
- tal=5 is the only value in this table — every row is just "Skilsmisseprocent (pct.)". Filter WHERE tal='5' (or omit and GROUP BY tid).
- indhold is a divorce rate percentage, not a count. Never sum across years.
- Longest time series in this subject (1986–2024). Use for long-run trend of the divorce rate.