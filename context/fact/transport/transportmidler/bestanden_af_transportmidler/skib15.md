table: fact.skib15
description: Danske skibe i udenlansk register efter skibstype, enhed og tid
measure: indhold (unit -)
columns:
- skibtype: values [40005=SKIBE I ALT, 40010=LASTSKIBE I ALT, 40015=Containerskibe, 40020=Ro-Ro-lastskibe, 40025=Bulk-carriers, 40030=Køleskibe, 40035=Andre tørlastskibe, 40040=Gastankskibe, 40045=Kemikalietankskibe, 40050=Supertankere, 40055=Andre tankskibe, 40060=PASSAGERSKIBE OG FÆRGER, 40070=ANDRE SKIBE]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 2017-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed.
- Covers only Danish ships in a foreign register (udenlandsk register). Compare with skib11/skib14 for ships in Danish registers.
- skibtype=40005 (SKIBE I ALT) and 40010 (LASTSKIBE I ALT) are aggregates — filter when summing detail codes.