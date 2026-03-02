table: fact.strafna9
description: Skyldige personer efter køn, alder, herkomst og tid
measure: indhold (unit Antal)
columns:
- koen: values [M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15-29=15-29 år, 30-49=30-49 år, 50-79=50-79 år]
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2000-01-01 to 2023-01-01
notes:
- herkomst is hierarchical — 21=Indvandrere i alt is the sum of 24+25, and 31=Efterkommere i alt is the sum of 34+35. TOT=1+21+31. Must pick one consistent level to avoid double-counting: either {1, 21, 31} for top-level breakdown or {1, 24, 25, 34, 35} for the detailed split. Mixing levels inflates counts.
- koen has only M and K — no total row. Sum M+K for total.
- alder TOT is aggregate of the three age bands — filter to one level.
