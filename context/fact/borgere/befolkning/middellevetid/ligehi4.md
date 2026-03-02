table: fact.ligehi4
description: Ligestillingsindikator for middelrestlevetid for 30-årige efter indikator, højest fuldførte uddannelse og tid
measure: indhold (unit -)
columns:
- indikator: values [M2=Mænd (år), K2=Kvinder (år), F2=Forskel mellem mænd og kvinder (år)]
- hfudd: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H70=H70 Lange videregående uddannelser, LVU]
- tid: date range 2012 to 2025

notes:
- indhold is remaining life expectancy at age 30. Filter indikator to one value; F2 = M2 − K2 (negative, women live longer).
- hfudd and indikator are both cross-tabs — must filter each to one value to avoid overcounting. TOT is the aggregate across all education levels.
- tid is a 5-year rolling range (e.g. [2020,2025), [2019,2024), ...). Use lower(tid) for the start year. Shortest series in this subject (2012+).
- Education groups go from H10 (grundskole) to H70 (lange videregående). H40/H50/H70 labels include verbose Danish acronyms (KVU/MVU/LVU) — match by code, not label substring.
- Example: life expectancy gap by education for most recent period: SELECT hfudd, indhold FROM fact.ligehi4 WHERE indikator='F2' AND lower(tid)=2020 ORDER BY hfudd;
