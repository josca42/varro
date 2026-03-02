table: fact.paaroe04
description: Befolkningen 1. januar efter relation, hovedpersonens alder og tid
measure: indhold (unit Antal)
columns:
- relation: values [TOT=Hele befolkningen, K00=Har ingen nære pårørende, K01=Har en partner, K02=Har børn, K03=Har forældre, K04=Har søskende, K05=Har en partner og børn, K06=Har en partner og forældre, K07=Har en partner og søskende, K08=Har børn og forældre, K09=Har børn og søskende, K10=Har forældre og søskende, K11=Har en partner, børn og forældre, K12=Har en partner, børn og søskende, K13=Har en partner, forældre og søskende, K14=Har børn, forældre og søskende, K15=Har en partner, børn, forældre og søskende]
- hoald: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- tid: date range 2020-01-01 to 2025-01-01

notes:
- relation codes K00–K15 are mutually exclusive combination categories (same as paaroe03). TOT = sum of all K rows. Safe to sum or compute shares.
- hoald uses broad age groups (Under 30, 30–39, … 70+) plus TOT. No individual year-ages. Use paaroe05 for single-year age granularity.
- No dim joins — no regional breakdown. Use paaroe03 if regional breakdown is needed.
- paaroe04 and paaroe03 are the same population but cross-tabulated differently: paaroe03 has region × relation, paaroe04 has age-group × relation.