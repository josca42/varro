table: fact.idrbes01
description: Idrætsbeskæftigelse efter branche (DB07), køn, alder, nøgletal og tid
measure: indhold (unit Antal)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [IALT=Alder i alt, 250=25 år og derunder, 2649=26-49 år, 50OV=50 år og derover]
- bnogle: values [AARSV=Årsværk, GENST=Gennemsnitligt antal beskæftigede]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branche07 joins dim.db at niveau 5. Only 4 sports branches plus TOTR (total). TOTR is not in dim.db — use it for aggregated figures, join dim.db for branch-level breakdown. Use ColumnValues("db", "titel", for_table="idrbes01") to see available branches.
- bnogle is a measure selector: AARSV=årsværk, GENST=gennemsnitligt antal beskæftigede. Always filter to one. Both are present for every (branche07, kon, alder, tid) combination — selecting both doubles the count.
- kon=TOT and alder=IALT are the totals. Filter to these unless breaking down by gender or age.
- alder groups (250, 2649, 50OV) are mutually exclusive age bands that sum to IALT.
