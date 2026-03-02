table: fact.aku410a
description: Gennemsnitlig ugentlig arbejdstid i hovedjob efter arbejdstid, alder, køn og tid
measure: indhold (unit Timer)
columns:
- arbejdstid: values [2=Normal ugentlig arbejdstid, 1-95 timer, 12=Faktisk ugentlig arbejdstid, 0-95 timer (inkl. fuld fravær i referenceugen), 22=Faktisk ugentlig arbejdstid, 1-95 timer (mindst en times arbejde i referenceugen)]
- alder: values [TOT=Alder i alt, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- arbejdstid has 3 distinct measurement types — always filter to exactly one: 2=normal contractual hours (most stable for comparisons), 12=actual hours (includes full-absence weeks with 0 hours), 22=actual hours excluding full-absence weeks. Never sum or average across types.
- alder (TOT + 5 bands) and koen (TOT + M + K) both have totals — filter to alder='TOT', koen='TOT' for a national average.
- Annual data only (ends 2024). For hours by industry instead of age/gender, use aku420a.