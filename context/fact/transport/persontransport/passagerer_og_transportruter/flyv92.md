table: fact.flyv92
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne efter transporttype, flyvning og tid
measure: indhold (unit 1.000 personer)
columns:
- transport: values [0=I alt, 15=National, 25=International]
- flyvning: values [20080=Flyvninger i alt, 20085=Ruteflyvninger, 20090=Charter/taxi flyvning, 20095=Anden flyvning]
- tid: date range 2001-01-01 to 2025-06-01

notes:
- Simplest current-data fly table: departing passengers across all airports combined, by transport type and flight type. Monthly data through 2025.
- transport=0 and flyvning=20080 are totals — filter to one value per column to avoid double-counting.
- No airport dimension — use flyv91 or flyv32 when airport breakdown is needed.
- For seasonally adjusted monthly figures, use flyv93 (identical structure).
