table: fact.nan2
description: Real disponibel bruttonationalindkomst mv. efter transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B1GQD=B.1*g Bruttonationalprodukt, BNP, B1GQRD=B.1*g Bruttonationalprodukt, BNP korrigeret for bytteforholdseffekt, D1A4N=D.1+D.4 Aflønning af ansatte og formueindkomst fra udlandet, netto, D2X3D=D.2-D.3  Produktions- og importskatter minus -subsidier fra udlandet, B5GQD=B.5*g Bruttonationalindkomst, BNI, D5_7N=D.5-D.7 Løbende overførsler fra udlandet, netto, B6GQD=B.6*g Disponibel bruttonationalindkomst, P51CD=P.51c Forbrug af fast realkapital, B1NQD=B.1*n Nettonationalprodukt, NNP, B5NQD=B.5*n Nettonationalindkomst, NNI, B6NQD=B.6*n Disponibel nettonationalindkomst]
- prisenhed: values [V=Løbende priser, RAN=2020-priser, real værdi]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- prisenhed is a MEASUREMENT SELECTOR — always filter to one value: V (løbende priser) or RAN (2020-priser, real værdi). The measure unit is Mio. kr. (not Mia. like nan1).
- D1A4N, D2X3D, D5_7N only exist with prisenhed='V' (no real/chained price version for these flow transactions).
- 18 transakt codes covering BNP, BNI, available income (B6GQD), net national product/income, and cross-border income flows. Use ColumnValues("nan2", "transakt") to browse.
- Covers the income approach to national accounts (from BNP → BNI → disponibel indkomst). nan1 covers the expenditure approach.
- Sample query — disponibel bruttonationalindkomst i løbende priser: SELECT tid, indhold FROM fact.nan2 WHERE transakt='B6GQD' AND prisenhed='V' ORDER BY tid