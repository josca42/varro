table: fact.kbi5
description: Vurdering af produktionskapacitet efter branche (DB07), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- bedommelse: values [MN2=For små eller ikke tilstrækkelig, NOR2=Passende eller tilstrækkelig, SNO2=For store eller mere end tilstrækkelig, NET=Nettotal]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db — uses DB07 letter codes. Same hierarchy as kbi1. Use ColumnValues("kbi5", "branche07") for labels.
- bedommelse=NET = SNO2 − MN2. Positive NET means more firms say capacity is more than sufficient (excess capacity). Negative means capacity shortage. Example for C in 2024-Q1: MN2=14, SNO2=26, NET=12 (excess capacity). Do not sum across bedommelse values.
- Qualitative complement to kbi4 (quantitative utilization %). Use together: kbi4 gives the rate, kbi5 gives firms' assessment of whether that rate is too high or low.
- Sample: SELECT tid, indhold FROM fact.kbi5 WHERE branche07='C' AND bedommelse='NET' ORDER BY tid;