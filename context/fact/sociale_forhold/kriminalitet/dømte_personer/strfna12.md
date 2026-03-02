table: fact.strfna12
description: Skyldige personer efter køn, alder, herkomst, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15-29=15-29 år, 30-49=30-49 år, 50-79=50-79 år]
- herkomst: values [5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere]
- statsb: values [DANSK=Dansk, VEST=Vestligt, IKKEVEST=Ikke-vestligt]
- tid: date range 2018-01-01 to 2023-01-01
notes:
- koen has TOT=I alt (unlike most other tables in this subject which have only M and K). Filter koen='TOT' for totals or M/K for gender breakdown.
- alder TOT is the aggregate of the three age bands — filter to one level.
- herkomst: simplified 3-way split (5=dansk oprindelse, 4=Indvandrere, 3=Efterkommere) — no total, no sub-categories. Different coding than strafna9/strfna10/strfna11 (which use 1/21/31). Sum all 3 for total.
- statsb: 3 values (DANSK, VEST, IKKEVEST) — no total. Sum all 3 for total.
- 4 non-tid dimensions: for a simple total count filter koen='TOT', alder='TOT', then aggregate or filter herkomst and statsb as needed.
