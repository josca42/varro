<fact tables>
<table>
id: hjalp1
description: Udlån af hjælpemidler efter kommune og tid
columns: kommunedk, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2024-01-01
</table>
<table>
id: hjalp2
description: Modtagere af udlån af hjælpemidler efter kommune, køn, alder og tid
columns: kommunedk, konams, alerams, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- hjalp1 = loan counts (udlån), hjalp2 = recipient counts (modtagere). These are different measures — use hjalp2 when asked about how many people receive aids, hjalp1 when asked about number of aids in circulation.
- hjalp2 adds breakdown by sex (konams) and age group (alerams); hjalp1 only has kommune and time.
- Both tables cover only 2023 and 2024 — very short series.
- Both tables have kommunedk='0' as a national aggregate not in dim.nuts. Use it directly for national totals or exclude it when joining to dim.nuts.
- When using hjalp2, always filter out the total rows to avoid overcounting: konams != 0 AND alerams != 'TOT'.
- Map: both tables support kommune-level choropleth via context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk='0'.