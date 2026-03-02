table: fact.erhv4
description: Arbejdssteder efter branche (DB07 127-grp), arbejdsstedsstørrelse og tid
measure: indhold (unit Antal)
columns:
- branchedb07127: values [TOT=TOT Erhverv i alt, 01000=01000 Landbrug og gartneri, 02000=02000 Skovbrug, 03000=03000 Fiskeri, 06000=06000 Indvinding af olie og gas ... 95000=95000 Reparation af husholdningsudstyr, 96000=96000 Frisører, vaskerier og andre serviceydelser, 97000=97000 Private husholdninger med ansat medhjælp, 99000=99000 Internationale organisationer og ambassader, 99999=99999 Uoplyst aktivitet]
- arbstrdk: values [1=1 job, 2-4=2-4 jobs, 5-9=5-9 jobs, 10-19=10-19 jobs, 20-49=20-49 jobs, 50-99=50-99 jobs, 130=100 jobs og derover]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- branchedb07127 is an inline column (no dim join) with ~127 DB07 groups. Values are 5-digit strings (e.g. '01000', '02000') plus 'TOT' = all industries total.
- No `tal` selector — indhold is always number of workplaces (ARBSTED). No job counts here; use erhv1 or erhv3 for jobs.
- arbstrdk has 7 size classes (no 'Fiktive enheder' unlike erhv3). Do NOT sum across size classes.
- This is the most granular branch breakdown (127 groups) but only for workplaces. Use ColumnValues("erhv4", "branchedb07127") to browse the ~127 branch codes and find your target.