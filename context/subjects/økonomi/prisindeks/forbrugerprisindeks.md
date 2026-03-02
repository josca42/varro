<fact tables>
<table>
id: pris111
description: Forbrugerprisindeks efter varegruppe, enhed og tid
columns: varegr, enhed, tid (time), indhold (unit -)
tid range: 2001-01-01 to 2025-09-01
</table>
<table>
id: pris112
description: Forbrugerprisindeks efter hovedtal og tid
columns: hoved, tid (time), indhold (unit Pct.)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: pris8
description: Forbrugerprisindeks, årsgennemsnit efter type og tid
columns: type, tid (time), indhold (unit Indeks)
tid range: 1900-01-01 to 2024-01-01
</table>
<table>
id: pris9
description: Forbrugerprisindeks, gennemsnitlig årlig inflation efter type og tid
columns: type, tid (time), indhold (unit Pct.)
tid range: 1901-01-01 to 2024-01-01
</table>
<table>
id: pris113
description: Forbrugerprisindeks, hovedtal efter type og tid
columns: type, tid (time), indhold (unit Indeks)
tid range: 1980-01-01 to 2025-09-01
</table>
<table>
id: pris201
description: Husstandsopdelte forbrugerprisindeks efter varegruppe, husstandsgrupper, enhed og tid
columns: varegr, husgrp, tal, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2025-08-01
</table>
</fact tables>

notes:
- **For current monthly CPI (headline)**: use pris113 (monthly from 1980, single series). Simplest query: SELECT tid, indhold FROM fact.pris113.
- **For annual CPI going back to 1900**: use pris8 (index level) or pris9 (% inflation rate). Both are single-series, no filtering needed.
- **For annual CPI from 1980 with both index and % change**: use pris112 (hoved=1005 for level, hoved=1010 for % change). Filter to one hoved — the two series have different units.
- **For CPI by product category (ECOICOP)**: use pris111 (monthly from 2001, 385 categories across all ECOICOP niveaux 1–5). The enhed column is a measurement selector (100/200/300) — always filter to one value.
- **For CPI by household group**: use pris201 (monthly from 2006, niveau 1–2 ECOICOP only). Has both husgrp (21 household groups in 3 overlapping schemes) and tal (measurement selector) — filter both.
- **varegr join gotcha (pris111 and pris201)**: the varegr column uses 5-or-6 digit zero-padded ECOICOP codes. A direct join on varegr=kode fails (~0% match). Use the modulo-based stripping join documented in each fact doc.
- **All tables with a measurement-type column** (enhed in pris111, tal in pris201, hoved in pris112) silently multiply rows — failing to filter will inflate any aggregate. This is the most common pitfall in this subject.