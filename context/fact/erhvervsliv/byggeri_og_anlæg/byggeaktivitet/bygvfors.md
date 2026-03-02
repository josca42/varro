table: fact.bygvfors
description: Ændring i indberetninger fra første til seneste indberetning efter byggefase og tid
measure: indhold (unit Pct.)
columns:
- bygfase: values [10=Boliger, påbegyndt, 11=Boliger, fuldført, 12=Etageareal. påbegyndt, 13=Etageareal, fuldført]
- tid: date range 2006-01-01 to 2025-04-01
notes:
- indhold is a percentage (Pct.) showing the revision from first to latest report — not a construction volume. Do not sum or aggregate these values across time.
- bygfase uses 4 distinct codes (10-13) covering boliger/etageareal × påbegyndt/fuldført. These do not match the bygfase codes (1-4) in other tables.
- Useful only for understanding data quality and reporting lag; not for construction volume analysis.
