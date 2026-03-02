table: fact.foubud4
description: Finanslovens bevillinger til forskning og udvikling, mio. kr. efter sektor, bevillingstype og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [1=Universiteter m.v., 2=Forskningsrådene, 3=Internationale aktiviteter, 4=Andre større tilskudspuljer, 5=Forskningsinstitutioner, 6=Andet, 7=Forskningsreserven, 9=I alt]
- bevilling1: values [1=I alt, 2=Basis, 3=Program]
- tid: date range 2007-01-01 to 2028-01-01
notes:
- bevilling1 is a selector column: 1=I alt, 2=Basis, 3=Program. Always filter to one value.
- sektor='9' = I alt (grand total). Codes 1–7 are sub-sectors (7=Forskningsreserven has sparse data in recent years).
- Longest future horizon in this subject: data runs through 2028 (budget projections). Use this table for multi-year budget forecasts.
- For breakdown by research purpose, use foubud1 or foubud5.
