<fact tables>
<table>
id: vandind
description: Indvinding af vand efter område, vandtype, indvindingskategori og tid
columns: omrade, vandtyp, indkat, tid (time), indhold (unit Mio. m3)
tid range: 1989-01-01 to 2023-01-01
</table>
<table>
id: vandrg1
description: Indvinding af vand (Fysiske vandregnskab) efter branche, vandtype og tid
columns: erhverv, vandtyp, tid (time), indhold (unit 1.000 m3)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: vandrg2
description: Forbrug af vand (Fysiske vandregnskab) efter branche, vandtype og tid
columns: erhverv, vandtyp, tid (time), indhold (unit 1.000 m3)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: vandrg3
description: Forbrug af vand (Monetært vandregnskab) efter branche, enhed og tid
columns: erhverv, enhed, tid (time), indhold (unit Mio. kr.)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: van2mu1n
description: Direkte og indirekte vandforbrug efter branche, vandtype, multiplikator, prisenhed og tid
columns: branche, vandtyp, mult, prisenhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: van2mu2n
description: Direkte og indirekte vandforbrug efter anvendelse, vandtype, multiplikator, prisenhed og tid
columns: anvend1, vandtyp, mult, prisenhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: vandud
description: Spildevandsudledning efter område, udledning, anlægstype og tid
columns: omrade, udl, anlaeg, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: vandrg4
description: Udledning af spildevand (Fysiske vandregnskab) efter branche, udledning og tid
columns: erhverv, udl, tid (time), indhold (unit 1.000 m3)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: vandrg5
description: Udledning af spildevand (Monetært vandregnskab) efter branche, enhed og tid
columns: erhverv, enhed, tid (time), indhold (unit Mio. kr.)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: van4mu1n
description: Direkte og indirekte udledning af spildevand efter branche, udledning, multiplikator, prisenhed og tid
columns: branche, udl, mult, prisenhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: van4mu2n
description: Direkte og indirekte udledning af spildevand efter anvendelse, udledning, multiplikator, prisenhed og tid
columns: anvend1, udl, mult, prisenhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- Water abstraction (indvinding) by geography: vandind (1989–2023, regions/kommuner, by source category). By industry: vandrg1 (2010–2023). vandind is the only table with both long history and regional detail.
- Water consumption (forbrug) by industry: vandrg2 physical (1000 m3), vandrg3 monetary (Mio. kr.). vandrg2 covers own abstraction + purchased water; vandrg3 decomposes cost into BAS/AFG/MOMS/MARK.
- Wastewater discharge (spildevand) by geography: vandud (regions/kommuner, 4 pollutant types: volume, nitrogen, phosphorus, organic matter). By industry: vandrg4 physical, vandrg5 monetary.
- Supply-chain / input-output multiplier tables: van2mu1n (water consumption by production branch), van2mu2n (by final demand category), van4mu1n (wastewater by branch), van4mu2n (wastewater by final demand). Use these for footprint analysis and intensity comparisons.
- All erhverv/branche columns use V-prefixed codes (e.g. V010000) that join dim.nr_branche via: REPLACE(REPLACE(f.erhverv, 'V', ''), '_', '-') = TRIM(d.kode). The dim has 5 hierarchy levels — always filter by d.niveau to avoid cross-level double-counting. ETOT and EHUSHOLD are aggregate codes not in the dim.
- vandud.udl encodes 4 completely different pollutants with different units — always filter to one udl value; never sum across them.
- Map: vandind and vandud support choropleth maps via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
- vandrg3/vandrg5 enhed and van2mu1n/van4mu1n mult/prisenhed are selector columns — each creates separate rows for the same underlying data. Always filter each selector to one value to avoid overcounting.
