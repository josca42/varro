table: fact.musik4
description: Autorers indtægter fra musikrettigheder efter køn, alder, område og tid
measure: indhold (unit Kr.)
columns:
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [9920=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- omrade: join dim.nuts on omrade=kode [approx]; levels [1]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=1 (5 regioner: 81–85). omrade=99 is not in dim.nuts — it represents authors whose income cannot be attributed to a Danish region.
- omrade=99 is NOT a national total. Sum all omrade values (81–85 + 99) to get national totals.
- kon has no total row (only 1=Mænd, 2=Kvinder). Safe to sum both for total.
- alder has no total row — 7 age groups (9920, 2029, 3039, 4049, 5059, 6069, 7099) are exhaustive. Safe to sum all for a total across ages.
- All 4 dimension columns (kon, alder, omrade, tid) must be grouped/filtered explicitly — forgetting omrade=99 in a SUM will undercount national totals.
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Filter omrade IN (81,82,83,84,85) before merging; exclude omrade=99.