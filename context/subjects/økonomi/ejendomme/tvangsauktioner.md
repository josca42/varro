<fact tables>
<table>
id: tvang1
description: Bekendtgjorte tvangsauktioner efter type og tid
columns: type, tid (time), indhold (unit Antal)
tid range: 1993-01-01 to 2025-09-01
</table>
<table>
id: tvang2
description: Bekendtgjorte tvangsauktioner efter type og tid
columns: type, tid (time), indhold (unit Antal)
tid range: 1979-01-01 to 2025-07-01
</table>
<table>
id: tvang3
description: Bekendtgjorte tvangsauktioner efter område og tid
columns: omrade, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For regional breakdown at kommuneniveau: use tvang3 (2012–2024, annual, joins dim.nuts with all 3 NUTS levels). Only table with geography below region level.
- For long monthly time series by property type or region: use tvang1 (from 1993) or tvang2 (from 1979). tvang1 also has a seasonally adjusted total; tvang2 has the longer history and includes pre-2007 geographic zones (Hovedstadsregionen/Øerne/Jylland).
- All three tables: the `type` / `omrade` column encodes multiple categorizations — never sum across all values. Always pick one view (national total, by region, or by property type) and filter accordingly.
- Property type categories changed in 2018 in both tvang1 and tvang2: Erhvervsejendomme and Nedlagte landbrug were split into three finer codes. Cross-2018 comparisons of commercial property need care.
- Map: tvang3 supports choropleth maps at kommune, landsdel, or region level via context/geo/kommuner.parquet, context/geo/landsdele.parquet, or context/geo/regioner.parquet — merge on omrade=dim_kode.