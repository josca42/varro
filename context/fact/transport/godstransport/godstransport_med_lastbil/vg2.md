table: fact.vg2
description: Vejgodstransport (faktiske tal) efter kørselsart, enhed og tid
measure: indhold (unit -)
columns:
- korart: values [1000=KØRSEL I ALT, 1500=National kørsel, 2000=Vognmandskørsel, 3000=Firmakørsel, 3500=International kørsel i alt, TIL=Til Danmark fra udlandet, FRA=Fra Danmark til udlandet, 3510=Øvrig international kørsel]
- maengde4: values [70=Pålæsset godsmængde (1000 ton), 88=Transportarbejde (mio. tonkm), 99=Kørte km (mio. km)]
- tid: date range 1998-01-01 to 2025-04-01

notes:
- maengde4 is a measurement selector (70=tons, 88=mio. tonkm, 99=mio. km). Filter to one.
- korart hierarchy is complex: 1000=grand total (national+international), 1500=National kørsel, 3500=International kørsel i alt; TIL+FRA+3510=3500; 1500+3500=1000; 2000/3000 are national vognmandskørsel/firmakørsel (subsets of 1500). Never sum across these without understanding the tree.
- Covers both national and international combined. Longest series from 1998. Actual (unadjusted) figures.
- For seasonally adjusted figures use vg3. For more detail (by goods type, region, truck type) use nvg*/ivg* tables.