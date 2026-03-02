table: fact.erhv2
description: Arbejdssteder og job efter område, branche (DB07 10-grp), enhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [3]
- branchedb0710: join dim.db_10 on branchedb0710=kode::text [approx]; levels [1]
- tal: values [ARBSTED=Arbejdssteder ultimo november, ANSATTE=Job ultimo november]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db_10.md, /dim/nuts.md

notes:
- `tal` is a measurement selector — every row is repeated twice (ARBSTED, ANSATTE). Always filter: `WHERE f.tal = 'ANSATTE'` to avoid doubling counts.
- omrade joins dim.nuts at niveau=3 (99 kommuner). omrade='0' = Denmark total (not in dim.nuts). omrade='950' = unknown area. Exclude these with `JOIN dim.nuts d ON f.omrade = d.kode` (the join naturally excludes them).
- branchedb0710 values 1–11 join dim.db_10 (niveau=1 only, 10 branches + "Uoplyst"). 'TOT' = all branches total, not in dim — use directly as a filter value.
- Sample: workplaces by kommune, all branches → `SELECT d.titel, f.indhold FROM fact.erhv2 f JOIN dim.nuts d ON f.omrade = d.kode WHERE f.tal = 'ARBSTED' AND f.branchedb0710 = 'TOT' AND f.tid = '2023-01-01' AND d.niveau = 3`
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.