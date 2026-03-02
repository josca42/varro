table: fact.foubud1
description: Finanslovens bevillinger til forskning og udvikling, mio. kr. efter forskningsformål , sektor, bevillingstype og tid
measure: indhold (unit Mio. kr.)
columns:
- forskformaal: values [10=Landbrug, skovbrug, jagt og fiskeri, 20=Minedrift, industri og håndværk, bygge- og anlægsvirksomhed og andre erhverv, 30=Produktion og fordeling af energi, 40=Transport og telekommunikation, 50=Boligforhold og fysisk planlægning ... 147=Almen videnskabelig udvikling - F og U som ikke kan fordeles på 14.1 til 14.6, 150=Rumforskning, 160=Forsvar, 199=Forskningsreserven, 200=I alt]
- sektor: values [1=Universiteter m.v., 2=Forskningsrådene, 3=Internationale aktiviteter, 4=Andre større tilskudspuljer, 5=Forskningsinstitutioner, 6=Andet, 7=Forskningsreserven]
- bevilling1: values [1=I alt, 2=Basis, 3=Program]
- tid: date range 2007-01-01 to 2025-01-01

notes:
- bevilling1: 1=I alt is the total, 2=Basis and 3=Program are the two components. bevilling1=1 exactly equals bevilling1=2 + bevilling1=3. Never include bevilling1=1 when summing 2 and 3.
- forskformaal: hierarchical. 200=I alt is the grand total. Sub-codes are numbered by NABS classification (10=landbrug, 20=minedrift, ..., 160=forsvar, etc.). Use ColumnValues("foubud1", "forskformaal") to browse all values.
- sektor: 7 additive sectors (1=Universiteter, 2=Forskningsråd, ..., 7=Forskningsreserven). These appear to be non-overlapping — summing all gives the total. Sektor 7=Forskningsreserven only applies to bevilling1=3 (program).
- Annual (2007–2025). For sector-only breakdown without forskformaal, use foubud4; for formål-only without sektor, use foubud5.