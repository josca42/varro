<fact tables>
<table>
id: idrfac01
description: Idrætsfaciliteter efter område, facilitetstype og tid
columns: omrade, idrfac, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2025-01-01
</table>
<table>
id: laby17
description: Idrætsforeningernes medlemmer (andel af befolkningen) efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Pct.)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: idrfor01
description: Idrætsforeninger og medlemmer efter område, organisation, nøgletal og tid
columns: blstkom, organisation, aktp, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For sports facilities by geography: use idrfac01 (2017–2025, 28 facility types, landsdele or kommuner via dim.nuts).
- For membership rates (% of population): use laby17 (2014–2024, by kommunegruppe only). indhold is a percentage — do not sum.
- For club counts and member counts by geography and umbrella organisation: use idrfor01 (2014–2024, landsdele or kommuner). Always filter aktp to 104 (clubs) or 105 (members) and use organisation=100 (I alt) for deduplicated national totals — summing across organisations double-counts because clubs can belong to multiple orgs.
- All three tables have an aggregate code (omrade/komgrp=0) for the national total that is not in the dim tables. Use it directly instead of summing sub-regions.
- Both idrfac01 and idrfor01 join dim.nuts with niveau 2 (landsdele) and niveau 3 (kommuner) — always filter d.niveau to avoid mixing hierarchy levels.
- Map: idrfac01 and idrfor01 support choropleth maps via context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2). laby17 (kommunegrupper) has no geographic boundary file.