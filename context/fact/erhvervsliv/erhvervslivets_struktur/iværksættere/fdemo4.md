table: fact.fdemo4
description: foreløbig erhvervsdemografi efter region, branche (DB07 10-grp), enhed og tid
measure: indhold (unit Antal)
columns:
- region: join dim.nuts on region=kode; levels [1]
- branchedb0710: join dim.db_10 on branchedb0710=kode::text [approx]; levels [1]
- maengde4: values [AFU=Fuldtidsansatte (antal), NYE=Nye firmaer (antal)]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db_10.md, /dim/nuts.md

notes:
- Single year of preliminary data (2023 only). Use demo14 for the confirmed 2019–2023 series.
- branchedb0710 joins dim.db_10 at niveau 1 (koder 1–11). TOT is a national aggregate not in the dim — exclude it when joining. JOIN dim.db_10 d ON f.branchedb0710 = d.kode::text AND d.niveau = 1.
- region: code 0 = national total (not in dim.nuts); codes 81–85 = 5 regioner (dim.nuts niveau 1). Exclude region = 0 when aggregating by region.
- maengde4 has only AFU and NYE (no OPH or OMS unlike demo14) — filter to one per query.
- Map: /geo/regioner.parquet — merge on region=dim_kode. Exclude region=0.