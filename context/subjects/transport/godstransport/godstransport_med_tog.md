<fact tables>
<table>
id: bane1
description: Jernbanetransport af gods efter enhed, transporttype, banenet og tid
columns: enhed, transport, bane, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: bane201
description: Jernbanetransport af gods efter enhed, transporttype, godsart og tid
columns: enhed, transport, gods, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: bane401
description: National jernbanetransport af gods efter enhed, pålæsningsregion, aflæsningsregion og tid
columns: enhed, paregion, afregion, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bane5
description: Jernbanetransport af farligt gods efter transporttype, godsart, enhed og tid
columns: transport, gods, maengde4, tid (time), indhold (unit -)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: bane6
description: Jernbanetransport af intermodale lasteenheder efter transporttype, lasteenhed, enhed og tid
columns: transport, last, maengde4, tid (time), indhold (unit -)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: bane3
description: International jernbanetransport af gods efter retning, enhed, land og tid
columns: ret, enhed, land, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bane9a
description: Jernbanetransport af gods efter enhed, transporttype og tid
columns: enhed, transport, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- For total rail freight (weight or tonne-km) without breakdown: bane9a is best for recent data (quarterly to 2025 Q1, from 2013); bane1 goes back to 1990 and has banenet breakdown. bane9a has no banenet or godsart columns — use bane1 if those are needed.
- For freight by cargo type (godsart): bane201 (2008+). Note the two-layer gods column: operator split (105/665) and cargo-type breakdown (840–878) both sit alongside the grand total (100) — pick one layer.
- For regional origin-destination matrix (which region loaded/unloaded): bane401 (2007+). Only 5 Danish regions (niveau=1). Rows with paregion=0 or afregion=0 are marginals, not extra shipments.
- For international freight by partner country: bane3 (2000+). Use INNER JOIN on dim.lande_uhv to get country names — this drops IA (total) and OV (other). For the total, filter land='IA' directly.
- For dangerous goods only: bane5 (2004+). Note column is named maengde4, not enhed — same values though (75/76).
- For intermodal loading units (containers, TEU, semi-trailers): bane6 (2004+). maengde4 has 6 incomparable measurement types including unit counts, TEU, and weight — always filter to one.
- Universal gotcha: every table has a measurement selector (enhed or maengde4) with at least values 75 and 76. Never sum across both — always filter to one unit. Similarly, transport always includes aggregate code 1000 alongside its sub-codes — pick one level of the hierarchy.
- Map: bane401 supports choropleth at region level (niveau 1) via /geo/regioner.parquet — merge on paregion or afregion. All other tables in this subject have no geographic dimension.