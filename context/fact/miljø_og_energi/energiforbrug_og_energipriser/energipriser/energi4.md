table: fact.energi4
description: Priser på naturgas for erhvervskunder efter årsforbrug, prisdefinition, energienhed og tid
measure: indhold (unit Kr. pr. enhed)
columns:
- aarsforbrug: values [15=Forbrug under 22.849 m3, 16=Forbrug 22.849 - 228.489 m3, 17=Forbrug 228.490 - 2.284.899 m3, 18=Forbrug 2.284.900 - 22.848.999 m3, 19=Forbrug 22.849.000 - 91.395.999 m3]
- prisdefinition: values [20A=Pris hos energiselskab (niveau 0), 20=Pris inklusiv transmission og distribution (niveau 1), 21=Pris inklusiv faktiske afgifter (niveau 2), 22=Pris inklusiv afregnede afgifter og moms (niveau 3)]
- energienhed: values [M3=Kubikmeter (M3), GJ=Gigajoule (GJ)]
- tid: date range 2015-01-01 to 2025-01-01

notes:
- Natural gas prices for business/commercial consumers. Semi-annual data (January and July). Same column structure as energi3.
- prisdefinition is a cumulative price-component selector (20A→20→21→22). Filter to exactly one level; '22' gives the total price incl. VAT. Never sum across prisdefinition values.
- energienhed is a unit selector: M3 or GJ. Filter to one — M3 is natural for gas, GJ enables cross-fuel comparison. Never sum across energienhed values.
- aarsforbrug has 5 commercial consumption bands (15=under 22,849 m3 … 19=22,849,000-91,395,999 m3). These are very large volumes — commercial/industrial scale. No total band.
- Every (aarsforbrug, tid) combination has exactly 8 rows (4 × 2). Always filter both prisdefinition and energienhed.
- Sample query — business gas price (incl. VAT) in m3: SELECT aarsforbrug, tid, indhold FROM fact.energi4 WHERE prisdefinition = '22' AND energienhed = 'M3' ORDER BY tid, aarsforbrug;