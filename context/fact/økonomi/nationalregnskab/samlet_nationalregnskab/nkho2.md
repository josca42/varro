table: fact.nkho2
description: 1-2.1.1 Produktion, BNP og indkomstdannelse efter transaktion, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, B1GQD=B.1*g Bruttonationalprodukt, BNP, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B1ND=B.1n Nettoværditilvækst, B1NQD=B.1*n Nettonationalprodukt, NNP]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- TWO measurement selectors: prisenhed (V/LKV) and saeson (N/Y). Always filter both or row counts quadruple.
- Quarterly BNP/production/indkomstdannelse from 1990. Annual equivalent: nahl2 (hoved) or naho2 (oversigt).
- Key codes: B1GQD=BNP, D1D=aflønning af ansatte, B2A3GD=bruttooverskud og blandet indkomst.
