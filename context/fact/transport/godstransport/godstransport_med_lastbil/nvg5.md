table: fact.nvg5
description: Danske lastbiler kapacitetsudnyttelse ved national transport efter enhed, turlængde, vogntype/kørselsart, læs og tid
measure: indhold (unit Pct.)
columns:
- enhed: values [90=Pct. af lasteevnen (ton) , 95=Pct. af lasteevnen (ton) korrigeret for volumengods, 100=Pct. af muligt transportarbejde (tonkm), 110=Pct. af muligt transportarbejde (tonkm) korrigeret for volumengods]
- turkm: values [00=Ture i alt, 00-14=Mindre end 15 km, 15-29=15-29 km, 30-49=30-49 km, 50-99=50-99 km, 100-199=100-199 km, 200OV=200 km eller mere]
- vogn: values [0=I ALT, 50=Solovogn, i alt, 55=Påhængsvogntog, i alt, 60=Sættevognstog, i alt, 65=Vognmandskørsel, i alt, 70=Vognmandskørsel, Solovogn, 75=Vognmandskørsel, Påhængsvogntog, 80=Vognmandskørsel, Sættevognstog, 85=Firmakørsel, i alt, 90=Firmakørsel, Solovogn, 95=Firmakørsel, Påhængsvogntog, 100=Firmakørsel, Sættevognstog]
- laes: values [1010=Kørsel i alt (inkl. tomkørsel), 1030=Kørsel med læs i alt]
- tid: date range 1999-01-01 to 2024-01-01
notes:
- All indhold values are percentages (capacity utilization). Do not sum across rows — each value is an independent rate.
- enhed selects what is measured: % of loading capacity (ton) or % of possible transport work (tonkm), with and without volume-goods correction. Filter to one.
- turkm=00 (Ture i alt) is the total across all distances. Filter here to avoid mixing distance bands.
- vogn mixes two classification axes in one column: vehicle type (Solovogn/Påhængs/Sætte, codes 50/55/60) and drive type (Vognmandskørsel/Firmakørsel, codes 65/85) with their cross combinations. Code 0=I ALT. Only filter to one interpretation — e.g. vogn='0' for overall average, or vogn='65' for vognmandskørsel regardless of vehicle type.
- laes: 1010=Kørsel i alt (includes empty trips) and 1030=Kørsel med læs. These are NOT mutually exclusive — 1010 includes 1030. Never sum them; pick one.
