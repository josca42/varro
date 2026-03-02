table: fact.kapit1
description: Kapitelstakster efter kapitelstakstområder, kornart og tid
measure: indhold (unit Kr. pr. 100 kg)
columns:
- kapit: values [000=Hele landet, 099=Sjælland med omliggende øer, 350X=Lolland-Falster med omliggende øer, 400=Bornholm, 420=Fyn med omliggende øer, 500=Sønderjylland, 600X=Østjylland, 550X=Vestjylland, 760X=Nordjylland]
- kornart: values [BYG=Byg, HVEDE=Hvede]
- tid: date range 1985-01-01 to 2024-01-01
notes:
- kapit uses 9 historical grain levy assessment areas (kapitelstakstområder), not standard administrative regions. These are DST-specific levy districts — code 000=Hele landet.
- kornart has only 2 values: BYG and HVEDE. Both are in the same table, so don't sum across kornart.
- Long series from 1985. Kapitelstakster (chapter rates) are historical reference prices used for agricultural land lease/taxation; they are not market prices.
