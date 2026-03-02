table: fact.foubud4
description: Finanslovens bevillinger til forskning og udvikling, mio. kr. efter sektor, bevillingstype og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [1=Universiteter m.v., 2=Forskningsrådene, 3=Internationale aktiviteter, 4=Andre større tilskudspuljer, 5=Forskningsinstitutioner, 6=Andet, 7=Forskningsreserven, 9=I alt]
- bevilling1: values [1=I alt, 2=Basis, 3=Program]
- tid: date range 2007-01-01 to 2028-01-01

notes:
- bevilling1: 1=I alt (total), 2=Basis, 3=Program. bevilling1=1 = bevilling1=2 + bevilling1=3. Don't include 1 when summing 2 and 3.
- sektor: 1–7 are detailed sectors, 9=I alt is the aggregate total. Don't sum 9 with 1–7.
- Extends to 2028 — years after current date are budget forecasts (finanslovsbevillinger), not actuals.
- Annual. For breakdown by forskningsformål, use foubud5 or foubud1.