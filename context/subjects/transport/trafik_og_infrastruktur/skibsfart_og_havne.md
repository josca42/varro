<fact tables>
<table>
id: skib21
description: Fragtskibes anløb på større havne efter flagstat, skibstype, enhed og tid
columns: flag, skibtype, enhed, tid (time), indhold (unit -)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: skib221
description: Skibsanløb på danske havne efter havn, skibstype, bruttotonnage (BT) og tid
columns: havn, skibtype, bt, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib23
description: Fragtskibes og krydstogtskibes anløb på større danske havne efter havn, skibstype og tid
columns: havn, skibtype, tid (time), indhold (unit Antal)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: ais1
description: Anløbsaktivitet i danske havne (eksperimentel statistik) efter landsdel, sæsonkorrigering, enhed og tid
columns: landdel, saeson, tal, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2025-10-01
</table>
<table>
id: skib101
description: Trafikhavnenes skibsanløb, passagerer og godsomsætning efter havn, enhed og tid
columns: havn, enhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib2
description: Investeringer i havne efter prisenhed, investeringstype og tid
columns: prisenhed, invest, tid (time), indhold (unit Mio. kr.)
tid range: 1992-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For ship arrivals with harbor + ship-type breakdown: use skib221 (from 2007, includes BT size class) or skib23 (from 1997, more cargo subtypes but no BT). skib23 goes further back and has finer cargo-type detail (8 types: containerskibe, bulk, tank, krydstogsskibe, etc.). skib221 only has 2 types (lastskibe, passagerskibe/færger) but adds BT size class.
- For cargo tonnage or passenger counts by harbor: use skib101. It is the only table with godsomsætning (1000 ton) and passagerer (1000). Also includes ship arrivals, so one table gives you all three metrics.
- For freight ships by flag state (country of registration): use skib21. Only table with flag dimension. Covers both ship arrivals (antal) and bruttotonnage — filter enhed to pick one.
- For most recent national trend data (monthly, through late 2025): use ais1. It is experimental/AIS-based and has no harbor or ship-type breakdown, but it is the most up-to-date.
- For harbor investment spending (not ship traffic): use skib2. Annual data back to 1992, national totals only.
- Common overcounting traps across all tables: (1) enhed/saeson/prisenhed are measurement selectors — always filter to one value; (2) havn codes 1000+ are LANDSDEL aggregates mixed with havn='0' (national total) and specific harbor codes — never sum across levels; (3) skibtype and bt codes include I ALT totals alongside individual categories.
- ais1 is the only table with data past 2024; all others run through 2024-01-01 or 2023-01-01 (skib2).