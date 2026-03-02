<fact tables>
<table>
id: pris117
description: EU-harmoniseret forbrugerprisindeks (HICP) efter varegruppe, enhed og tid
columns: varegr, enhed, tid (time), indhold (unit -)
tid range: 1996-01-01 to 2025-09-01
</table>
<table>
id: pris118
description: EU-harmoniseret forbrugerprisindeks med konstante skatter (HICP-CT) efter varegruppe, enhed og tid
columns: varegr, tal, tid (time), indhold (unit -)
tid range: 2001-01-01 to 2025-09-01
</table>
<table>
id: pris119
description: EU-harmoniseret forbrugerprisindeks efter hovedtal og tid
columns: hoved, tid (time), indhold (unit Indeks)
tid range: 1996-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- pris117 (HICP) is the primary table: monthly data from 1996, full ECOICOP product breakdown (378 categories across 4 hierarchy levels), three measures (index/mom%/yoy%). Use this for most HICP questions.
- pris118 (HICP-CT) has identical structure to pris117 but with taxes held constant — use it to isolate price changes from tax policy changes. Starts 2001 instead of 1996.
- pris119 is a simple annual summary with no product breakdown (only overall HICP, annual average and annual growth). Use only when a quick single-number annual series suffices; stops at 2024.
- Critical gotcha for pris117/pris118: varegr uses 6-digit ECOICOP codes (e.g. '010000', '100000') that cannot be joined to dim.ecoicop with simple equality. Requires a decode expression — see the pris117 fact doc for the full SQL. Never attempt f.varegr = d.kode::text directly.
- Critical gotcha for all three tables: enhed/tal/hoved are measurement selectors. Every varegr+tid row appears 2–3 times for different measures. Always filter to one value before summing or charting.
- The HICP uses the EU ECOICOP classification (12 divisions, 47 groups, 117 classes, 303 subclasses in dim.ecoicop). For Danish-specific CPI use the forbrugerprisindeks tables (pris111/pris112/pris113) instead.