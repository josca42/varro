table: fact.kbi4
description: Kapacitetsudnyttelse i industrien efter branche (DB07) og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db — uses DB07 letter codes. Same hierarchy as kbi1 (BC=aggregate, C=total manufacturing, CA–CM=sub-industries, S1–S4=MIG groups). Use ColumnValues("kbi4", "branche07") for labels.
- Simplest kbi table — indhold is the direct % capacity utilization rate (e.g. 81 = 81%). No other dimension columns; no overcounting risk beyond branche07 hierarchy. Each branche07×tid has exactly one row.
- Pair with kbi5 for the qualitative assessment of whether capacity level is too small/appropriate/too large.
- Sample: SELECT tid, indhold FROM fact.kbi4 WHERE branche07='C' ORDER BY tid;