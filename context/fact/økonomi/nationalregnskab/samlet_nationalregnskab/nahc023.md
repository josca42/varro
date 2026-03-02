table: fact.nahc023
description: Husholdningers forbrug på dansk område (73 grp) efter formål, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- formaaal: values [CPT=I alt, CP01110=Brød og kornprodukter, CP01120=Kød, CP01130=Fisk, CP01141=Mælk, fløde, yoghurt mv. ... CP13130=Frisører mv., CP13200=Andre personlige artikler, CP13301=Daginstitutioner for børn, CP13302=Plejehjem, dagcentre mv., CP13900=Andre tjenesteydelser]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2022-01-01
notes:
- prisenhed is a measurement selector (V/LAN) — filter to one value or row counts double.
- Most granular COICOP breakdown (73 groups) but only available to 2022. For current data use nahc022 (44 grp) or nahc021 (15 grp) which go to 2024.
- CPT=I alt is the total. The 73 groups sum to CPT.
