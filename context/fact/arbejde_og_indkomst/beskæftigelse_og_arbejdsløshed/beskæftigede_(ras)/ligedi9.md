table: fact.ligedi9
description: Ligestillingsindikator for beskæftigede lønmodtagere efter indikator, lønmodtagergruppe, branche (DB07 127-grp) og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- longrp: values [TOT=I alt, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau, 25=Lønmodtagere på mellemniveau, 30=Lønmodtagere på grundniveau, 35=Andre lønmodtagere, 40=Lønmodtagere u.n.a.]
- branchedb07127: join dim.db on branchedb07127=kode::text [approx]; levels [2, 3, 5]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- indhold is a gender indicator, NOT a count. LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). Never sum across indikator values.
- branchedb07127 uses DB07-127 coding with two hierarchy levels — same as ligedb9. Never mix both levels.
- longrp has TOT plus 6 wage earner groups.
