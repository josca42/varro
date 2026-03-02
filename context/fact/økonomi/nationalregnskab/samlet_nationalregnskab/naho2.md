table: fact.naho2
description: 1-2.1.1 Produktion, BNP og indkomstdannelse (oversigt) efter transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, B1GQD=B.1*g Bruttonationalprodukt, BNP, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, B2GD=B.2g Bruttooverskud af produktion, B3GD=B.3g Blandet bruttoindkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B2ND=B.2n Nettooverskud af produktion, B3ND=B.3n Blandet nettoindkomst, B1ND=B.1n Nettoværditilvækst, B1NQD=B.1*n Nettonationalprodukt, NNP]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector: V=løbende priser, LAN=2020-priser (kædede værdier). Filter to one value or row counts double.
- 'Oversigt' version from 1995 — has more transakt codes than nahl2 (e.g., B2GD and B3GD split out separately). For data back to 1966 use nahl2. For even more detail from 1995 use nahd21 + nahd22. Quarterly version: nkho2.
- Key codes: B1GQD=BNP, D1D=aflønning af ansatte.
