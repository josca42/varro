<fact tables>
<table>
id: ls01
description: Ledige stillinger efter branche, enhed, størrelse og tid
columns: branche, enhed, storrelse, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: ls02
description: Ledige stillinger efter region, enhed og tid
columns: region, enhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: lsk01
description: Ledige stillinger efter branche, enhed, størrelse og tid
columns: branche, enhed, storrelse, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2025-04-01
</table>
<table>
id: lsk02
description: Ledige stillinger efter region, enhed og tid
columns: region, enhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2025-04-01
</table>
<table>
id: lsk03
description: Ledige stillinger (sæsonkorrigeret) efter enhed, sæsonkorrigering og tid
columns: enhed, saeson, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- Naming convention: ls* = annual (one observation per year, up to 2024), lsk* = quarterly (Jan/Apr/Jul/Oct, up to 2025-Q1). Prefer lsk tables for recent or high-frequency data.
- By industry/size: use ls01 (annual) or lsk01 (quarterly). Both have branche (6 sectors) and storrelse (firm size).
- By region: use ls02 (annual) or lsk02 (quarterly). Both have 5-region NUTS breakdown. Note: region code 1 is the national total — do NOT treat it as Landsdel Byen København despite matching dim.nuts kode=1.
- Seasonally adjusted national series: only lsk03. It has no industry or regional breakdown, just enhed + saeson.
- All tables have enhed as a measurement selector (LS=antal, ALS=procent). Always filter to one — mixing doubles the data. ALS values are percentages and must never be summed across dimensions.
- branche and storrelse both have a code 0 = I alt row. Always exclude code 0 when aggregating across categories to avoid double-counting.
- lsk03 has an additional saeson selector (Sæsonkorrigeret vs Faktiske tal) that must also be filtered to one value.
- Map: ls02 and lsk02 support regional choropleth via /geo/regioner.parquet — merge on region=dim_kode, filter to region IN ('81','82','83','84','85').