<fact tables>
<table>
id: fviv
description: Foreløbige nye højvækstvirksomheder efter branche (DB07 10-grp), variable og tid
columns: branchedb0710, varia, tid (time), indhold (unit -)
tid range: 2020 to 2024
</table>
<table>
id: viv
description: Nye højvækstvirksomheder efter branche (DB07 10-grp), variable og tid
columns: branchedb0710, varia, tid (time), indhold (unit -)
tid range: 2004 to 2024
</table>
<table>
id: demo11
description: Erhvervsdemografi efter branche (DB07 127-grp), status, enhed og tid
columns: branchedb07127, fstatus, enhed, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: demo13
description: Erhvervsdemografi efter branche (DB07 19-grp), enhed og tid
columns: branchedb0721, maengde4, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: demo14
description: Erhvervsdemografi efter region, branche (DB07 10-grp), enhed og tid
columns: region, branchedb0710, maengde4, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fdemo4
description: foreløbig erhvervsdemografi efter region, branche (DB07 10-grp), enhed og tid
columns: region, branchedb0710, maengde4, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: demo15
description: Erhvervsdemografi efter ejerform, enhed og tid
columns: ejerform, maengde4, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: demo16
description: Erhvervsdemografi efter branche (DB07 10-grp), enhed, startår og tid
columns: branchedb0710, enhed, startaar, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: demo18
description: Erhvervsdemografi efter firmastørrelse (fuldtidsansatte), enhed og tid
columns: firmstr, maengde4, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: demo19
description: Erhvervsdemografi efter kommune, enhed og tid
columns: regi07a, maengde4, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For high-growth firms (højvækstvirksomheder): use viv (2004–2024, confirmed) or fviv (2020–2024, preliminary). Both require filtering varia to one measurement type (A=count, B–E=employees/revenue at start/end year). tid is a 4-year rolling window, not a single year.
- For general firm demographics (erhvervsdemografi, 2019–2023): pick by breakdown needed — demo13 (by sector/21 NACE sections), demo11 (by industry/127 DST groups), demo14 (by region + industry/10 groups), demo15 (by ownership type), demo16 (survival cohorts), demo18 (by firm size), demo19 (by kommune). fdemo4 is the preliminary 2023-only version of demo14.
- maengde4 appears in demo13, demo14, fdemo4, demo15, demo18, demo19 — it is always a measurement selector. Filter to one value per query (AFU=fuldtidsansatte, NYE=nye firmaer, OPH=ophørte firmaer, OMS=omsætning mio kr.).
- demo16 is structurally different: it is a cohort survival table. startaar = founding cohort year, tid = observation year, enhed = NYE (count) or SURV (survival%). Filter to one startaar and one enhed before grouping.
- Branch dimension gotcha: demo13 uses EU NACE letter codes (A–T) — no dim join, use ColumnValues("demo13", "branchedb0721"). demo11 uses DST's own 127-group codes — no dim join, use ColumnValues("demo11", "branchedb07127"). demo14, demo16, fdemo4 use DB10 groups 1–11 and join dim.db_10 niveau 1 (the fact docs say dim.db for demo14 and demo16 but that is wrong).
- All tables with a region or kommune column include a code 0 (national total not in the dim). Exclude it when aggregating by geography.
- Map: demo19 (kommune niveau 3) → /geo/kommuner.parquet on regi07a=dim_kode. demo14 and fdemo4 (region niveau 1) → /geo/regioner.parquet on region=dim_kode.