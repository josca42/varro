table: fact.flyv93
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne (sæsonkorrigeret) efter transporttype, flyvning og tid
measure: indhold (unit 1.000 personer)
columns:
- transport: values [0=I alt, 15=National, 25=International]
- flyvning: values [20080=Flyvninger i alt, 20085=Ruteflyvninger, 20090=Charter/taxi flyvning, 20095=Anden flyvning]
- tid: date range 2001-01-01 to 2025-06-01

notes:
- Seasonally adjusted version of flyv92 — identical structure and codes, but values are corrected for seasonal variation. Use for trend analysis; do not use for actual annual totals.
- transport=0 and flyvning=20080 are aggregate totals — filter to one value per column.
- For unadjusted monthly figures use flyv92.
