<fact tables>
<table>
id: pris114
description: Nettoprisindeks efter varegruppe, enhed og tid
columns: varegr, enhed, tid (time), indhold (unit Indeks)
tid range: 2001-01-01 to 2025-09-01
</table>
<table>
id: pris115
description: Nettoprisindeks efter hovedtal og tid
columns: hoved, tid (time), indhold (unit Indeks)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: pris116
description: Nettoprisindeks, hovedtal efter type og tid
columns: type, tid (time), indhold (unit Indeks)
tid range: 1980-01-01 to 2025-09-01
</table>
</fact tables>

notes:
- For monthly headline NPI (long series, 1980–now): use pris116. One row per month, no filtering needed.
- For annual headline NPI (1980–2024): use pris115. Filter hoved to one value — 1005=årsgennemsnit (index level) or 1010=årsstigning (annual % change).
- For monthly NPI broken down by product group (from 2001): use pris114. Filter enhed to one value — 100=indeks, 200=månedlig ændring, 300=årlig ændring. Browse varegr codes with ColumnValues("pris114", "varegr") or fuzzy_match_str.
- pris115 and pris116 are headline-only (no product breakdown). pris114 is the only table with product-level detail.
- All three tables have a measurement-selector column (enhed or hoved) that must be filtered to a single value. Forgetting this silently multiplies row counts (×3 for pris114, ×2 for pris115).
- pris114.varegr does NOT reliably join to dim.ecoicop_dst — use ColumnValues instead. The varegr coding scheme is pris114-specific (5-digit zero-padded, with special aggregate codes like 131000, 132000, 151005).