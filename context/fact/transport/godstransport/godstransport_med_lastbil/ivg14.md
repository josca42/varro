table: fact.ivg14
description: Danske lastbilers kapacitetsudnyttelse ved international vejgodstransport efter kørselsart, læs, enhed og tid
measure: indhold (unit -)
columns:
- korart: values [1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark]
- laes: values [1010=Kørsel i alt (inkl. tomkørsel), 1030=Kørsel med læs i alt]
- enhed: values [90=Pct. af lasteevnen (ton) , 95=Pct. af lasteevnen (ton) korrigeret for volumengods, 100=Pct. af muligt transportarbejde (tonkm), 110=Pct. af muligt transportarbejde (tonkm) korrigeret for volumengods]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- enhed is the measurement selector (capacity utilization percentages, 4 options). Filter to one — values are rates, not sums.
- korart: 1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark. Note: only 3 korart values (no tredjelandskørsel/cabotage), unlike ivg11.
- laes: 1010 includes 1030. Not mutually exclusive.
- Simplest international capacity utilization table. Use for time series of capacity utilization by direction.