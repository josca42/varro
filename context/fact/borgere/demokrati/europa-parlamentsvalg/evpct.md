table: fact.evpct
description: Europa-Parlamentsvalg efter valgresultat og tid
measure: indhold (unit Pct.)
columns:
- valres: values [STEMPCT=Stemmeprocent, UGYLPCT=Ugyldighedsprocent, BREVPCT=Brevstemmeprocent]
- tid: date range 1979-01-01 to 2024-01-01

notes:
- National-level percentage rates only (no regional breakdown). Longest historical series: 1979–2024.
- The 3 valres values are independent rates: STEMPCT = voter turnout, UGYLPCT = invalid vote share, BREVPCT = postal vote share. Never sum them — each is a separate percentage.
- This is the go-to table for "hvad var stemmeprocenten til EP-valget i år X?"