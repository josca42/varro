<fact tables>
<table>
id: kys01
description: Kontanthjælp (sæsonkorrigeret) efter visitation, sæsonkorrigering, alder, køn og tid
columns: visitation, saeson, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: kys02
description: Kontanthjælp (sæsonkorrigeret) efter ydelsestype, sæsonkorrigering og tid
columns: ydelsestype, saeson, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: ky01
description: Kontanthjælp (personer) efter visitation, alder, køn og tid
columns: visitation, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: ky12
description: Kontanthjælp (personer) efter ydelsestype, alder, køn og tid
columns: ydelsestype, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: ky13
description: Kontanthjælp (personer og beløb) efter enhed, ydelsestype, visitation og tid
columns: tal, ydelsestype, visitation, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: ky04
description: Kontanthjælp (personer og beløb) efter område, enhed, visitation og tid
columns: omrade, tal, visitation, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: ky15
description: Kontanthjælp (personer og beløb) efter enhed, ydelsestype (detaljeret) og tid
columns: tal, ydtypdetal, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-06-01
</table>
<table>
id: ky16
description: Kontanthjælp (personer og beløb) efter område, enhed, ydelsestype og tid
columns: omrade, tal, ydelsestype, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-06-01
</table>
<table>
id: ky031
description: Kontanthjælp (personer og beløb) efter enhed, visitation, alder, køn og tid
columns: tal, visitation, alder, kon, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky032
description: Kontanthjælp (personer og beløb) efter enhed, ydelsestype, alder, køn og tid
columns: tal, ydelsestype, alder, kon, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky033
description: Kontanthjælp (personer og beløb) efter enhed, ydelsestype, visitation og tid
columns: tal, ydelsestype, visitation, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky034
description: Kontanthjælp (personer og beløb) efter enhed, område og tid
columns: tal, omrade, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky035
description: Kontanthjælp (helårsmodtagere) efter område, visitation og tid
columns: omrade, visitation, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky036
description: Kontanthjælp detaljeret (personer og beløb) efter enhed, ydelsestype og tid
columns: tal, ydelsestype, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: ky037
description: Kontanthjælp (personer og beløb) efter enhed, ydelsestype, familietype og tid
columns: tal, ydelsestype, famtype, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky038
description: Kontanthjælp (helårsmodtagere) efter område, ydelsestype, national oprindelse, herkomst og tid
columns: omrade, ydelsestype, herkomst1, herkomst, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky050
description: Hjælp i særlige tilfælde (personer og beløb) efter enhed, ydelsestype, alder, køn og tid
columns: tal, ydelsestype, alder, kon, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ky051
description: Hjælp i særlige tilfælde (personer og beløb) efter område, enhed, ydelsestype og tid
columns: omrade, tal, ydelsestype, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Two table families by recency: monthly tables (2007–2025-06): kys01, kys02, ky01, ky12, ky13, ky04, ky15, ky16. Annual tables (2007–2024): ky031–ky038, ky050, ky051.

- For current monthly recipients — simplest tables: ky01 (by visitation+age+gender), ky12 (by ydelsestype+age+gender), ky13 (by ydelsestype+visitation, also payments).

- For regional breakdown: ky04 (monthly, visitation), ky16 (monthly, ydelsestype), ky034/ky035 (annual). ky035 is helårsmodtagere only; ky034 has persons+payments+helårs.

- For payments (beløb): all tables with a tal column include tal=3=Udbetalt beløb (1.000 kr.). ky01 and ky12 are persons-only (no tal column).

- tal column is a critical measurement selector in all ky0xx tables: 1=Berørte personer, 2=Helårsmodtagere, 3=Udbetalt beløb. Not all tables have all 3 values (ky13/ky04/ky15/ky16 have only 1 and 3; ky031–ky038/ky050/ky051 have all 3). Always filter tal to one value.

- kys01/kys02 are the seasonal-adjustment tables. They have a saeson selector (10=korrigeret, 20=faktiske tal) instead of tal. Use for trend analysis; for raw counts prefer ky01/ky12.

- Detailed ydelsestype (573xxx, 579xxx codes): use ky15 (monthly, from 2016) or ky036 (annual, 2016–2024). All other tables use summary codes (10xxx).

- Unique breakdowns only available in annual (ended 2024) tables: familietype→ky037, herkomst/national origin→ky038 (note: herkomst codes 10/20/30/40 ≠ dim.herkomst codes, do not join dim).

- Hjælp i særlige tilfælde (special one-off benefits) is a distinct benefit type in ky050/ky051 — not regular kontanthjælp. These use KST and 572xxx ydelsestype codes and include age 0–15.

- All tables with a regional (omrade) column: omrade=0=Hele landet and omrade=997=Udlandet are not in dim.nuts. Exclude these rows when joining dim.nuts or handle as special aggregates.

- Map: Tables ky04, ky16, ky034, ky035, ky038, ky051 support choropleth maps at kommune (niveau 3), landsdel (niveau 2), or region (niveau 1) level via context/geo/ parquet files — merge on omrade=dim_kode.
