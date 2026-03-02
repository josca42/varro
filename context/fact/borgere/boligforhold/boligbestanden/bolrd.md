table: fact.bolrd
description: Beboede boliger efter udlejningsforhold og tid
measure: indhold (unit Antal)
columns:
- udlforh: values [EJ=Beboet af ejer, LEJ=Beboet af lejer, UOPL=Uoplyst]
- tid: date range 1930-01-01 to 2025-01-01

notes:
- Simplest table in this subject: only udlforh and tid. National level only, no regional breakdown.
- udlforh has 3 values: EJ (ejer), LEJ (lejer), UOPL (uoplyst). No IB (ikke benyttet) unlike bol101/104. No aggregate/total code — SUM all three to get total beboede boliger.
- Historical series from 1930 — the only table in this subject covering pre-2010 data. Use it for long-term trend analysis of owner-occupied vs. rented dwellings.
- All rows are beboede boliger (occupied dwellings) by definition — the table description says "beboede boliger".