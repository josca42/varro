table: fact.bane53
description: Investeringer i rullende materiel efter investeringstype, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- invest: values [10011=RULLENDE MATERIEL, I ALT, 10015=DSB I ALT, 10031=DSB, nyinvesteringer, 10032=DSB, reinvesteringer, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- enhed: values [2004=Årets priser, 1990=1990-priser, 1995=1995-priser, 2000=2000-priser]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a price-year selector — same as bane42: MUST filter to exactly one value. 2004=Årets priser, 1990/1995/2000=constant prices.
- invest is hierarchical — do NOT sum all codes. Top level: 10011 (RULLENDE MATERIEL I ALT) = 10015 (DSB I ALT) + 10120 (ANDRE BANER) + 10130 (METROEN) + 10140 (LETBANE). Within DSB I ALT: 10031 (DSB nyinvesteringer) + 10032 (DSB reinvesteringer).
- This table covers rolling stock investments (trains, wagons). For infrastructure investments (track, stations) use bane42. The two tables share the same enhed coding and a similar bane/invest hierarchy but are NOT addable — they cover different asset types.
- Not all invest codes present for all years — LETBANE (10140) starts 2017, METROEN (10130) starts ~2002.