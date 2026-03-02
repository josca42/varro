<fact tables>
<table>
id: ifi01r
description: Industriens investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), bedømmelse og tid
columns: branche07, opg, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2026-01-01
</table>
<table>
id: ifib
description: Industriens investeringsforventninger efter branche (DB07), påvirkende forhold og tid
columns: branche07, paafor, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2026-01-01
</table>
<table>
id: ifif
description: Industriens investeringsforventninger efter branche (DB07), formål og tid
columns: branche07, formal, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2026-01-01
</table>
<table>
id: ifi01
description: Industriens investeringsforventninger efter branche (DB07), bedømmelse og tid
columns: branche07, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2026-01-01
</table>
<table>
id: ifi02r
description: Industriens investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), investeringstype, bedømmelse og tid
columns: branche07, opg, invest, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2026-01-01
</table>
<table>
id: ifi02
description: Industriens investeringsforventninger efter branche (DB07), investeringstype, bedømmelse og tid
columns: branche07, invest, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: ifs01r
description: Serviceerhvervets investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), bedømmelse og tid
columns: branche07, opg, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2021-01-01 to 2026-01-01
</table>
<table>
id: ifsb
description: Serviceerhvervets investeringsforventninger efter branche (DB07), påvirkende forhold og tid
columns: branche07, paafor, tid (time), indhold (unit Pct.)
tid range: 2021-01-01 to 2026-01-01
</table>
<table>
id: ifsf
description: Serviceerhvervets investeringsforventninger efter branche (DB07), formål og tid
columns: branche07, formal, tid (time), indhold (unit Pct.)
tid range: 2021-01-01 to 2026-01-01
</table>
<table>
id: ifs01
description: Servicerhvervets investeringsforventninger efter branche (DB07), bedømmelse og tid
columns: branche07, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2021-01-01 to 2026-01-01
</table>
<table>
id: ifs02r
description: Serviceerhvervets investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), investeringstype, bedømmelse og tid
columns: branche07, opg, invest, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2021-01-01 to 2026-01-01
</table>
<table>
id: ifs02
description: Serviceerhvervets investeringsforventninger efter branche (DB07), investeringstype, bedømmelse og tid
columns: branche07, invest, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2021-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- Two parallel survey series: **industri** (ifi*) from 2010, and **serviceerhverv** (ifs*) from 2021. Same structure within each group, but different branche07 coding schemes and different sectors covered.
- **Naming pattern**: no suffix = bedømmelse only (headline sentiment), "b" = påvirkende forhold (factors), "f" = formål (investment purpose), "02" = investeringstype breakdown, "r" suffix = includes opgørelse/revision dimension. For most questions use the non-"r" version; use "r" only to compare preliminary vs final estimates.
- **bedommelse is always a selector that must be filtered**: STØ+UÆN+MIN sum to 100; NET=STØ−MIN. Use bedommelse='NET' for the standard net expectations headline.
- **opg in "r" tables multiplies rows 4×**: ifi01r, ifi02r, ifs01r, ifs02r each store preliminary and revised estimates for every year. Always filter to one opg value (opg=45=Endelige tal for final, opg=10 for earliest estimate).
- **branche07 does NOT join dim.db in any of these tables**: ifi* uses DB07 section letter codes (B, C, CA–CM) plus MIG groups (S1–S4); ifs* uses survey-specific numeric codes (0=SERVICEERHVERV I ALT, 5=TRANSPORT sector, etc.). Use ColumnValues on the specific table for labels.
- **ifs* branche07 has 2-level hierarchy** embedded in the coded values: code 0 is total; uppercase-labeled codes (5, 15, 35, 45, 60, 65, 80) are sector aggregates; mixed-case codes (10, 20, 25, 30, 40, 50, 55, 70, 75, 85, 90) are sub-sectors. Filter to one level to avoid double-counting.
- **paafor (ifib/ifsb) is NOT mutually exclusive** — percentages sum above 100 per group. Compare factors side by side, never aggregate.
- **formal (ifif/ifsf) sums to 100** — investment budget allocation. Show all four values together.
- **invest (ifi02/ifi02r/ifs02/ifs02r)**: TOTAL is stored independently. Filter invest='TOTAL' for aggregate; use MASK/LAND/IMMA to compare composition. Never sum invest values.