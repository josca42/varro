table: fact.oeko55
description: Udenrigshandel med økologiske varer efter im- og eksport, land og tid
measure: indhold (unit 1.000 kr.)
columns:
- indud: values [415=Import, 430=Eksport]
- land: join dim.lande_uhv on land=kode [approx]; levels [1, 4]
- tid: date range 2003-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md

notes:
- indud must always be filtered: 415=Import, 430=Eksport. Never sum across both.
- land mixes two hierarchy levels: niveau 1 (continents: 51=Europa, 52=Afrika, 53=Amerika, 54=Asien, 55=Oceanien og Polarregionerne) and niveau 4 (individual countries, ~107 ISO 2-letter codes). Filter WHERE d.niveau = 4 for individual countries, or WHERE d.niveau = 1 for continental aggregates. Mixing both doubles counts.
- TOT (total across all countries) is not in dim.lande_uhv — use WHERE land = 'TOT' directly, without a join, for the overall total.
- Use ColumnValues("lande_uhv", "titel", for_table="oeko55") to see only the ~112 land codes present in this table.