<fact tables>
<table>
id: gf11
description: Generel firmastatistik efter branche (DB07 10- 19- og 127-grp.), enhed og tid
columns: branchedb071019127, maengde4, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: gf12
description: Generel firmastatistik efter kommune, branche (DB07 10 19 127-grp. og detaljeret) og tid
columns: komk, branchedb0710til127, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: gf13
description: Generel firmastatistik efter branche (DB07 19-grp), enhed, firmastørrelse (fuldtidsansatte) og tid
columns: branchedb0738, enhed, firmstr, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: gf15
description: Generel firmastatistik efter branche (DB07 10-grp), virksomhedsform, enhed og tid
columns: branchedb0710, virkf1, enhed, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: laby38b
description: Generel firmastatistik efter kommunegruppe, branche (DB07 10-grp), firmaets alder og tid
columns: komgrp, branchedb0710, firmaalder, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: laby39
description: Erhvervsdemografi efter kommunegruppe, årsværk og tid
columns: komgrp, fui11, tid (time), indhold (unit Antal)
tid range: 2010 to 2024
</table>
<table>
id: gf14
description: Generel firmastatistik efter region, enhed, firmastørrelse (fuldtidsansatte) og tid
columns: region, enhed, firmstr, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fgf1
description: Foreløbig generel firmastatistik efter branche (DB07 19-grp), enhed og tid
columns: branchedb0738, maengde4, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: fgf3
description: Foreløbig generel firmastatistik efter branche (DB07 10-grp.), enhed, firmastørrelse (fuldtidsansatte) og tid
columns: branche0710, enhed, firmstr, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: fgf6
description: Foreløbig generel firmastatistik efter region, branche (DB07 10-grp), enhed og tid
columns: region, branchedb0710, enhed, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: konc11
description: Koncerner i Danmark efter koncernstørrelse (fuldtidsansatte), enhed og tid
columns: koncernstor, enhed, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2023-01-01
</table>
<table>
id: konc12
description: Koncerner i Danmark efter koncernstørrelse (firmaer), enhed og tid
columns: koncern, enhed, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2023-01-01
</table>
<table>
id: konc13
description: Aktive firmaer der indgår i koncerner efter branche (DB07 10-grp.), enhed og tid
columns: branche0710, enhed, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- Table name prefixes encode the dataset: "gf" = Generel Firmastatistik (final, 2019–2023), "fgf" = Foreløbig/preliminary (2023 only), "konc" = Koncerner/business groups (2022–2023), "laby" = labour demographics (longer range).
- For firms/employees/revenue by sector nationally: use gf13 (19-group branche + firm size), gf15 (10-group + legal form), or gf11 (all three granularity levels in one column). All require filtering enhed/maengde4 to one value to avoid tripling counts.
- For regional breakdown: gf14 (region + firm size, 2019–2023), gf12 (kommune + branche, 2019–2023), fgf6 (region + sector, 2023 only).
- For municipality-level data: only gf12 has kommuneniveau. komk joins dim.nuts; use niveau 3 for individual kommuner.
- For legal form (virksomhedsform): only gf15 has this breakdown.
- For firm size (firmstørrelse): gf13, gf14, fgf3.
- For firm age: laby38b (by kommunegruppe + sector + firm age, 2019–2023).
- For firm survival and growth: laby39 (by kommunegruppe + growth category, 2010–2024 — longest time series in this subject).
- For business group (koncern) statistics: konc11 (by employee-count size), konc12 (by firm-count size), konc13 (by sector). All cover 2022–2023 only.
- Critical gotcha shared by almost all tables: enhed (or maengde4 in gf11/fgf1) stacks firmaer/fuldtidsansatte/omsætning as separate rows. Not filtering it multiplies every count by 3.
- DB07 branche coding: letter codes (A–S, X = 19-group) do NOT join dim.db — use ColumnValues on the fact table directly. Numeric 10-group codes (1–11) match dim.db niveau 2. 127-group codes in gf11/gf12 partially match dim.db niveau 5, but zero-padded codes (e.g. 01000, 011100) do not match anything in dim.db.
- Map: gf12 (kommune/landsdel/region), gf14 (region), and fgf6 (region) support choropleth maps via /geo/kommuner.parquet, /geo/landsdele.parquet, and /geo/regioner.parquet respectively.