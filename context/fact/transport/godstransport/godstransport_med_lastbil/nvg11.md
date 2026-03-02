table: fact.nvg11
description: National vejgodstransport efter kørselsart, enhed og tid
measure: indhold (unit -)
columns:
- korart: values [1000=KØRSEL I ALT, 2000=Vognmandskørsel, 3000=Firmakørsel]
- enhed: values [10=Ture i alt, 1000, 20=Ture med læs, 1000, 30=Ture uden læs, 1000, 40=Kørte km i alt, 1000 km, 50=Kørte km med læs, 1000 km, 60=Kørte km uden læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- tid: date range 1999-01-01 to 2025-04-01
notes:
- enhed is a measurement selector — every korart/tid combination repeats for each enhed value. Always filter to one enhed value.
- korart=1000 (KØRSEL I ALT) is the aggregate of 2000+3000. Never sum 1000 with its children.
- Simplest national transport table: just korart × enhed × tid. Use this for time series of total national freight.
