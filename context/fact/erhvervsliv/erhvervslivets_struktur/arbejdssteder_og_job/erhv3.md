table: fact.erhv3
description: Arbejdssteder og job efter branche (DB07 10-grp.), enhed, arbejdsstedsstørrelse og tid
measure: indhold (unit Antal)
columns:
- branche0710: join dim.db_10 on branche0710=kode::text [approx]; levels [1]
- tal: values [ARBSTED=Arbejdssteder ultimo november, ANSATTE=Job ultimo november]
- arbstrdk: values [1=1 job, 2-4=2-4 jobs, 5-9=5-9 jobs, 10-19=10-19 jobs, 20-49=20-49 jobs, 50-99=50-99 jobs, 130=100 jobs og derover, 135=Fiktive enheder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db_10.md

notes:
- `tal` is a measurement selector — every row is repeated twice (ARBSTED, ANSATTE). Always filter to one value.
- branche0710 values 1–11 join dim.db_10 (niveau=1). 'TOT' = all branches total, not in dim.
- arbstrdk is an inline size-class column with 8 mutually exclusive categories: 1, 2-4, 5-9, 10-19, 20-49, 50-99, 130 (100+), 135 (Fiktive enheder). Do NOT sum across arbstrdk values — they already partition all workplaces. Filter to one category or sum the specific subset you want.
- arbstrdk='135' (Fiktive enheder) covers administrative registrations with no physical workplace. Typically exclude this when studying actual workplaces.
- No regional breakdown — national totals only. For regional data use erhv6.