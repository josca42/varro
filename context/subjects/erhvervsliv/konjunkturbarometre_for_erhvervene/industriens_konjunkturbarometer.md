<fact tables>
<table>
id: kbi1
description: Udviklingsforløb i industrien efter branche (DB07), indikator, bedømmelse, forløb og tid
columns: branche07, indikator, bedommelse, forlob, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbi2
description: Vurderinger i industrien efter branche (DB07), indikator, bedømmelse og tid
columns: branche07, indikator, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbi3
description: Produktionsbegrænsninger i industrien efter branche (DB07), årsag og tid
columns: branche07, aarsag, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbi4
description: Kapacitetsudnyttelse i industrien efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbi5
description: Vurdering af produktionskapacitet efter branche (DB07), bedømmelse og tid
columns: branche07, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbi6
description: Konkurrencesituationen på eksportmarkederne i industrien efter branche (DB07), indikator, bedømmelse og tid
columns: branche07, indikator1, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
</fact tables>

notes:
- All 6 tables share the same branche07 column with DB07 letter codes (B, BC, C, CA–CM, S1–S4). These do NOT join dim.db (which uses numeric codes). BC=mining+manufacturing aggregate, C=total manufacturing, CA–CM=13 sub-industries, S1–S4=MIG cross-cutting groups. Always filter to one hierarchy level; never sum across BC/C/sub-industries as they overlap.
- For a quick time series on a single topic without sub-industry breakdown, branche07='C' (total manufacturing) is the natural default.
- Table selection guide:
  - kbi1: production/employment/orders/prices — trend direction (rising/falling/net). Has forlob (actual vs expected). Most multidimensional table (4 dims).
  - kbi2: current levels of inventory and order backlogs — too small / appropriate / too large assessments.
  - kbi3: production constraints — which bottlenecks firms cite (labour, materials, demand, finance). Values are NOT mutually exclusive; do not sum across aarsag.
  - kbi4: quantitative capacity utilization rate (%). Simplest table — just branche07 and tid, one row per combination.
  - kbi5: qualitative capacity assessment — firms' view of whether capacity is too small/appropriate/too large. Pair with kbi4.
  - kbi6: competitive situation on export markets, split into EU vs non-EU (indikator1).
- NET (nettotal) interpretation varies by table: kbi1 NET = STØ1−MIN1; kbi2/kbi5 NET = SNO2−MN2; kbi6 NET = FORB−FORR. Always filter to a single bedommelse value; never sum across all bedommelse values (NET is derived from the others).
- All tables cover 2005–2025 quarterly.