<fact tables>
<table>
id: pris4321
description: Producent- og importprisindeks for varer efter branchehovedgrupper, marked, enhed og tid
columns: hovedgrp, marked1, enhed, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2025-09-01
</table>
<table>
id: pris1121
description: Prisindeks for indenlandsk vareforsyning efter varegruppe, enhed og tid
columns: varegr, tal, tid (time), indhold (unit Indeks)
tid range: 1981-01-01 to 2025-09-01
</table>
<table>
id: pris4621
description: Prisindeks for indenlandsk vareforsyning efter branchehovedgrupper, enhed og tid
columns: hovedgrp, enhed, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2025-09-01
</table>
<table>
id: pris1900
description: Prisindeks for indenlandsk vareforsyning; årsgennemsnit efter indekstype og tid
columns: indekstype, tid (time), indhold (unit Indeks)
tid range: 1876-01-01 to 2024-01-01
</table>
<table>
id: pris4221
description: Producentprisindeks for varer efter branche standardgrupperinger, enhed og tid
columns: standgrp, tal, tid (time), indhold (unit Indeks)
tid range: 2000-01-01 to 2025-09-01
</table>
</fact tables>

notes:
- All tables in this subject use a measurement selector column (enhed or tal) with three values: Indeks (100), Ændring i forhold til måneden før (200), Ændring i f.t. samme måned året før (300). Always filter to one value — failure to do so triples all counts.
- Table selection by classification type: pris4321 and pris4221 classify by industry branch (NACE/DB07-inspired), pris4621 by branch too. pris1121 classifies by commodity/product group (SITC-based). Use industry branch tables when the question is about which sector produced the goods; use pris1121 when the question is about which type of goods.
- Table selection by time coverage: pris1900 = annual 1876–2024 (aggregate total only). pris1121 = monthly 1981–present (by commodity). pris4221 = monthly 2000–present (by producer branch). pris4321 = monthly 2005–present (by branch + market). pris4621 = monthly 2014–present (by branch, domestic supply only).
- For market split (home market vs export vs import): only pris4321 has the marked1 column. pris4321 must always have both enhed and marked1 filtered to avoid 12x overcounting.
- For long historical commodity series: pris1121 goes back to 1981 with 93 product groups.
- For ultra-long historical aggregate: pris1900 goes back to 1876 as a single annual series.
- dim.db joins are unreliable across this entire subject. The branch columns (hovedgrp in pris4321/pris4621, standgrp in pris4221) mix numeric NACE codes with letter aggregate codes and S-codes, none of which join cleanly to dim.db. Always use ColumnValues on the fact table column directly — labels are embedded in the column values.