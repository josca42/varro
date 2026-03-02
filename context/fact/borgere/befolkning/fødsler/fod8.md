table: fact.fod8
description: Enkelt- og flerfødsler efter fødselstype og tid
measure: indhold (unit Antal)
columns:
- fodtype: values [9=Enkeltfødsler, 10=Tvillingefødsler, 122=Trillinge- og firlingefødsler]
- tid: date range 1850-01-01 to 2023-01-01
notes:
- fodtype counts birth EVENTS (deliveries), not babies. A twin delivery is 1 event producing 2 children. Sum all 3 fodtype values for total deliveries; total live births = Enkeltfødsler*1 + Tvillingefødsler*2 + Trillinge/firlingefødsler*3+.
- Longest historical series in the subject: goes back to 1850. For gender breakdown of twin births, see fod9.
