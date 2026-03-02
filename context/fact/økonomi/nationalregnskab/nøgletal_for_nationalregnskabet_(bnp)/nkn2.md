table: fact.nkn2
description: Real disponibel bruttonationalindkomst mv. efter transaktion, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B1GQD=B.1*g Bruttonationalprodukt, BNP, B1GQRD=B.1*g Bruttonationalprodukt, BNP korrigeret for bytteforholdseffekt, D1A4N=D.1+D.4 Aflønning af ansatte og formueindkomst fra udlandet, netto, D2X3D=D.2-D.3  Produktions- og importskatter minus -subsidier fra udlandet, B5GQD=B.5*g Bruttonationalindkomst, BNI, D5_7N=D.5-D.7 Løbende overførsler fra udlandet, netto, B6GQD=B.6*g Disponibel bruttonationalindkomst, P51CD=P.51c Forbrug af fast realkapital, B1NQD=B.1*n Nettonationalprodukt, NNP, B5NQD=B.5*n Nettonationalindkomst, NNI, B6NQD=B.6*n Disponibel nettonationalindkomst]
- prisenhed: values [V=Løbende priser, RKV=2020-priser, real værdi]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01

notes:
- TWO measurement selectors — filter both prisenhed and saeson. Values: prisenhed IN ('V','RKV'), saeson IN ('Y','N'). Uses RKV (2020-priser kædede værdier) where nan2 uses RAN — same concept, different code.
- D1A4N, D2X3D, D5_7N only exist with prisenhed='V' (no real/chained version) — same constraint as nan2.
- Quarterly from 1990. Measure unit is Mio. kr. (not Mia. like nkn1).
- Sample query — disponibel bruttonationalindkomst kvartal, sæsonkorrigeret: SELECT tid, indhold FROM fact.nkn2 WHERE transakt='B6GQD' AND prisenhed='V' AND saeson='Y' ORDER BY tid