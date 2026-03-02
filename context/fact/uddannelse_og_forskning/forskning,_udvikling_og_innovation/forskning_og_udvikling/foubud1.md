table: fact.foubud1
description: Finanslovens bevillinger til forskning og udvikling, mio. kr. efter forskningsformål , sektor, bevillingstype og tid
measure: indhold (unit Mio. kr.)
columns:
- forskformaal: values [10=Landbrug, skovbrug, jagt og fiskeri, 20=Minedrift, industri og håndværk, bygge- og anlægsvirksomhed og andre erhverv, 30=Produktion og fordeling af energi, 40=Transport og telekommunikation, 50=Boligforhold og fysisk planlægning ... 147=Almen videnskabelig udvikling - F og U som ikke kan fordeles på 14.1 til 14.6, 150=Rumforskning, 160=Forsvar, 199=Forskningsreserven, 200=I alt]
- sektor: values [1=Universiteter m.v., 2=Forskningsrådene, 3=Internationale aktiviteter, 4=Andre større tilskudspuljer, 5=Forskningsinstitutioner, 6=Andet, 7=Forskningsreserven]
- bevilling1: values [1=I alt, 2=Basis, 3=Program]
- tid: date range 2007-01-01 to 2025-01-01
notes:
- bevilling1 is a selector column: 1=I alt, 2=Basis, 3=Program. Every sektor/forskformaal/tid combination appears 3×. Filter to bevilling1='1' for totals, or '2'/'3' to compare funding types.
- sektor has no total code (codes 1–7, where 7=Forskningsreserven with sparse data). Sum codes 1–6 (or 1–7) for a sektor total, but note there is no "I alt" sektor row in this table. Use foubud4 if you need sektor='9' (I alt).
- forskformaal='200' = I alt (grand total). All other codes are sub-purposes. The code numbering is not sequential and uses two-digit sub-codes (e.g., 141–147 for "Almen videnskabelig udvikling" sub-categories).
- This is the most detailed table: forskformaal × sektor × bevilling type. For simpler queries use foubud4 (sektor only) or foubud5 (forskformaal only).
