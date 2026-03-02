table: fact.foubud5
description: Finanslovens bevillinger til forskning og udvikling, mio. kr. efter forskningsformål , bevillingstype og tid
measure: indhold (unit Mio. kr.)
columns:
- forskformaal: values [10=Landbrug, skovbrug, jagt og fiskeri, 20=Minedrift, industri og håndværk, bygge- og anlægsvirksomhed og andre erhverv, 30=Produktion og fordeling af energi, 40=Transport og telekommunikation, 50=Boligforhold og fysisk planlægning ... 147=Almen videnskabelig udvikling - F og U som ikke kan fordeles på 14.1 til 14.6, 150=Rumforskning, 160=Forsvar, 199=Forskningsreserven, 200=I alt]
- bevilling1: values [1=I alt, 2=Basis, 3=Program]
- tid: date range 2007-01-01 to 2028-01-01
notes:
- bevilling1 is a selector column: 1=I alt, 2=Basis, 3=Program. Always filter to one value.
- forskformaal='200' = I alt (grand total). All other codes are sub-purposes. Same purpose coding as foubud1.
- No sektor breakdown (unlike foubud1). Also runs through 2028. Use this table when you need purpose × funding-type without sector detail.
