<fact tables>
<table>
id: km4
description: Kirkelige handlinger efter sogn, bevægelse og tid
columns: sogn, bevaegelsev, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: km44
description: Kirkelige handlinger efter provsti, bevægelse og tid
columns: provsti, bevaegelsev, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two tables covering the same data at different geographic granularities: km4 by sogn (2,297 parishes), km44 by provsti (112 deaneries). Same bevaegelsev values and time range (2006–2024) in both.
- Pick based on geographic need: parish-level detail → km4; provsti-level aggregation → km44. Neither has a higher-level stift column — stift can be derived from the provsti code (first digit × 100).
- bevaegelsev drives what you're counting. Key groupings: baptisms (1+2+3), weddings (5+6), deaths (9), burials by type (10–15), confirmations (16), births (17). Never sum all 17 — they measure unrelated events.
- Burial sub-types (10–15) sum to approximately the same total as bevaegelsev=9 (deaths). Do not add 9 and 10–15 together — that double-counts.
- km4 includes special sogne codes 4001–4007 (civil registry offices for Sønderjylland) and residual codes 0 and 9999 — filter these out for purely ecclesiastical analysis.
- Map: km4 supports choropleth maps at parish level via context/geo/sogne.parquet — merge on sogn=dim_kode. Exclude 0, 9999, 4001–4007. km44 (provsti) has no matching geo file.