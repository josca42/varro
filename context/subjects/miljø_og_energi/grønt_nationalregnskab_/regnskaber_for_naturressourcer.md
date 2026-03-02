<fact tables>
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
<table>
id: vogrg
description: Værdien af olie og naturgas efter balanceposter og tid
columns: balpost, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: olierg
description: Fysisk balance for oliereserverne efter balanceposter og tid
columns: balpost, tid (time), indhold (unit Mio. m3)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: gasrg
description: Fysisk balance for naturgasreserverne efter balanceposter og tid
columns: balpost, tid (time), indhold (unit Mia. Nm3)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: fisk11
description: Fisk og skaldyr i dam- og havbrug (fysisk balance) efter balanceposter, fiske- og skaldyrsarter og tid
columns: balpost, fiskskal, tid (time), indhold (unit Ton)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: fisk33
description: Fritlevende fisk og skaldyr (fysisk balance) efter balanceposter, fiske- og skaldyrsarter og tid
columns: balpost, fiskskal, tid (time), indhold (unit Ton)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: fisk22
description: Fisk og skaldyr i dam- og havbrug (økonomisk balance) efter balanceposter, fiske- og skaldyrsarter og tid
columns: balpost, fiskskal, tid (time), indhold (unit 1.000 kr.)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: skovrg03
description: Skovareal (Kyoto) (fysisk balance) efter balanceposter, region og tid
columns: balpost, regi07, tid (time), indhold (unit Km2)
tid range: 1990-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables use a `balpost` column for balance sheet rows (primo/flows/ultimo). Never sum across all balpost codes — they include both stocks and flows, and sometimes subtotals of subtotals. Always select the specific balpost codes you need.
- Oil/gas tables (vogrg, olierg, gasrg): recent data (~2015+) is near-zero as Danish reserves are exhausted. Historical analysis is most meaningful for 1990–2010. vogrg has economic values (mio. kr.) for both oil and gas combined; olierg and gasrg have separate physical balances (Mio. m3 and Mia. Nm3 respectively). gasrg has a more granular extraction breakdown (gross vs net, breakdown by end-use).
- Fish tables come in three variants: fisk11 (aquaculture, physical, tons), fisk22 (aquaculture, economic, 1.000 kr.), fisk33 (wild fish, physical, tons). There is no economic balance table for wild fish. Species sets differ: fisk11/fisk22 cover Ørred/Laks/Ål/Muslinger; fisk33 covers Torsk/Rødspætte/Sild/Makrel/Industrifisk.
- Land area tables (arealdk, arealan1): arealdk has kommune-level detail and multi-year data (2011–2021) with land-cover classification (are1). arealan1 has only 2016 data but adds industry-sector breakdown (br19a2) and joins to dim.nuts for regional grouping. Both have an enhed selector (km2/m2-per-person/pct) that must be filtered.
- skovrg03 is the forest area table (Kyoto definition), with regional breakdown to 5 regioner, from 1990. Useful for long-run afforestation/deforestation trends.
- arealdk and arealan1 both have `enhed` as a measurement selector — forgetting to filter it multiplies results by 3.
- arealdk's are1 column has a two-level hierarchy (letter codes = subtotals of alphanumeric leaf codes). arealan1's br19a2 includes TOTAREAL. In both cases, avoid mixing parent and child codes in aggregations.
- Map support: arealdk (kommune + region level via inline omrade codes), arealan1 (region/landsdel via dim.nuts levels 1-2), skovrg03 (region via dim.nuts niveau 1) all support choropleth maps. See individual fact docs for merge details.