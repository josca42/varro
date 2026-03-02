table: fact.nvg13
description: Danske lastbilers kapacitetsudnyttelse ved national vejgodstransport efter enhed, kørselsart, læs og tid
measure: indhold (unit -)
columns:
- enhed: values [90=Pct. af lasteevnen (ton) , 95=Pct. af lasteevnen (ton) korrigeret for volumengods, 100=Pct. af muligt transportarbejde (tonkm), 110=Pct. af muligt transportarbejde (tonkm) korrigeret for volumengods]
- korart: values [1000=KØRSEL I ALT, 2000=Vognmandskørsel, 3000=Firmakørsel]
- laes: values [1010=Kørsel i alt (inkl. tomkørsel), 1030=Kørsel med læs i alt]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- enhed is the measurement selector (capacity utilization percentages). All values are rates — do not sum across enhed.
- korart=1000 (KØRSEL I ALT) is the total; 2000/3000 are vognmandskørsel/firmakørsel. Don't sum 1000 with its children.
- laes: 1010=Kørsel i alt (including empty trips) contains 1030=Kørsel med læs. Not mutually exclusive — pick one.
- Simplest national capacity utilization table: korart × laes × enhed × tid.