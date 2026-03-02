table: fact.kv2mks2
description: Udøvelse af musik efter måde, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- musm: values [42120=Spiller et instrument, 42130=Synger i kor, 42140=Synger i band eller ensemble, 42150=Synger som solist eller forsanger, 42160=Skriver eller komponerer musik, 42170=Skaber eller producerer musik fx på computer el.lign., 42180=Rapper, 42190=DJer, 42200=Skriver tekster, 42210=Anden udøvelse]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Single survey year (2024) — no time series.
- indhold is a percentage (Pct.). musm categories are multi-select (survey respondents could tick multiple boxes). Categories sum to ~60 for kon=10/alder='TOT', NOT 100. Never sum across musm — it produces a meaningless total.
- Each row is an independent rate: "X% of respondents play music in this particular way." E.g., 13% play an instrument, 6% sing in a choir — these are not mutually exclusive, one person can do both.
- "Anden udøvelse" (42210) catches all unlisted methods at 27% — the largest single category. Do not over-interpret this.
- To know the overall share who play music in any way, use kv2mks1 and exclude the non-participation codes (111000, 111100, 111200).
- Filter to kon=10 AND alder='TOT' for population totals. Omitting these inflates results by ~3× (3 kon × 8 alder values).