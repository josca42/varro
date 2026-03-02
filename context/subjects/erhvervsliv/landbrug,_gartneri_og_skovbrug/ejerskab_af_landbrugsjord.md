<fact tables>
<table>
id: ejjord1
description: Ejerskab af dansk landbrugsjord efter region, enhed, land og tid
columns: region, tal, land, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2024-01-01
</table>
<table>
id: ejjord2
description: Ejerskab af dansk landbrugsjord efter ejerform, enhed, land og tid
columns: ejerform, tal, land, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2024-01-01
</table>
<table>
id: ejjord3
description: Ejerskab af dansk landbrugsjord efter arealstørrelse, enhed, land og tid
columns: arealstor, tal, land, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2024-01-01
</table>
<table>
id: ejjord4
description: Ejerskab af dansk landbrugsjord efter ejers alder, enhed, land og tid
columns: ejalder, tal, land, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: ejjord5
description: Ejerskab af dansk landbrugsjord efter køn, enhed, land og tid
columns: kon, tal, land, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All five tables cover the same universe — ownership of Danish agricultural land — broken down by a single characteristic per table: region (ejjord1), ownership type (ejjord2), parcel size (ejjord3), owner age (ejjord4), and owner gender (ejjord5). There is no single table combining all dimensions simultaneously.
- ejjord4 and ejjord5 are only available from 2022; ejjord1–ejjord3 go back to 2020. All are annual snapshots.
- Every table has a `tal` measurement selector: '100' = antal ejerskaber (count of ownerships), '110' = areal i ha. Always filter to one value — they are independent measures, not additive.
- The `land` (country of owner) column is shared across all tables and has a non-additive hierarchy: land=12 (EU) includes Denmark (land=15), so never sum land=12 and land=15. The safe partition is: land='15' (Danish) + land='10' (foreign known) + land='55' (unknown) = land='0' (total). For foreign-EU-only ownership, subtract: land=12 indhold − land=15 indhold.
- ejjord4 and ejjord5 each have a large "ikke personligt ejerskab" category (ejalder='9988', kon='UP') representing ~16% of all ownerships — these are corporate/institutional owners with no personal age or gender. When profiling individual owners, exclude or report this category separately.
- For questions about who owns the land (individuals vs. companies): ejjord2. For geographic spread: ejjord1. For farm-size distribution: ejjord3. For demographic owner profile: ejjord4 (age) or ejjord5 (gender).
- Map: ejjord1 supports choropleth at region level via context/geo/regioner.parquet — merge on region=dim_kode. Exclude region='0'.