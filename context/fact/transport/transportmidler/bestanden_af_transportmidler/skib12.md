table: fact.skib12
description: Danske skibe pr. 1. januar efter skibstype, bruttotonnage (BT), enhed og tid
measure: indhold (unit -)
columns:
- skibtype: values [40005=SKIBE I ALT, 40031=Tankskibe, 40039=Tørlastskibe, 40060=PASSAGERSKIBE OG FÆRGER, 40071=Fiskerfartøjer, 40130=Skibe i øvrigt]
- bt: values [6600=SKIBE I ALT, 6605=20-49 BT, 6610=50-99 BT, 6615=100-149 BT, 6620=150-249 BT ... 6680=25000-29999 BT, 6685=30000-39999 BT, 6690=40000-49999 BT, 6695=50000-99999 BT, 6700=100000 BT og derover]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 1994-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed.
- bt=6600 (SKIBE I ALT) is the total across all tonnage bands. Summing individual bt bands without filtering out bt=6600 will double-count.
- skibtype has aggregate codes (40005=SKIBE I ALT) alongside detail codes — filter to the level you need.