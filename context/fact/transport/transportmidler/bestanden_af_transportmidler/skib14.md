table: fact.skib14
description: Danske handelsskibe pr. 1. januar efter skibstype, enhed og tid
measure: indhold (unit -)
columns:
- skibtype: values [40005=SKIBE I ALT, 40010=LASTSKIBE I ALT, 40015=Containerskibe, 40020=Ro-Ro-lastskibe, 40025=Bulk-carriers, 40030=Køleskibe, 40035=Andre tørlastskibe, 40040=Gastankskibe, 40045=Kemikalietankskibe, 40050=Supertankere, 40055=Andre tankskibe, 40060=PASSAGERSKIBE OG FÆRGER, 40070=ANDRE SKIBE]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 1990-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed.
- Covers only handelsskibe (merchant ships). Has the most detailed skibstype breakdown of the skib tables, including individual cargo/tanker subtypes.
- skibtype=40005 (SKIBE I ALT) and 40010 (LASTSKIBE I ALT) are aggregates — filter to detail codes only when summing.
- Longest time series of the skib tables: back to 1990.