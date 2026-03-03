<fact tables>
<table>
id: erhv1
description: Arbejdssteder, job, fuldtidsbeskæftigede og lønsum efter branche (DB07), enhed og tid
columns: branche07, tal, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: erhv2
description: Arbejdssteder og job efter område, branche (DB07 10-grp), enhed og tid
columns: omrade, branchedb0710, tal, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: erhv3
description: Arbejdssteder og job efter branche (DB07 10-grp.), enhed, arbejdsstedsstørrelse og tid
columns: branche0710, tal, arbstrdk, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: erhv4
description: Arbejdssteder efter branche (DB07 127-grp), arbejdsstedsstørrelse og tid
columns: branchedb07127, arbstrdk, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: erhv5
description: Arbejdssteder efter område, sektor og tid
columns: omrade, sektor, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: erhv6
description: Arbejdssteder efter område, branche (DB07 10-grp.), arbejdsstedsstørrelse og tid
columns: omrade, branche0710, arbstrdk, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: laby43
description: Arbejdssteder, job og fuldtidsbeskæftigede efter kommunegruppe, branche (DB07), enhed og tid
columns: komgrp, branche07, tal, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All tables cover 2008–2023 (annual, measured ultimo november). No monthly or quarterly variants.
- **tal selector**: erhv1, erhv2, erhv3, and laby43 have a `tal` column that repeats every row for each measure type (ARBSTED/ANSATTE/FULDBESK/LØNSUM). Always filter `WHERE tal = '...'` or counts will be 2–4× too high.
- **For workplaces + jobs by detailed branch (DB07 finest level)**: use erhv1. The only table with lønsum (payroll) and the finest branch granularity (niveau=5 codes). Watch the leading-zero join issue: cast `branche07::integer` when joining dim.db.
- **For regional breakdown (kommune level) + branches**: use erhv2 (workplaces + jobs, 10-group branches, kommuner). For region/landsdel level use erhv6 (workplaces only, all 3 NUTS levels, also has size class).
- **For workplace size-class analysis**: erhv3 (no region, 10-group branches), erhv4 (no region, 127-group branches, workplaces only), or erhv6 (region × branch × size class). Note: arbstrdk categories are mutually exclusive — don't sum across them.
- **For public vs private sector breakdown**: erhv5 is the only table with `sektor` (7 categories). Kommune-level geography, workplaces only.
- **For kommunegruppe comparison** (urban vs rural municipality types): laby43, but only for 3 sectors (C=industri, G=handel, I=overnatning/restauranter).
- omrade='0' appears in several tables as a Denmark-total row. It is NOT in dim.nuts, so a JOIN naturally excludes it. Use it as a literal filter (`WHERE omrade = '0'`) to get national totals without aggregating.
- Map: erhv2 and erhv5 support kommune-level choropleth (/geo/kommuner.parquet). erhv6 supports all three NUTS levels (kommuner, landsdele, regioner). Merge on omrade=dim_kode; exclude omrade=0.