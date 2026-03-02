table: fact.aku220k
description: Beskæftigede efter branche (DB07 10-grp.), område, køn og tid
measure: indhold (unit 1.000 personer)
columns:
- branche0710: join dim.db_10 on branche0710=kode::text [approx]; levels [1]
- omrade: join dim.nuts on omrade=kode; levels [1]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db_10.md, /dim/nuts.md

notes:
- branche0710 joins dim.db_10 at niveau 1 (11 DB07 10-groups, codes 1-11). Code TOT = all industries, not in dim. Use ColumnValues("db_10", "titel", for_table="aku220k") to see the 11 groups.
- omrade joins dim.nuts at niveau 1 only (5 regioner, codes 81-85). Code 0 = national total, not in dim.
- kon has TOT — filter kon='TOT' for the gender total to avoid overcounting.
- For a cross-tab of industry × region, filter branche0710 != 'TOT' AND omrade != '0'. Some industry/region combinations may be suppressed (small sample) and absent from the result.
- Join syntax: LEFT JOIN dim.db_10 d ON f.branche0710 = d.kode::text (kode is int in dim, string in fact).
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade='0'.