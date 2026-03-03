table: fact.pend101
description: Beskæftigede (ultimo november) efter område, branche (DB07), pendling, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [1]
- pendling: values [NAT=Natbefolkning (bopælskommune), IND=Indpendling, UD=Udpendling, DAG=Dagbefolkning (arbejdsstedskommune)]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db_10.md, /dim/nuts.md

notes:
- omrade is ONLY at niveau 3 (99 kommuner). There are no region or landsdel totals in this table — for regional summaries, aggregate kommuner in SQL.
- branche07 stores values as text (e.g. '1', '10', 'TOT'). Join to dim.db_10 with f.branche07::int = d.kode, filtering to niveau=1 (10 sectors + 11=Uoplyst). 'TOT' is the all-sectors total and is NOT in dim.db_10 — filter it out or handle separately.
- pendling has 4 distinct measure types: NAT=natbefolkning (residents of the municipality), IND=indpendlere (workers commuting in), UD=udpendlere (residents commuting out), DAG=dagbefolkning (workers located there). These are not additive — pick exactly one type per query.
- kon has only M and K (no TOT). Sum both to get total employed.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.