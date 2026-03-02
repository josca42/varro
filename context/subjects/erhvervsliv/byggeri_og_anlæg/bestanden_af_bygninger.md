<fact tables>
<table>
id: bygb12
description: Bygninger efter område, ejerforhold, anvendelse, arealintervaller og tid
columns: omrade, ejer, anvend, arealint, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2025-01-01
</table>
<table>
id: bygb34
description: Bygningsbestandens areal efter område, anvendelse, arealtype, opførelsesår og tid
columns: omrade, anvend, arealtype, opforelsesar, tid (time), indhold (unit 1.000 m2)
tid range: 2011-01-01 to 2025-01-01
</table>
<table>
id: bygb40
description: Bygninger og deres opvarmede areal efter område, enhed, opvarmingsform, anvendelse, opførelsesår og tid
columns: omrade, maengde4, opvarm, anvend, opforelsesar, tid (time), indhold (unit -)
tid range: 2011-01-01 to 2025-01-01
</table>
<table>
id: bygb50
description: Bygninger og deres bebyggede areal efter område, enhed, tagdækningsmateriale, anvendelse, opførelsesår og tid
columns: omrade, maengde4, tagmat, anvend, opforelsesar, tid (time), indhold (unit -)
tid range: 2011-01-01 to 2025-01-01
</table>
<table>
id: bygb70
description: Bygninger og deres etageareal efter område, enhed, anvendelse og tid
columns: omrade, maengde4, anvend, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2025-01-01
</table>
<table>
id: bygb60
description: Bygninger og deres etageareal efter område, enhed, ydrevægsmateriale, anvendelse, opførelsesår og tid
columns: omrade, maengde4, ydremat, anvend, opforelsesar, tid (time), indhold (unit -)
tid range: 2011-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- All 6 tables share the same time range 2011-2025 (annual, January) except bygb70 which only covers 2021-2025.
- All tables have omrade (region/municipality) and anvend (building use) dimensions. Join dim.nuts and dim.byganv with WHERE d.niveau = 2 on anvend for all tables except bygb70.
- bygb70 is the only table with niveau=3 BBR building-use codes (finer breakdown: separate codes for parcelhus vs sammenbygget enfamiliehus, stald til svin vs kvæg, etc.). Use bygb70 when you need that granularity, but note it only goes back to 2021.
- bygb12 — building counts (antal) by owner type (ejer) and size band (arealint). Use for: how many buildings by municipality, owner type breakdown, size distribution.
- bygb34 — floor area (1.000 m2) by area type (arealtype: total/basement/commercial/residential) and construction period. Use for: total or residential/commercial area stock. NOTE: arealtype=1 is the total, not the sum of 2+3+4 — always filter to a specific arealtype.
- bygb40 — buildings and heated area (maengde4 selector: antal or m2) by heating type (opvarm) and construction period. Use for: heat source breakdown (fjernvarme, varmepumpe, naturgas, etc.).
- bygb50 — buildings and footprint area (maengde4 selector) by roof material (tagmat) and construction period.
- bygb60 — buildings and floor area (maengde4 selector) by wall cladding material (ydremat) and construction period.
- bygb70 — buildings and floor area (maengde4 selector) by building use at niveau=3 BBR detail. No opforelsesar dimension (unlike bygb40/50/60).
- Tables bygb40, bygb50, bygb60, bygb70 all have maengde4 as a measurement selector (45=antal, 50=areal in 1.000 m2). Always filter to one value — summing both silently combines incompatible units.
- opforelsesar (construction period) uses confusing century-wrapping 5-year codes ("05-09"=1905-1909 but "05-10"=2005-2009). Use ColumnValues to read labels rather than interpreting the codes visually.
- Map: All 6 tables support choropleth maps via omrade — context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1). Merge on omrade=dim_kode. Exclude omrade=0.