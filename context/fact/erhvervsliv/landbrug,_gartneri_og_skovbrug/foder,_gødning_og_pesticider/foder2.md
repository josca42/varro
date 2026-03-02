table: fact.foder2
description: Fordeling af foder efter fodermiddel, anvendelse og tid
measure: indhold (unit Mio. kg)
columns:
- foder2: values [5=Foderforbrug i alt, 10=Kraftfoderforbrug i alt, 15=Korn til foder i alt, 20=Hvede, 25=Rug ... 195=Korn, helsædsensilage, 200=Græs og kløver i omdriften, 205=Græs og kløver udenfor omdriften, 210=Andet grøntfoder, 215=Halm]
- vandty: values [FB=I foderblandinger, EF=Som enkeltfoderstof, 1=I alt]
- tid: date range 1992-01-01 to 2024-01-01

notes:
- vandty: 1=I alt, FB=I foderblandinger, EF=Som enkeltfoderstof. Code 1 is the total of FB+EF. Filter to `vandty='1'` for total or FB/EF for the breakdown — do not sum all three.
- foder2 has the same hierarchical codes as foder1 (starting at 10, no code 5 grand total here). Code 10=Kraftfoderforbrug i alt and 15=Korn til foder i alt are subtotals; codes 20–215 are individual commodities. Do not mix hierarchy levels in a sum.
- This table is simpler than foder1: unit is always Mio. kg, no origin split. Use it when you just need feed distribution by usage type (foderblandinger vs enkeltfoderstof).