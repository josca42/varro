table: fact.skib221
description: Skibsanløb på danske havne efter havn, skibstype, bruttotonnage (BT) og tid
measure: indhold (unit Antal)
columns:
- havn: values [0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 25=Københavns Havn, 2000=LANDSDEL KØBENHAVNS OMEGN, 10=Avedøreværkets Havn ... 790=Skagen Havn, 720=Thisted Havn, 795=Vesterø Havn, 730=Aalborg Havn, 735=Aalborg Portland Havn]
- skibtype: values [40005=SKIBE I ALT, 40011=Lastskibe, 40061=Passagerskibe og færger]
- bt: values [6600=SKIBE I ALT, 6621=Mindre end 250 BT, 6623=250 - 499 BT, 6630=500-1499 BT, 6636=1500 - 4999 BT, 6656=5000 - 9999 BT, 6666=10000 - 24999  BT, 6705=25000 BT og derover ]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Three columns each have a grand total code — filter all three to avoid overcounting: havn='0' (HAVNE I ALT), skibtype='40005' (SKIBE I ALT), bt='6600' (SKIBE I ALT).
- havn codes 1000–11000 are LANDSDEL regional aggregates (11 landsdele). Codes below 1000 are specific harbors. havn='0' is the national total. These levels are NOT additive — only pick one level.
- bt has 7 size classes (6621–6705) that sum to 6600. For a breakdown by BT size, use all 7 and exclude bt='6600'.
- skibtype covers only lastskibe (40011) and passagerskibe/færger (40061) — fewer types than skib23. For cargo-ship-type detail, use skib23 instead.
- For a simple count of arrivals by harbor: WHERE skibtype='40005' AND bt='6600' AND havn != '0' AND CAST(havn AS INTEGER) < 1000.