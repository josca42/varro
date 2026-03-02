table: fact.pris115
description: Nettoprisindeks efter hovedtal og tid
measure: indhold (unit Indeks)
columns:
- hoved: values [1005=Årsgennemsnit, 1010=Årsstigning]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- hoved is a measurement selector — each tid has 2 rows. Filter to one: hoved=1005 for the annual average index level, hoved=1010 for the annual rate of change (pct.). Mixing them makes sums meaningless.
- This is the headline aggregate NPI only — no product-group breakdown. 45 annual observations per hoved value (1980–2024).
- For monthly frequency (same headline aggregate), use pris116. For product-group breakdown, use pris114.