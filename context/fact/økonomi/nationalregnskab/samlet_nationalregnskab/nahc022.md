table: fact.nahc022
description: Husholdningers forbrug på dansk område (44 grp) efter formål, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- formaaal: values [CPT=I alt, CP0113=Fødevarer mv., CP0120=Ikke-alkoholiske drikkevarer, CP0212=Alkoholiske drikkevarer, CP0290=Tobak mv. ... CP1220=Finansielle tjenesteydelser, CP1310=Toiletartikler, barbermask.mv, frisører, CP1320=Andre personlige artikler, CP1330=Daginstitutioner, plejehjem, CP1390=Andre tjenesteydelser]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector (V/LAN) — filter to one value or row counts double.
- formaaal with 44 COICOP groups from 1966. For fewer groups use nahc021 (15 grp). For more detail use nahc023 (73 grp, to 2022 only).
- CPT=I alt is the total — sum of the 44 subcategories. Use CPT to get total household consumption without summing.
