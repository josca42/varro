<fact tables>
<table>
id: vej22
description: Motorkøretøjer pr. døgn efter vejstrækning og tid
columns: vejstr, tid (time), indhold (unit Antal)
tid range: 1988-01-01 to 2024-01-01
</table>
<table>
id: vej23
description: Trafikarbejdet med danske køretøjer på danske veje efter transportmiddel og tid
columns: transmid, tid (time), indhold (unit Mio. køretøjskm)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: vej11
description: Vejnet efter landsdel, vejtype og tid
columns: landdel, vejtype, tid (time), indhold (unit Km)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: vej2
description: Investeringer i vejnettet efter investeringstype, enhed og tid
columns: invest, enhed, tid (time), indhold (unit Mio. kr.)
tid range: 1990-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- vej22: daily vehicle counts (Antal/day) at 197 specific road segments, 1988–2024. Use for point-specific traffic intensity. No overcounting risk, but vejstr codes are opaque — use ColumnValues("vej22", "vejstr") to find the segment you want.
- vej23: total traffic volume (Mio. køretøjskm) by vehicle type, national level only, 2000–2024. Good for modal split or trend questions. transmid is hierarchical — always filter to a single level (e.g. transmid='0' for total, or a non-overlapping set of sub-categories).
- vej11: road network length (km) by landsdel and road type, 2007–2024. Only table with regional breakdown. landdel joins dim.nuts at niveau=2 (11 landsdele); vejtype has 3-tier hierarchy (filter to one level).
- vej2: road investment (Mio. kr.) by investment type and price base, 1990–2022. enhed is a price-base selector (årets priser / 1995-priser / 2000-priser) — must always filter to one value or counts triple. Best default: enhed='2004' (årets priser, full time range).
- Map: only vej11 has a geographic breakdown (landdel at niveau 2). Use context/geo/landsdele.parquet — merge on landdel=dim_kode, exclude landdel='0'.