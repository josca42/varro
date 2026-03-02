table: fact.nahc1
description: Forbrugsudgift efter forbrugsart, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- forbrugsart: values [P31DC=Husholdningers forbrugsudgift på dansk område, P33=Turistudgifter, P34=Turistindtægter, P31S14=Husholdningernes forbrugsudgifter, P31S15=Forbrugsudgifter i Non-profit institutioner rettet mod husholdninger (NPISH), P31S1M=Privatforbrug, P3S13=Offentlige forbrugsudgifter, P31S13=Offentlige individuelle forbrugsudgifter, P32S13=Offentlige kollektive forbrugsudgifter, P3=Samlede udgifter til forbrug, P41=Faktisk individuelt forbrug, P42=Faktisk kollektivt forbrug]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector (V/LAN) — filter to one value or row counts double.
- forbrugsart codes span multiple levels of aggregation. P3=samlede forbrugsudgifter (broadest total), P41=faktisk individuelt forbrug, P31S14=husholdningers forbrugsudgifter. Several codes overlap: P31S1M = P31S14 + P31S15; P3S13 = P31S13 + P32S13. Never sum all forbrugsart values.
- Annual from 1966. For breakdown by COICOP purpose see nahc021 (15 grp). For breakdown by durability see nahc3.
