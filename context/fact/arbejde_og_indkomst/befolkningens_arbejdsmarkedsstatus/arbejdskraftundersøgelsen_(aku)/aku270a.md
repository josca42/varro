table: fact.aku270a
description: Beskæftigede efter arbejde på atypiske tidspunkter, hyppighed, alder, køn og tid
measure: indhold (unit 1.000 personer)
columns:
- atyp: values [1=Aftenarbejde, 2=Natarbejde, 3=Lørdagsarbejde, 4=Søndagsarbejde]
- hyp: values [TOT=I alt, 1=Ja, mindst en gang inden for de sidste fire uger, 3=Nej, ikke inden for de sidste fire uger, 9=Uoplyst]
- alder: values [TOT=Alder i alt, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- atyp represents 4 independent types of atypical work (evening, night, Saturday, Sunday) — a person can work multiple types. NEVER sum across atyp values. Always filter to one type per query.
- hyp=TOT combines all responses for a given atyp — use hyp='TOT' for "how many worked [this type]", or hyp='1' for "worked at least once in last 4 weeks".
- alder (TOT + 5 bands) and koen (TOT + M + K) both have totals — filter to avoid overcounting. Annual data only (ends 2024).