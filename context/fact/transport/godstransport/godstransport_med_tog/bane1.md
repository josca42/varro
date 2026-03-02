table: fact.bane1
description: Jernbanetransport af gods efter enhed, transporttype, banenet og tid
measure: indhold (unit -)
columns:
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- transport: values [1000=KØRSEL I ALT, 1500=National kørsel, 1600=International kørsel , 4000=Fra Danmark, 5000=Til Danmark, 8000=Transit kørsel]
- bane: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10120=ANDRE BANER]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a measurement selector: 75=1000 ton (weight), 76=Mio. tonkm (tonne-kilometres). Always filter to one value — summing both doubles the result.
- transport has aggregate/detail structure: 1000=KØRSEL I ALT is the grand total; 1500 (national) and 1600 (international) partition it; 4000 (fra Danmark) and 5000 (til Danmark) partition international; 8000 (transit) is separate. Pick one level — never sum across all transport values.
- bane has the same pattern: 10010=I ALT, 10020=Banedanmarks net, 10120=Andre baner. Filter to 10010 for totals or pick one sub-net.
- Annual data (tid is always Jan 1). Longest series in this subject: goes back to 1990. Use this table when historical context pre-2008 is needed.