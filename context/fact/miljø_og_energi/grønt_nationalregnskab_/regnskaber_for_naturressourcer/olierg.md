table: fact.olierg
description: Fysisk balance for oliereserverne efter balanceposter og tid
measure: indhold (unit Mio. m3)
columns:
- balpost: values [1=Primobeholdning (1), 11=Primobeholdning - heraf igangværende og besluttet indvinding, 12=Primobeholdning  - heraf planlagt indvinding, 13=Primobeholdning - heraf mulig indvinding, 2=Indvinding (nettoproduktion)(2), 3=Nye fund og anden økonomisk opståen (+)/forsvinden (-) (3), 4=Ultimoheholdning (4)=(1)-(2)+(3), 41=Ultimobeholdning - heraf igangværende og besluttet indvinding, 42=Ultimobeholdning - heraf planlagt udvinding, 43=Ultimobeholdning - heraf mulig indvinding]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- balpost codes form a hierarchy: codes 11/12/13 are sub-components of 1 (primobeholdning by readiness category); codes 41/42/43 are sub-components of 4 (ultimobeholdning). Never sum parent + children together.
- Accounting identity: 4 = 1 - 2 + 3. Do not sum all balpost codes.
- To get total reserves at year-end use balpost='4'. To get extraction use balpost='2'.
- Recent years show near-zero values as Danish oil reserves are close to exhaustion. Historical data peaks in the 1990s–2000s.