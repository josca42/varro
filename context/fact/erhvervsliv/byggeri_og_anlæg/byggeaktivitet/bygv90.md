table: fact.bygv90
description: Boliger i det samlede boligbyggeri (korrigeret for forsinkelser) efter byggefase, anvendelse og tid
measure: indhold (unit Antal)
columns:
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvendelse: join dim.byganv on anvendelse=kode::text [approx]; levels [2, 3]
- tid: date range 1998-01-01 to 2025-06-01
dim docs: /dim/byganv.md
notes:
- This is the delay-corrected (korrigeret) version of boligbyggeri (antal boliger) — no regional breakdown, no bygherre, no saeson. For the version with bygherre and seasonal adjustment use bygv99. For regional data use bygv33.
- anvendelse joins dim.byganv at niveauer 2 and 3. Code 'UOPL' is not in the dim.
- bygfase has 4 mutually exclusive phases — always filter to one when aggregating. Goes back to 1998.
