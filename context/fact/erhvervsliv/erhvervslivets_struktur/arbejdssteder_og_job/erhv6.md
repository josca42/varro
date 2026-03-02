table: fact.erhv6
description: Arbejdssteder efter område, branche (DB07 10-grp.), arbejdsstedsstørrelse og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- branche0710: join dim.db_10 on branche0710=kode::text [approx]; levels [1]
- arbstrdk: values [1=1 job, 2-4=2-4 jobs, 5-9=5-9 jobs, 10-19=10-19 jobs, 20-49=20-49 jobs, 50-99=50-99 jobs, 130=100 jobs og derover]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db_10.md, /dim/nuts.md

notes:
- omrade spans all 3 NUTS niveaux: niveau=1 (5 regioner), niveau=2 (11 landsdele), niveau=3 (99 kommuner), plus omrade='0' (Denmark total). Always filter `WHERE d.niveau = X` to pick one level — mixing levels silently inflates totals.
- Unlike erhv2/erhv5 which only have niveau=3, this table supports regional aggregation from kommune up to region. Use erhv2 if you only need kommuner; use this table for landsdel or region breakdowns.
- branche0710 values 1–11 join dim.db_10 (niveau=1). 'TOT' = all branches total, not in dim.
- arbstrdk is the same 7-category size-class as erhv3 (no Fiktive enheder). Do NOT sum across categories.
- No `tal` selector — indhold is always ARBSTED (workplaces). Use ColumnValues("nuts", "titel", for_table="erhv6") to see the 115 matched regions.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.