table: fact.idrbes03
description: Idrætsbeskæftigelse efter branche (DB07), uddannelsesniveau, nøgletal og tid
measure: indhold (unit Antal)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- uddniv: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- bnogle: values [AARSV=Årsværk, GENST=Gennemsnitligt antal beskæftigede]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branche07 joins dim.db at niveau 5. Only 4 sports branches plus TOTR. Use ColumnValues("db", "titel", for_table="idrbes03") to see available branches.
- branche07='TOTR' is the aggregate across all branches — not in dim.db.
- bnogle is a measure selector: AARSV=årsværk, GENST=gennemsnitligt antal beskæftigede. Always filter to one bnogle value to avoid doubling.
- uddniv=TOT is total across all education levels. Individual codes (H10-H90) are subcategories.
