table: fact.pris112
description: Forbrugerprisindeks efter hovedtal og tid
measure: indhold (unit Pct.)
columns:
- hoved: values [1005=Årsgennemsnit, 1010=Årsstigning]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- **hoved is a measurement selector** — hoved=1005 gives the annual average index level (values like 34.8 in 1980, ~130 in 2024), hoved=1010 gives the annual % change (inflation rate). Always filter to one hoved; the two series have different units and should never be mixed.
- Only 45 years × 2 series = 90 rows total. No dimension joins needed.
- Despite the unit label "Pct." in the metadata, hoved=1005 contains index values (not percentages). Only hoved=1010 is a true percentage.
- For monthly granularity use pris113; for data before 1980 use pris8 (annual index) or pris9 (annual % change).