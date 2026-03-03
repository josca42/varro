table: fact.strafna7
description: Skyldige personer efter område, overtrædelsens art og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- overtraed: join dim.overtraedtype on overtraed=kode [approx]; levels [1, 3]
- tid: date range 2005-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/overtraedtype.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). Code 0 (I alt) is not in the dim. Filter WHERE d.niveau=1 or niveau=3 to pick granularity.
- overtraed covers ONLY Straffelov — both niveau 1 and 3 appear as separate rows. Filter WHERE d.niveau=3 (or niveau=1) to avoid double-counting across overtraed levels.
- Both dimensions mix aggregate and detail rows simultaneously, so always specify niveau filters for both omrade and overtraed joins.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
- Map: kommune data (niveau 3) can be aggregated to politikredse via dim.politikredse (niveau 2 = kommuner, niveau 1 = 12 politikredse). Use /geo/politikredse.parquet for boundaries.
