table: fact.dod2
description: Døde under 5 år efter køn, alder og tid
measure: indhold (unit Antal)
columns:
- kon: values [D=Drenge, P=Piger]
- alder: values [U1=Under 1 år, 1-4=1-4 år]
- tid: date range 1901-01-01 to 2024-01-01

notes:
- Restricted to children under 5 only. Only 4 combinations: kon (D=Drenge, P=Piger) × alder (U1=under 1 år, 1-4=1-4 år). No total rows for either column — safe to SUM all rows for a year to get total under-5 deaths.
- Longest historical series in this subject: goes back to 1901. Use for child mortality trends.
- kon uses D/P (not M/K or 1/2) — note the different coding from other tables in this subject.