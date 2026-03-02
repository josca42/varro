table: fact.ror2
description: Investeringer i rørledningsnettet efter rørledningstype, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- ror: values [100=RØRLEDNINGER I ALT, 110=Naturgasrør (Transmissionssystemet), 142=Naturgasrør, nyinvesteringer, 145=Naturgasrør, vedligeholdelse, 150=OLIERØR, 225=Olierør, nyinvesteringer, 230=Olierør, vedligeholdese]
- enhed: values [2004=Årets priser, 1990=1990-priser, 1995=1995-priser, 2000=2000-priser]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- `enhed` is a price-base selector — every ror×tid combination is repeated for all 4 price bases (1990-priser, 1995-priser, 2000-priser, Årets priser). Always filter to one enhed or the sum is 4x too large. For current prices use enhed='2004'; for time-series comparisons pick a single fixed base year.
- `ror` has a 3-level hierarchy: 100=total; 110=gas and 150=oil are subtotals; 142=gas nyinvesteringer, 145=gas vedligeholdelse, 225=oil nyinvesteringer, 230=oil vedligeholdelse are leaf codes. Verified: 100=110+150 and 110=142+145. Never sum across levels.
- Oil pipeline investment data (ror 150, 225, 230) is only available through 2017. From 2018 onward ror=100 equals ror=110 (gas only). Restrict tid <= '2017-01-01' for oil-specific queries.
- Oil nyinvesteringer (ror=225) disappears after 2013 — from 2014-2017 only vedligeholdelse (230) is recorded for oil.