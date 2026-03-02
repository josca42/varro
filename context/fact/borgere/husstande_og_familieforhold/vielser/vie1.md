table: fact.vie1
description: Gennemsnitsalder for viede mænd og kvinder efter alder og tid
measure: indhold (unit -)
columns:
- alder: values [613=Gennemsnitsalder for 1. gangsviede mænd, 614=Gennemsnitsalder for 1. gangsviede kvinder, 615=Gennemsnitsalder for samtlige viede mænd, 616=Gennemsnitsalder for samtlige viede kvinder]
- tid: date range 1901-01-01 to 2024-01-01

notes:
- `alder` is a measurement selector, not a dimension. Each year has exactly 4 rows — one per code. Never sum across alder values; pick the one you want: 613=gennemsnitsalder 1. gangsviede mænd, 614=gennemsnitsalder 1. gangsviede kvinder, 615=gennemsnitsalder samtlige viede mænd, 616=gennemsnitsalder samtlige viede kvinder.
- `indhold` is an average age (decimal), not a count. Do not sum or aggregate it.
- This is the only table with historical data back to 1901 — useful for long time-series on marriage age trends.