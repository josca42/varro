table: fact.skib21
description: Fragtskibes anløb på større havne efter flagstat, skibstype, enhed og tid
measure: indhold (unit -)
columns:
- flag: values [TOT=LANDE I ALT, 003=Nederlandene, 004=Tyskland, 006=Storbritannien, 008=Danmark ... 706=Singapore, 740=Hongkong, 7990=Asien i øvrigt, 800=Australien, 958=Uoplyst land]
- skibtype: values [40005=SKIBE I ALT, 40031=Tankskibe, 40039=Tørlastskibe]
- enhed: values [7000=Skibsanløb, antal, 7001=Bruttotonnage, 1000 BT]
- tid: date range 1997-01-01 to 2024-01-01

notes:
- enhed is a measurement selector: 7000=Skibsanløb (antal), 7001=Bruttotonnage (1000 BT). These are completely different units. Always filter to one enhed — summing across both silently doubles rows.
- flag='TOT' is the grand total across all countries. Individual country codes (003, 004, ...) sum up to TOT. Filter flag='TOT' for national totals, or pick specific countries.
- skibtype='40005' (SKIBE I ALT) is the total of 40031+40039. Filter to one level to avoid double-counting.
- For a simple query (e.g. total freight ship arrivals in 2024): WHERE flag='TOT' AND skibtype='40005' AND enhed='7000' AND tid='2024-01-01'.
- The flag column includes a handful of "rest" codes (e.g. 7990=Asien i øvrigt, 958=Uoplyst land) that are not specific countries — these roll up into TOT.