table: fact.oeko4
description: Udenrigshandel med økologiske varer efter im- og eksport, varer og tid
measure: indhold (unit 1.000 kr.)
columns:
- indud: values [415=Import, 430=Eksport]
- vare: values [TOT=TOT I ALT, 001=001 Levende dyr, 011=011 Kød hornkvæg fersk, kølet el frosset, 012=012 Kød (undt af hornkvæg) og spiseligt slagteaffald fersk, kølet el frosset, 016=016 Kød og spiseligt slagteaffald,saltet,i saltlage,tørret el røget;mel og pulver af kød/slagteaf. ... 411=411 Animalske olier og fedtstoffer, 421=421 Vegetabilske olier og fedtstoffer; bløde, 422=422 Andre vegetabilske olier og fedtstoffer , 431=431 Animalske og vegetabilske olier og fedtstoffer og blandinger heraf, bearbejdede; voks, 500=500 Stivelse med mere]
- tid: date range 2003-01-01 to 2023-01-01

notes:
- indud uses non-standard codes: 415=Import, 430=Eksport (not 1/2 as used elsewhere). Don't confuse with other tables.
- vare is inline (no dim join). vare='TOT' is the all-products total. Individual codes follow a SITC-like scheme (3-digit, e.g. 001=Levende dyr, 011=Kød hornkvæg). Use ColumnValues("oeko4", "vare") to see all organic product categories.
- Annual data 2003–2023. Organic goods only. For trade by country see oeko55. For country+product breakdown see oeko66.