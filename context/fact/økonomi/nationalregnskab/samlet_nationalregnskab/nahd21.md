table: fact.nahd21
description: 1 Produktion og BNP (detaljeret) efter transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P11K=P.11 Markedsmæssig produktion, P12K=P.12 Produktion til eget brug, P13K=P.13 ikke-markedsmæssig produktion, P131K=P.131 Betaling for ikke-markedsmæssig produktion, P132K=P.132 Anden ikke-markedsmæssig produktion, P11A12A131K=P.11+P.12+P.131 Markedsmæssig produktion, produktion til eget brug samt betaling for ikke-markedsmæssig produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, D21D=D.21 Produktskatter, D211D=D.211 Moms, D2121D=D.2121 Told mv., D2124D=D.2122+D.214 Øvrige produktskatter, D31D=D.31 Produktsubsidier, B1GQD=B.1*g Bruttonationalprodukt, BNP, P51CD=P.51c Forbrug af fast realkapital, B1ND=B.1n Nettoværditilvækst, B1NQD=B.1*n Nettonationalprodukt, NNP]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector: V=løbende priser, LAN=2020-priser (kædede værdier). Filter to one value or row counts double.
- 'Detaljeret' production/BNP table from 1995 — has the most transakt codes of the production tables (includes full breakdown of P.1, D.21, D.31 etc.). Less detail back in time: nahl2/naho2 go to 1966/1995 with fewer codes.
- Companion table: nahd22 covers indkomstdannelse (same period, no prisenhed).
