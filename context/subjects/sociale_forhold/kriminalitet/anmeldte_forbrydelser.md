<fact tables>
<table>
id: straf10
description: Anmeldte forbrydelser efter overtrædelsens art og tid
columns: overtraed, tid (time), indhold (unit Antal)
tid range: 1995-01-01 to 2025-07-01
</table>
<table>
id: straf11
description: Anmeldte forbrydelser efter område, overtrædelsens art og tid
columns: omrade, overtraed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-07-01
</table>
<table>
id: straf20
description: Anmeldte forbrydelser og sigtelser efter overtrædelsens art, anmeldte og sigtede og tid
columns: overtraed, anmsigt, tid (time), indhold (unit Antal)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: straf22
description: Anmeldte forbrydelser og sigtelser efter område, overtrædelsens art, anmeldte og sigtede og tid
columns: omrade, overtraed, anmsigt, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: straf24
description: Anmeldte forbrydelser pr. 100.000 indbyggere efter overtrædelsens art og tid
columns: overtraed, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For simple crime counts over time (no geography): straf10 (1995–2025, longest series). For reported + charged in one query: straf20 (1995–2024).
- For regional breakdown: straf11 (counts, 2007–2025) or straf22 (counts + reported/charged split, 2007–2024). Neither has landsdele — only regioner (niveau 1) and kommuner (niveau 3).
- For crime rates (per 100,000 inhabitants): straf24 (2018–2024 only, national level only, no regional version).
- All tables share the overtraed dimension (dim.overtraedtype). The fact tables contain niveaux 1, 2, and 3 simultaneously — always filter to a single niveau to avoid double-counting. overtraed='TOT' is a grand-total placeholder not present in the dim table.
- Færdselslov (traffic offenses, kode=2) is absent from all tables in this subject — only Straffelov and Særlov are covered.
- In regional tables (straf11, straf22): omrade=0 is the national total, omrade=998 is unknown location — exclude both when doing geographic analysis.
- anmsigt in straf20/straf22: ANM=reported crimes, SIG=charges. Always filter to one — never sum across both.
- Map: straf11 and straf22 support choropleth maps at kommune (niveau 3) and region (niveau 1) level via context/geo/kommuner.parquet and context/geo/regioner.parquet. Kommune data can also be aggregated to 12 politikredse via dim.politikredse (parent_kode) and mapped with context/geo/politikredse.parquet.