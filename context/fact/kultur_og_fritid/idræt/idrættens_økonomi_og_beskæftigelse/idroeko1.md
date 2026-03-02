table: fact.idroeko1
description: Idrætsbranchernes økonomiske nøgletal efter branche (DB07), nøgletal og tid
measure: indhold (unit -)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- aktp: values [45=Omsætning (mio. kr.), 46=Eksport (mio. kr.), 47=Import (mio. kr.), 48=Lønsum (mio. kr.), 49=Jobs ultimo november (antal), 50=Fuldtidsbeskæftigede (årsværk)]
- tid: date range 2013-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branche07 joins dim.db at niveau 5. Only 4 branches are in this table: 931100 (Drift af sportsanlæg), 931200 (Sportsklubber), 931300 (Fitnesscentre), 931900 (Andre sportsaktiviteter). Use ColumnValues("db", "titel", for_table="idroeko1") to see them.
- branche07='TOTR' is the total across all 4 branches — not in dim.db. For national totals use TOTR; for branch breakdown filter to the individual codes.
- aktp is a measure selector, not a dimension. Each (branche07, tid) combination has 6 different measures: omsætning (45), eksport (46), import (47), lønsum (48), jobs ultimo november (49), fuldtidsbeskæftigede (50). Always filter to one aktp value. Summing across aktp mixes incompatible units.
- indhold unit is "-" because it varies by aktp: mio. kr. for 45-48, antal for 49, årsværk for 50.
