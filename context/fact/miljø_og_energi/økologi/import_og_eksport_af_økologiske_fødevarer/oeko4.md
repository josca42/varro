table: fact.oeko4
description: Udenrigshandel med økologiske varer efter im- og eksport, varer og tid
measure: indhold (unit 1.000 kr.)
columns:
- indud: values [415=Import, 430=Eksport]
- vare: values [TOT=TOT I ALT, 001=001 Levende dyr, 011=011 Kød hornkvæg fersk, kølet el frosset, 012=012 Kød (undt af hornkvæg) og spiseligt slagteaffald fersk, kølet el frosset, 016=016 Kød og spiseligt slagteaffald,saltet,i saltlage,tørret el røget;mel og pulver af kød/slagteaf. ... 411=411 Animalske olier og fedtstoffer, 421=421 Vegetabilske olier og fedtstoffer; bløde, 422=422 Andre vegetabilske olier og fedtstoffer , 431=431 Animalske og vegetabilske olier og fedtstoffer og blandinger heraf, bearbejdede; voks, 500=500 Stivelse med mere]
- tid: date range 2003-01-01 to 2023-01-01

notes:
- indud must always be filtered: 415=Import, 430=Eksport. Never sum across both.
- vare has 47 inline 3-digit product codes + TOT (I ALT = total all goods). These look like SITC codes but do NOT match dim.sitc — no dim join is possible. Use exact vare code to filter or use TOT for the overall total.
- To get total import or export across all goods: WHERE indud=415 (or 430) AND vare='TOT'.
- For a specific commodity, filter by the 3-digit vare code (e.g. vare='011' for beef). Use ColumnValues("oeko4", "vare") to browse all codes with labels.