table: fact.energi2
description: Priser på elektricitet for erhvervskunder efter årsforbrug, prisdefinition, energienhed og tid
measure: indhold (unit Kr. pr. enhed)
columns:
- aarsforbrug: values [6=Forbrug under 20 MWh, 7=Forbrug 20 - 499 MWh, 8=Forbrug 500 - 1.999 MWh, 9=Forbrug 2.000 - 19.999 MWh, 10=Forbrug 20.000 - 69.999 MWh, 11=Forbrug 70.000 - 149.999 MWh, 12=Forbrug 150.000 MWh og over]
- prisdefinition: values [20A=Pris hos energiselskab (niveau 0), 20=Pris inklusiv transmission og distribution (niveau 1), 21=Pris inklusiv faktiske afgifter (niveau 2), 22=Pris inklusiv afregnede afgifter og moms (niveau 3)]
- energienhed: values [KWH=Kilowatttimer (kWh), GJ=Gigajoule (GJ)]
- tid: date range 2015-01-01 to 2025-01-01

notes:
- Same structure as energi1 but for business/commercial electricity customers. Semi-annual data (January and July).
- prisdefinition is a cumulative price-component selector (20A→20→21→22). Filter to exactly one level; '22' gives the full consumer price incl. VAT. Never sum across prisdefinition values.
- energienhed is a unit selector: KWH or GJ express the same price in different units. Filter to one (KWH is standard for electricity). Never sum across energienhed values.
- aarsforbrug has 7 commercial consumption bands (6=under 20 MWh … 12=150,000 MWh+), with no total band. Business consumers at different scales pay different prices; comparing bands is valid, summing is not.
- Every (aarsforbrug, tid) combination has exactly 8 rows (4 × 2). Always filter both prisdefinition and energienhed.
- Sample query — business electricity price (incl. VAT) in kWh: SELECT aarsforbrug, tid, indhold FROM fact.energi2 WHERE prisdefinition = '22' AND energienhed = 'KWH' ORDER BY tid, aarsforbrug;