table: fact.demo14
description: Erhvervsdemografi efter region, branche (DB07 10-grp), enhed og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode; levels [1]
- branchedb0710: join dim.db on branchedb0710=kode::text [approx]; levels [2, 3]
- maengde4: values [AFU=Fuldtidsansatte (antal), OPH=Ophørte firmaer (antal), OMS=Omsætning (mio kr.) , NYE=Nye firmaer (antal)]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md, /dim/nuts.md

notes:
- branchedb0710 is documented as joining dim.db but actually joins dim.db_10 at niveau 1. Use: JOIN dim.db_10 d ON f.branchedb0710 = d.kode::text AND d.niveau = 1. Codes are 1–11 plus TOT (national total not in the dim). The dim.db join (levels 2,3) is wrong for this table.
- region: code 0 = national total (not in dim.nuts); codes 81–85 = the 5 regions (dim.nuts niveau 1). Filter region != 0 when summing by region to avoid double-counting with the national total.
- maengde4 is a measurement selector — filter to one value per query: AFU=fuldtidsansatte, NYE=nye firmaer, OPH=ophørte firmaer, OMS=omsætning (mio kr.).
- Only table in this subject with simultaneous region + branch breakdown. Use it for regional comparisons by industry.
- Map: /geo/regioner.parquet — merge on region=dim_kode. Exclude region=0.