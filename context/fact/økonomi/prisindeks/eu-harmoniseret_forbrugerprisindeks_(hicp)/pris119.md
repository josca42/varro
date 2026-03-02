table: fact.pris119
description: EU-harmoniseret forbrugerprisindeks efter hovedtal og tid
measure: indhold (unit Indeks)
columns:
- hoved: values [1005=Årsgennemsnit, 1010=Årsstigning]
- tid: date range 1996-01-01 to 2024-01-01

notes:
- Very simple table: only two series — annual average index (1005) and annual growth rate (1010). No product breakdown (unlike pris117/pris118 which have full ECOICOP detail).
- hoved is a measurement selector — every tid has 2 rows. Always filter: WHERE hoved = '1005' for the annual average, or WHERE hoved = '1010' for year-on-year growth.
- Data is annual only (tid is always YYYY-01-01) and stops at 2024 — more recent data requires pris117 (monthly, through 2025).
- Use this table for a quick single-number annual HICP series. For any breakdown by product category, use pris117 instead.