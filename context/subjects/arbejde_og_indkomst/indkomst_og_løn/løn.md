<fact tables>
<table>
id: lons30
description: Løn efter område, sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
columns: omrade, sektor, afloen, longrp, lonmal, kon, tid (time), indhold (unit Kr.)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: lons40
description: Løn efter branche (DB07), sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
columns: branche07, sektor, afloen, longrp, lonmal, kon, tid (time), indhold (unit Kr.)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: lons60
description: Fortjeneste pr. præsteret time efter branche (DB07), alder, køn, lønkomponenter og tid
columns: branche07, alder, kon, lonmal, tid (time), indhold (unit Kr.)
tid range: 2002-01-01 to 2024-01-01
</table>
<table>
id: lons50
description: Løn efter alder, sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
columns: alder1, sektor, afloen, longrp, lonmal, kon, tid (time), indhold (unit Kr.)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: lons11
description: Løn efter uddannelse, sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
columns: uddannelse, sektor, afloen, longrp, lonmal, kon, tid (time), indhold (unit Kr.)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: ligelb1
description: Lønniveau efter arbejdssted/bopæl, område, alder, køn, familietype og tid
columns: arbbop, omrade, alder, kon, famtyp, tid (time), indhold (unit Kr.)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: sblon1
description: Standardberegnet lønindeks efter branche (DB07), sektor, enhed og tid
columns: branche07, sektor, varia1, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: sblon2
description: Standardberegnet lønindeks efter arbejdsfunktion, sektor, enhed og tid
columns: arbfunk, sektor, varia1, tid (time), indhold (unit Indeks)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: ilon12
description: Implicit lønindeks for virksomheder og organisationer efter branche, sæsonkorrigering og tid
columns: erhverv, saeson, tid (time), indhold (unit Indeks)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ilon15
description: Årlig ændring i timefortjenesten for virksomheder og organisationer efter branche og tid
columns: erhverv, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ilon22
description: Implicit lønindeks for den statslige sektor efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Indeks)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ilon25
description: Årlig procentvis ændring i timefortjenesten for statsansatte efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ilon32
description: Implicit lønindeks for kommuner og regioner efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Indeks)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ilon35
description: Årlig procentvis ændring i timefortjenesten for ansatte i kommuner og regioner efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ilon42
description: Implicit lønindeks og ændring i timefortjenesten for kommuner efter enhed, branche (DB07) og tid
columns: enhed, branche07, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: ilon52
description: Implicit lønindeks og ændring i timefortjenesten for regioner efter enhed, branche (DB07) og tid
columns: enhed, branche07, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: ligeli1
description: Ligestillingsindikator for løngab efter indikator og tid
columns: indikator, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: ligeli2
description: Ligestillingsindikator for løngab efter indikator, arbejdsfunktion, alder og tid
columns: indikator, arbfunk, alder, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: ligeli3
description: Ligestillingsindikator for løngab efter indikator, arbejdstidens omfang, alder og tid
columns: indikator, arbomfang, alder, tid (time), indhold (unit Pct.)
tid range: 2009-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- For actual wage levels (kr/hour or kr/month), use the lons* tables. For wage indices and growth rates, use sblon* or ilon* tables.

**Picking a lons* table by breakdown dimension:**
- By region (5 regions): lons30 — joins dim.nuts niveau 1. Annual 2013-2024.
- By industry (DB07): lons40 — use ColumnValues for branche07 (do NOT join dim.db). Annual 2013-2024.
- By age group: lons50 — inline alder1 bands. Annual 2013-2024.
- By education: lons11 — inline uddannelse with 2-level hierarchy (3-char vs 5-char codes). Annual 2015-2024 (shortest series).
- By age+industry (private sector only, longer history): lons60 — from 2002, no sektor/afloen/longrp dimensions.
- By municipality + family type: ligelb1 — joins dim.nuts niveau 3 (98 kommuner). Also has arbbop (work vs home municipality). Annual 2009-2024.

**lonmal is universal across all lons* tables:** Every dimension combination is repeated for each of 25 measurement types. ALWAYS filter lonmal to one value before aggregating. FORINKL=total hourly earnings is the standard starting point. ANTAL is headcount (different unit entirely).

**sektor overlapping aggregates (all lons* except lons60):** 1000=all, 1032=public (=1016+1018), 1046=private. Never sum across sektor values.

**dim.db joins are WRONG for branche07/erhverv columns:** lons40, lons60, sblon1, ilon12, ilon15 all document a dim.db join, but the numeric codes (1-10) in those tables refer to DST sector aggregates, not DB07 sub-groups. Joining to dim.db returns completely wrong labels. Use ColumnValues on the fact table directly.

**Wage index tables (ilon*) by sector:**
- Private sector (virksomheder og organisationer): ilon12 (index) + ilon15 (pct change). Quarterly from 2005. Has saeson selector.
- State sector (statslig): ilon22 (index) + ilon25 (pct change). Quarterly from 2005.
- Kommuner+regioner: ilon32 (index) + ilon35 (pct change). Quarterly from 2005.
- Kommuner alone: ilon42 (index+pct in one table via enhed column). From 2007.
- Regioner alone: ilon52 (index+pct via enhed). From 2007. Very narrow — only 4 industries.

**Standardised wage index (sblon*):**
- sblon1: by industry + sector. sblon2: by occupation (ISCO major groups) + sector. Both quarterly from 2016. varia1 is a selector (index vs pct change) — always filter to one value.

**Gender pay gap (ligeli*):**
- ligeli1: national trend only, annual from 2004.
- ligeli2: by occupation (ISCO, 4 levels) + age. From 2010. arbfunk has 601 codes across 4 levels — filter to one level.
- ligeli3: by full/part-time + fine age bands. From 2009.
- All ligeli tables: indikator is a measurement-type selector (women's share vs gap pct) — always filter to one value.
- Map: lons30 supports choropleth at region level (/geo/regioner.parquet, omrade=dim_kode). ligelb1 supports choropleth at kommune level (/geo/kommuner.parquet, omrade=dim_kode). Both exclude omrade=0.
