table: fact.ivg11
description: International vejgodstransport med dansk lastbil efter kørselsart, enhed og tid
measure: indhold (unit -)
columns:
- korart: values [1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark, 6000=Tredjelandskørsel, 7000=Cabotagekørsel]
- enhed: values [10=Ture i alt, 1000, 20=Ture med læs, 1000, 30=Ture uden læs, 1000, 40=Kørte km i alt, 1000 km, 50=Kørte km med læs, 1000 km, 60=Kørte km uden læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- enhed is a measurement selector (8 options, trips to tonkm). Always filter to one.
- korart=1000 (KØRSEL I ALT) is the aggregate. 4000=Fra Danmark, 5000=Til Danmark, 6000=Tredjelandskørsel, 7000=Cabotagekørsel sum to 1000. Never sum 1000 with its children.
- Simplest international transport table (Danish trucks): korart × enhed × tid. Use for time series.