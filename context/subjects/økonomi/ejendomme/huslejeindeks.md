<fact tables>
<table>
id: hus1
description: Huslejeindeks for boliger efter region, ejendomskategori, enhed og tid
columns: region, ejendomskate, tal, tid (time), indhold (unit Indeks)
tid range: 2021-01-01 to 2025-07-01
</table>
<table>
id: erhejd1
description: Lejeindeks for erhvervsejendomme (eksperimentel statistik) efter ejendomskategori, enhed og tid
columns: ejendomskate, tal, tid (time), indhold (unit Indeks)
tid range: 2021-01-01 to 2025-07-01
</table>
<table>
id: laby32
description: Huslejeindeks for boliger efter kommunegruppe, enhed og tid
columns: komgrp, tal, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2025-07-01
</table>
</fact tables>

notes:
- All three tables share the same `tal` measurement selector (100=Indeks, 210=QoQ change%, 310=YoY change%). Always filter to one `tal` value — mixing them produces meaningless aggregates.
- For residential rent by region (5 regioner): use **hus1**. It also has ejendomskategori breakdown (Boliger i alt / Private / Almene / Andelsboliger). Note: Andelsboliger only has national-level data, no regional split.
- For residential rent by kommunegruppe (5 groups: Hovedstad, Storby, Provinsby, Opland, Land): use **laby32**. No ejendomskategori breakdown.
- For commercial property rent (Kontor, Butik, Industri): use **erhejd1**. National level only, no regional breakdown. Experimental statistics — treat as indicative.
- All tables cover 2021–2025 (quarterly). No table has longer historical coverage or finer time granularity.
- All tables include a national total as code `0` (not in the relevant dim table). Filter out or handle separately when joining dims.
- Map: **hus1** supports choropleth at region level — /geo/regioner.parquet, merge on region=dim_kode. **laby32** and **erhejd1** have no geographic join (kommunegrupper and national-only).