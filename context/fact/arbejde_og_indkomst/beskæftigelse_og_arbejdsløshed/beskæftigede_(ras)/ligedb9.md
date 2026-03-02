table: fact.ligedb9
description: Beskæftigede lønmodtagere efter køn, lønmodtagergruppe, branche (DB07 127-grp) og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- longrp: values [TOT=I alt, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau, 25=Lønmodtagere på mellemniveau, 30=Lønmodtagere på grundniveau, 35=Andre lønmodtagere, 40=Lønmodtagere u.n.a.]
- branchedb07127: join dim.db on branchedb07127=kode::text [approx]; levels [2, 3, 5]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branchedb07127 uses DB07-127 coding with two hierarchy levels: single/double-digit sector totals and 5-digit sub-sector codes — same scheme as ras300/kas300. Never mix both levels. Use ColumnValues("ligedb9", "branchedb07127") for labels.
- longrp has TOT (I alt) plus 6 wage earner groups (15, 20, 25, 30, 35, 40). Filter to TOT for all wage earners combined.
- kon has TOT, M, K.
