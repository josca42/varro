table: fact.erhv1
description: Arbejdssteder, job, fuldtidsbeskæftigede og lønsum efter branche (DB07), enhed og tid
measure: indhold (unit -)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- tal: values [ARBSTED=Arbejdssteder ultimo november, ANSATTE=Job ultimo november, FULDBESK=Fuldtidsbeskæftigede, LØNSUM=Årlig lønsum (Mio. kr)]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- `tal` is a measurement selector — every row is repeated 4 times (ARBSTED, ANSATTE, FULDBESK, LØNSUM). Always filter: `WHERE f.tal = 'ANSATTE'` (or your chosen measure) or you silently quadruple counts.
- branche07 join gotcha: fact values are 6-digit zero-padded strings (e.g. '011100') while dim.db.kode is integer (11100). Text comparison misses ~8% of codes. Correct join: `JOIN dim.db d ON f.branche07::integer = d.kode`. Exclude the 'TOT' aggregate first: `WHERE f.branche07 != 'TOT'`.
- All numeric branche07 codes are at niveau=5 (the finest DB07 level). If you want broader groupings, aggregate in SQL or use erhv2/laby43 which have coarser branches.
- TOT in branche07 = all industries total. Not in dim.db — use it directly as a filter value rather than joining.
- This is the only table in this subject with LØNSUM (annual payroll in DKK millions). All other tables only have ARBSTED/ANSATTE counts.