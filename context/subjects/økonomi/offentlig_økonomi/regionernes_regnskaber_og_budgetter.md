<fact tables>
<table>
id: regr11
description: Regionernes regnskaber på hovedkonti efter område, hovedkonto, dranst, art, prisenhed og tid
columns: omrade, funk1, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regr31
description: Regionernes regnskaber efter region, hovedkonto, dranst, art, prisenhed og tid
columns: regi07, funk1, dranst, art, prisenhed, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regr4
description: Regionernes balance (1000 kr.) efter område, funktion og tid
columns: omrade, funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regr55
description: Regionernes regnskaber efter region, hovedkonto, tværgående grupperinger, art og tid
columns: regi07, funk1, tvgrp, art, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regr63
description: Regionernes finansielle aktiver og passiver efter funktion og tid
columns: funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-04-01 to 2025-04-01
</table>
<table>
id: regr64
description: Regionernes likvide beholdninger (1000 kr.) efter funktion og tid
columns: funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-04-01 to 2025-04-01
</table>
<table>
id: regr65
description: Regionernes langfristede gæld (1000 kr.) efter funktion og tid
columns: funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-04-01 to 2025-04-01
</table>
<table>
id: budr32
description: Region budgetter (1000 kr.) efter region, funktion, dranst, art, prisenhed og tid
columns: regi07, funktion, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: budr1
description: Region budgetter (1000 kr.) efter region, hovedkonto, dranst, art, prisenhed og tid
columns: regi07, funk1, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- Accounts (regnskaber) vs budgets: regr11/regr31/regr4/regr55/regr63/regr64/regr65 are actual accounts (through 2024). budr1/budr32 are budgets (through 2025). To compare budget vs. actual, pair budr1↔regr11 or budr32↔regr31.
- High-level vs detailed functions: regr11/budr1 use funk1 with 6 sector codes (X/1-5) — fast overview. regr31/budr32 use 100+ detailed function codes — for breakdowns within health, social services, etc.
- Regional vs national: regr11/regr31/regr4/regr55/budr1/budr32 have a region dimension (code 0=national total, 81-85=five regions). regr63/regr64/regr65 are national totals only (no region split).
- Balance sheet: regr4 for annual detailed balance sheet by region (69 function codes, no aggregates). regr63 for quarterly national assets+liabilities with AKTIV/PASSIV totals. regr64 (liquid assets) and regr65 (long-term debt) are quarterly sub-tables of regr63.
- Cross-cutting groupings: regr55 for personnel costs, IT, payments between sectors (regions↔municipalities↔state). Not useful for total expenditure; use regr31 for that.
- Time frequency: all tables have annual data (January dates) except regr63/regr64/regr65 which are quarterly.
- Universal pitfall — prisenhed: regr11, regr31, budr1, budr32 all have LOBM (1.000 kr.) and INDL (per inhabitant) rows for every observation. Always filter prisenhed='LOBM' unless per-capita figures are needed. Forgetting this silently doubles every sum.
- Universal pitfall — art: all regnskab/budget tables have hierarchical art codes. TOT=net total, UE=gross expenditure, UI=gross incl. computed costs. Never sum across all art values — always filter to a single aggregate (usually UE for gross or TOT for net).
- The region join key differs: regr11/regr4 use omrade; regr31/regr55/budr1/budr32 use regi07. Both join to dim.nuts on kode; only niveau=1 codes (81-85) are present.
- Map: regr11, regr31, regr4, regr55, budr1, budr32 all support choropleth maps at region level via /geo/regioner.parquet. regr63/regr64/regr65 are national totals only — no map.