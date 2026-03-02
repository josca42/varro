table: fact.nahd22
description: 2.1.1 Indkomstdannelse (detaljeret) efter transaktion og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B1GQK=B.1*g Bruttonationalprodukt, BNP, D21X312D=D.21-D.31 Produktskatter minus produktsubsidier, B1GK=B.1g  Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, D29D=D.29 Andre produktionsskatter, D39D=D.39 Andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, D11D=D.11 Løn, D12D=D.12 Arbejdsgiverbidrag til sociale ordninger, D121D=D.121 Faktiske arbejdsgiverbidrag til sociale ordninger, D122D=D.122 Imputerede arbejdsgiverbidrag til sociale ordninger, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, B2GD=B.2g Bruttooverskud af produktion, B3GD=B.3g Blandet bruttoindkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B2ND=B.2n Nettooverskud af produktion, B3ND=B.3n Blandet nettoindkomst]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- No prisenhed column (løbende priser only). Single measure per transakt×tid.
- 'Detaljeret' indkomstdannelse (income generation) from 1995. Most granular breakdown of D.1 (løn + arbejdsgiverbidrag split by type) and B.2/B.3. Companion: nahd21 (produktion og BNP, has prisenhed).
- Key codes: D1D=aflønning af ansatte total, D11D=løn, D12D=arbejdsgiverbidrag.
