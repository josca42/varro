table: fact.energi3
description: Priser på naturgas for husholdningskunder efter årsforbrug, prisdefinition, energienhed og tid
measure: indhold (unit Kr. pr. enhed)
columns:
- aarsforbrug: values [23=Forbrug under 457 m3, 13=Forbrug 457 - 4.569 m3, 14=Forbrug 4.570 m3 og over]
- prisdefinition: values [20A=Pris hos energiselskab (niveau 0), 20=Pris inklusiv transmission og distribution (niveau 1), 21=Pris inklusiv faktiske afgifter (niveau 2), 22=Pris inklusiv afregnede afgifter og moms (niveau 3)]
- energienhed: values [M3=Kubikmeter (M3), GJ=Gigajoule (GJ)]
- tid: date range 2015-01-01 to 2025-01-01

notes:
- Natural gas prices for household consumers. Semi-annual data (January and July). Same column structure as energi1/energi2.
- prisdefinition is a cumulative price-component selector (20A→20→21→22). Filter to exactly one level; '22' gives the total consumer price incl. VAT. Never sum across prisdefinition values.
- energienhed is a unit selector: M3 (cubic metres) or GJ express the same price in different units. Filter to one — M3 is the natural unit for gas, GJ enables cross-fuel comparison. Never sum across energienhed values.
- aarsforbrug has only 3 consumption bands for households (23=under 457 m3, 13=457-4,569 m3, 14=4,570 m3+). No total band.
- Every (aarsforbrug, tid) combination has exactly 8 rows (4 prisdefinitioner × 2 energienheder). Always filter both.
- Sample query — household gas price (incl. VAT) in m3: SELECT aarsforbrug, tid, indhold FROM fact.energi3 WHERE prisdefinition = '22' AND energienhed = 'M3' ORDER BY tid, aarsforbrug;