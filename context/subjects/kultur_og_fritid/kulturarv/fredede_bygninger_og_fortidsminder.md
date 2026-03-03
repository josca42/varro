<fact tables>
<table>
id: kfred1
description: Fredede bygninger efter område, bygningstype, opførelsesår og tid
columns: omrade, bygtyp, opforelsesar, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: kfred2
description: Fredede fortidsminder efter område, anlægskategori og tid
columns: omrade, ankat, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: kfred3
description: Nyfredninger og affredninger efter enhed, område og tid
columns: enhed, omrade, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: kv2kar1
description: Besøg på dansk kulturarv efter type af kulturarv, køn, alder og tid
columns: typkultarv, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2kar2
description: Besøg på dansk kulturarv efter formål, køn, alder og tid
columns: formal, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2kar3
description: Besøg på dansk kulturarv efter seværdighed, køn, alder og tid
columns: sevaerd, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2kar4
description: Barrierer for besøg på dansk kulturarv efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two distinct topic groups: kfred1/kfred2/kfred3 cover the stock and flow of legally protected sites (fredede bygninger and fortidsminder); kv2kar1/kv2kar2/kv2kar3/kv2kar4 cover a 2024 survey on cultural heritage visits and barriers.
- For count of protected buildings by region/type/era: use kfred1 (from 2012). Filter bygtyp='0' and opforelsesar='0' for simple regional totals. omrade=0 is the national total (not in dim.nuts).
- For count of protected antiquities (fortidsminder) by region/category: use kfred2 (from 2010). No total-category row — sum across ankat for regional totals.
- For annual changes (new protections / de-listings): use kfred3. enhed distinguishes nyfredning vs affredning for both fortidsminder and bygninger — always filter to one enhed at a time.
- All three kfred tables share the same omrade coding: 5 NUTS niveau=1 regions (81–85) plus 0=landstal. No finer geographic breakdown available.
- kv2kar1/2/3/4 are all single-year (2024) percentage tables from a cultural participation survey. All categories are non-mutually-exclusive — values will not sum to 100%. Use for comparing rates across categories or between gender/age groups, never for summing.
- kv2kar1: which types of kulturarv people visit. kv2kar2: why they visit. kv2kar3: which specific UNESCO/landmark sites they visit. kv2kar4: why non-visitors don't go (barriers).
- Map: kfred1, kfred2, kfred3 support choropleth at region level via /geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0. kv2kar tables have no geographic breakdown.
