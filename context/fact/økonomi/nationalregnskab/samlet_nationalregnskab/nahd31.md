table: fact.nahd31
description: 2.1.2 Allokering af primær indkomst (detaljeret) efter transaktion og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, B2GK=B.2g Bruttooverskud af produktionen, B3GK=B.3g Blandet bruttoindkomst, D1K=D.1 Modtaget aflønning af ansatte, D11K=D.11 Modtaget løn ... D442D=D.442 Betalt formueindkomst henført til pensionsopsparere, D443D=D.443 Betalt investeringsindkomst henført til ejere af kapitalandele i kollektive investeringsforeninger, B5GQD=B.5*g Bruttonationalindkomst, BNI, P51C1D=P.51c Forbrug af fast realkapital, B5NQD=B.5*n Nettonationalindkomst, NNI]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- No prisenhed column (løbende priser only). Single measure per transakt×tid.
- 'Detaljeret' primary income allocation from 1995 — most granular breakdown of formueindkomst (D.4) received and paid. Key output: B5GQD=BNI (Bruttonationalindkomst). Oversigt version: naho3.
- transakt codes flow from B2A3GK through D.4 components to B5GQD — these are accounting stages, not independent additive items.
