table: fact.nahl2
description: 1-2.1.1 Produktion, BNP og indkomstdannelse (hovedposter) efter transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, B1GQD=B.1*g Bruttonationalprodukt, BNP, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B1ND=B.1n Nettoværditilvækst, B1NQD=B.1*n Nettonationalprodukt, NNP]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector: V=løbende priser, LAN=2020-priser (kædede værdier). Filter to one value or row counts double.
- transakt codes are national accounts aggregates (BNP, BVT, BNI etc.) — not additive across all transakt values. Key codes: B1GQD=BNP, B1GD=Bruttoværditilvækst, D1D=aflønning af ansatte.
- 'Hoved' (main posts) version from 1966. naho2 has slightly more detail from 1995. Quarterly version with saeson: nkho2.
