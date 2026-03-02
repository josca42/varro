table: fact.ligehi2
description: Ligestillingsindikator for middelrestlevetid for 50-årige efter indikator, familietype og tid
measure: indhold (unit -)
columns:
- indikator: values [M2=Mænd (år), K2=Kvinder (år), F2=Forskel mellem mænd og kvinder (år)]
- famtyp: values [FAMIALT=Familier i alt, ENL=Enlige, PAF=Parfamilier]
- tid: date range 1996 to 2025

notes:
- indhold is remaining life expectancy at age 50 (not at birth). Filter indikator to one value; F2 = M2 − K2 (negative, women live longer).
- famtyp and indikator are both cross-tabs — must filter each to one value to avoid overcounting. FAMIALT is the aggregate of ENL and PAF.
- tid is a 5-year rolling range (e.g. [2020,2025), [2019,2024), ...). Use lower(tid) for the start year.
- Example: remaining life expectancy at 50 for single men vs partnered men: SELECT famtyp, lower(tid), indhold FROM fact.ligehi2 WHERE indikator='M2' ORDER BY tid DESC, famtyp;
