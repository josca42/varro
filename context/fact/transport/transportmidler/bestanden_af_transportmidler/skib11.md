table: fact.skib11
description: Danske skibe  pr. 1. januar efter skibstype, skibsregister, enhed og tid
measure: indhold (unit -)
columns:
- skibtype: values [40005=SKIBE I ALT, 40010=LASTSKIBE I ALT, 40015=Containerskibe, 40020=Ro-Ro-lastskibe, 40025=Bulk-carriers ... 40110=Redningsskibe, 40115=Vagtskibe, 40120=Dykkerskibe, 40125=Fritidsskibe, 40130=Skibe i øvrigt]
- skibreg: values [1000=I alt, 1003=Dansk skibsregister, hjemsted Danmark, 1004=Dansk skibsregister, hjemsted Grønland, 1005=Dansk Skibsregister, 1010=Dansk Internationalt Skibsregister (DIS)]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 1990-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed — they are in completely different units and must never be summed together.
- skibreg=1000 is I alt. 1005=Dansk Skibsregister (combined), 1010=Dansk Internationalt Skibsregister (DIS). Filter skibreg=1000 for totals.
- skibtype=40005 (SKIBE I ALT) is the grand total. Use ColumnValues("skib11", "skibtype") for the full hierarchy with aggregate and detail codes.