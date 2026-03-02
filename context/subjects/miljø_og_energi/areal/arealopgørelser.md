<fact tables>
<table>
id: are207
description: Areal 1. januar efter område og tid
columns: omrade, tid (time), indhold (unit Km2)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: arealdk
description: Areal efter arealdække, område, enhed og tid
columns: are1, omrade, enhed, tid (time), indhold (unit -)
tid range: 2011-01-01 to 2021-01-01
</table>
<table>
id: arealan1
description: Arealanvendelse efter branche (19a2-gruppering), område, enhed og tid
columns: br19a2, omrade, enhed, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2016-01-01
</table>
</fact tables>

notes:
- For total land area by region or municipality over time: use are207 (2007–2025, annual, niveau 1=regioner or niveau 3=kommuner). Simplest table — only omrade and tid, no unit selector.
- For land area broken down by land cover type (arealdække): use arealdk (2011–2021). Has a hierarchical are1 column (A–H top level, sub-codes beneath). Must filter enhed to one unit (120=km2 most common) and are1 to one hierarchy level.
- For land use by industry (arealanvendelse efter branche): use arealan1 — but it only has data for 2016. Useful for a snapshot of which industries occupy land. Must filter enhed and pick one br19a2 hierarchy level.
- All tables with enhed (arealdk, arealan1) repeat every row for each of 3 units (km2, m2/inhabitant, %). Always filter WHERE enhed = '120' (or chosen unit) first.
- are207 is the only table with municipality-level (niveau 3) breakdown. arealdk has municipalities via inline omrade codes. arealan1 only goes to landsdele (niveau 2).
- Map: are207 supports kommuner/regioner choropleth (omrade=dim_kode, exclude omrade=0). arealdk supports kommuner/regioner via CAST(omrade AS INT)=dim_kode. arealan1 supports landsdele/regioner choropleth (omrade=dim_kode, exclude omrade=0).