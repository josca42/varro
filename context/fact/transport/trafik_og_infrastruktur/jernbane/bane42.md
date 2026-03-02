table: fact.bane42
description: Investeringer i jernbanenettet efter investeringstype, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- invest: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10031=DSB, nyinvesteringer, 10032=DSB, reinvesteringer, 10033=DSB, øvrige investeringer, 10034=Storebæltsforbindelsen, 10035=Øresundsforbindelsen, 10036=Femernforbindelsen, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- enhed: values [2004=Årets priser, 1990=1990-priser, 1995=1995-priser, 2000=2000-priser]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a price-year selector — MUST filter to exactly one value. Options: 2004=Årets priser (current prices), 1990/1995/2000=constant prices in that base year. For time-series comparisons use a fixed base year; for a single year use 2004. Summing across enhed counts the same investments multiple times in different price bases.
- invest is hierarchical — do NOT sum all codes. Top level: 10010 (BANENETTET I ALT) = 10020 (BANEDANMARKS NET) + 10120 (ANDRE BANER) + 10130 (METROEN) + 10140 (LETBANE). Within BANEDANMARKS NET: 10031 (DSB nyinvesteringer) + 10032 (DSB reinvesteringer) + 10033 (DSB øvrige) + 10034 (Storebælt) + 10035 (Øresund) + 10036 (Femern).
- Not all invest/enhed combos span 1990–2024: Femern (10036) only has data from ~2010; some sub-codes only available from 1995 or 2000. Expect NULLs.
- This table covers infrastructure investments (track, stations). For rolling stock investments use bane53.