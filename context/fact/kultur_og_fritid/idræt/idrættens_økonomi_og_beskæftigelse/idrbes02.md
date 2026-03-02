table: fact.idrbes02
description: Idrætsbeskæftigelse efter branche (DB07), funktion, nøgletal og tid
measure: indhold (unit Antal)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- funktion: values [980=Alle funktioner, 900=Almindeligt kontorarbejde, 910=Andet manuelt arbejde, 920=Andre arbejdsfunktioner og udefineret, 930=Fitnessinstruktør, 940=Ledelsesarbejde, 950=Service- og salgsarbejde, 960=Sportsudøvere, 970=Træner- instruktør- og dommerarbejde inden for sport]
- bnogle: values [AARSV=Årsværk, GENST=Gennemsnitligt antal beskæftigede]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branche07 joins dim.db at niveau 5. Only 4 sports branches plus TOTR. Use ColumnValues("db", "titel", for_table="idrbes02") to see available branches.
- branche07='TOTR' is the aggregate across all branches — not in dim.db.
- bnogle is a measure selector: AARSV=årsværk, GENST=gennemsnitligt antal beskæftigede. Always filter to one bnogle value to avoid doubling.
- funktion=980 is total across all job functions. Individual functions (900-970) are subcategories. For an overall employment figure filter funktion='980'.
