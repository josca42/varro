table: fact.fiks9
description: Firmaernes køb og salg, historisk sammendrag efter beløb og tid
measure: indhold (unit Mio. kr.)
columns:
- belob: values [4=Salg i alt, 1=Indenlandsk salg, 3=Køb i alt, 0=Indenlandsk køb, 5=Antal virksomheder]
- tid: date range 1969-01-01 to 2024-01-01

notes:
- Annual historical summary from 1969 — the longest time series in this subject. No branche breakdown.
- belob is a measurement selector: pick one per query. Unique to this table: belob=5 gives Antal virksomheder (number of firms) rather than a financial amount. Do not sum across belob values.
- Simple two-column query: SELECT tid, indhold FROM fact.fiks9 WHERE belob='4' ORDER BY tid for total annual sales.