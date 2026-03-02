table: fact.aku240k
description: Beskæftigede med normal arbejdstid efter arbejdstid, alder, køn og tid
measure: indhold (unit 1.000 personer)
columns:
- arbejdstid: values [<15=1-14 timer, 15-36=15-36 timer, 37=37 timer, 38-48=38-48 timer, >48=49-97 timer, UOPLYST=Uoplyst]
- alder: values [TOT=Alder i alt, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2025-04-01

notes:
- arbejdstid values are mutually exclusive hour bands (no total row) — summing across all bands gives total employed. Filter to a specific band or group bands with a CASE expression.
- alder (TOT + 5 bands) and kon (TOT + M + K) have totals — filter to alder='TOT', kon='TOT' for national totals.
- Quarterly data. For average hours (not distribution) use aku410a instead.