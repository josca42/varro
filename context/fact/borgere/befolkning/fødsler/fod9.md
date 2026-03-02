table: fact.fod9
description: Tvillingefødsler fordelt efter fødselstype og tid
measure: indhold (unit Antal)
columns:
- fodtype: values [13=Tvillingefødsler 2 drenge, 14=Tvillingefødsler  1 dreng og 1 pige, 15=Tvillingefødsler 2 piger, 16=Tvillingefødsler køn uoplyst]
- tid: date range 1911-01-01 to 2023-01-01
notes:
- fodtype has 4 mutually exclusive twin birth sub-types (2 drenge, 1 dreng+1 pige, 2 piger, køn uoplyst). Sum of all 4 equals total twin deliveries — the same count as fodtype=10 in fod8.
- indhold counts twin birth EVENTS, not babies (each event produces 2 children).
