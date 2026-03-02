<fact tables>
<table>
id: deta211
description: Detailomsætningsindeks efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Indeks)
tid range: 2000-01-01 to 2025-08-01
</table>
<table>
id: deta212
description: Detailomsætningsindeks efter varegruppe, indekstype og tid
columns: varegr, indekstype, tid (time), indhold (unit Indeks)
tid range: 2000-01-01 to 2025-09-01
</table>
</fact tables>

notes:
- Both tables are monthly indices (base year = 100) running from 2000-01-01. Neither has regional breakdown.
- deta211: use when you need industry-level detail by DB07 branche (e.g. supermarkets vs. clothing vs. internet retail). Joins dim.db at niveau=5 for 29 standard codes. Also contains DST-specific aggregate and custom codes (S-suffix) that don't join dim.db — filter to standard codes with `JOIN dim.db d ON f.branche07 = d.kode::text AND d.niveau = 5`, or use `branche07 = '4700'` for the overall retail total.
- deta212: use when you need the index split by broad merchandise group (food, clothing, other) or when you specifically need seasonally adjusted series. Always filter `indekstype` to one value (VAERDI/SVAERDI/MAENGDE/SMAENGDE) — all four series are stored for every row and forgetting this inflates results 4×.