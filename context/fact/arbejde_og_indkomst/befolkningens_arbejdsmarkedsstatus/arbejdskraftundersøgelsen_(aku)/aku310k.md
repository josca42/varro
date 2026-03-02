table: fact.aku310k
description: Overarbejde for lønmodtagere efter aflønningsstatus, branche (DB07 10-grp.) og tid
measure: indhold (unit 1.000 personer)
columns:
- aflon: values [1=Betalt overarbejde, 2=Ubetalt overarbejde]
- branche0710: join dim.db_10 on branche0710=kode::text [approx]; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db_10.md

notes:
- branche0710 joins dim.db_10 at niveau 1 (11 DB07 industry groups, codes 1-11). Code TOT = all industries, not in dim. Filter branche0710 != 'TOT' to work with individual industries.
- aflon only has 2 values (betalt/ubetalt) — mutually exclusive, no total row. To get all overtime, sum across both or don't filter on aflon.
- Join syntax: LEFT JOIN dim.db_10 d ON f.branche0710 = d.kode::text.