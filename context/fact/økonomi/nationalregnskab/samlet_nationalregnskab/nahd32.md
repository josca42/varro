table: fact.nahd32
description: 2.2 Fordeling af sekundær indkomst (detaljeret) efter transaktion og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B5GQK=B.5*g Bruttonationalindkomst, BNI, D5_7K=D.5-D.7 Modtaget løbende overførsler, D5K=D.5 Modtaget løbende indkomst- og formueskatter mv., D61K=D.61 Modtaget nettobidrag til sociale ordninger, D611K=D.611 Modtaget faktiske arbejdsgiverbidrag til sociale ordninger ... D75D=D.75 Betalt diverse løbende overførsler, D76D=D.76 Betalt moms- og BNI-baserede egne EU-indtægter, TP=I alt bruttoudgifter, B6GQD=B.6*g Disponibel bruttonationalindkomst, B6NQD=B.6*n Disponibel nettonationalindkomst]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- No prisenhed column (løbende priser only). Single measure per transakt×tid.
- 'Detaljeret' secondary income distribution from 1995 — covers D.5 (skatter), D.6 (sociale bidrag/ydelser), D.7 (andre løbende overførsler), plus EU egne indtægter. Key output: B6GQD=disponibel bruttonationalindkomst.
- TP='I alt bruttoudgifter' is the total of all payments — do not sum with the individual D-codes as that double-counts.
