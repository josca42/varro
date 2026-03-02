table: fact.lbesk60
description: Lønmodtagere efter enhed, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 15=15 år, 16=16 år, 17=17 år ... 72=72 år, 73=73 år, 74=74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- alder has single-year age codes (15, 16, 17... 74) plus U15, 75OV, TOT, UDK — 75+ individual age values total. For age group analysis, aggregate with CASE in SQL (no pre-grouped dimension available). TOT and UDK should be excluded when summing individual ages.
- Filter kon (TOT sums genders) and alder (TOT sums all ages) as needed.
- Most granular age table in this subject (single years). For 5-year bands use lbesk43; for 10-year bands use lbesk67/lbesk68.
