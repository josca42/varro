table: fact.foubud5
description: Finanslovens bevillinger til forskning og udvikling, mio. kr. efter forskningsformål , bevillingstype og tid
measure: indhold (unit Mio. kr.)
columns:
- forskformaal: values [10=Landbrug, skovbrug, jagt og fiskeri, 20=Minedrift, industri og håndværk, bygge- og anlægsvirksomhed og andre erhverv, 30=Produktion og fordeling af energi, 40=Transport og telekommunikation, 50=Boligforhold og fysisk planlægning ... 147=Almen videnskabelig udvikling - F og U som ikke kan fordeles på 14.1 til 14.6, 150=Rumforskning, 160=Forsvar, 199=Forskningsreserven, 200=I alt]
- bevilling1: values [1=I alt, 2=Basis, 3=Program]
- tid: date range 2007-01-01 to 2028-01-01

notes:
- bevilling1: 1=I alt (total), 2=Basis, 3=Program. bevilling1=1 = 2+3. Don't include 1 when summing 2 and 3.
- forskformaal: hierarchical (200=I alt is grand total). Same NABS structure as foubud1.
- Extends to 2028 — years beyond current date are budget forecasts.
- No sektor breakdown. For sektor breakdown use foubud4 (by sektor only) or foubud1 (both sektor and formål).