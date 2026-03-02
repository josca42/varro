table: fact.energi1
description: Priser på elektricitet for husholdningskunder efter årsforbrug, prisdefinition, energienhed og tid
measure: indhold (unit Kr. pr. enhed)
columns:
- aarsforbrug: values [1=Forbrug under 1 MWh, 2=Forbrug 1,0-2,4 MWh, 3=Forbrug 2,5 - 4,9 MWh, 4=Forbrug 5,0 - 14,9 MWh, 5=Forbrug 15,0 MWh og over]
- prisdefinition: values [20A=Pris hos energiselskab (niveau 0), 20=Pris inklusiv transmission og distribution (niveau 1), 21=Pris inklusiv faktiske afgifter (niveau 2), 22=Pris inklusiv afregnede afgifter og moms (niveau 3)]
- energienhed: values [KWH=Kilowatttimer (kWh), GJ=Gigajoule (GJ)]
- tid: date range 2015-01-01 to 2025-01-01

notes:
- Semi-annual data: January and July each year (21 periods from 2015H1 to 2025H1).
- prisdefinition is a cumulative price-component selector — each level adds more to the price. The 4 levels are: 20A (base energy price only), 20 (+ transmission/distribution), 21 (+ actual taxes), 22 (+ VAT, consumer-facing total price). Always filter to exactly one level. For the consumer-paid price, use '22'. Never sum across prisdefinition values.
- energienhed is a unit selector: KWH and GJ express the same price in different units. Filter to one unit (KWH is most common for electricity). Never sum across energienhed values.
- aarsforbrug splits consumers into 5 annual consumption bands (1=under 1 MWh … 5=15 MWh+). These are not a hierarchy — there is no total band. Each row represents a different consumer segment; comparing across bands is valid, summing is not.
- Every (aarsforbrug, tid) combination has exactly 8 rows (4 prisdefinitioner × 2 energienheder). A typical query must filter both: WHERE prisdefinition = '22' AND energienhed = 'KWH'.
- Sample query — consumer electricity price (incl. VAT) in kWh by consumption band over time: SELECT aarsforbrug, tid, indhold FROM fact.energi1 WHERE prisdefinition = '22' AND energienhed = 'KWH' ORDER BY tid, aarsforbrug;