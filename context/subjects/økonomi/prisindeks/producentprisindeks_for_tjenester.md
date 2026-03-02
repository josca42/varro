<fact tables>
<table>
id: pris1521
description: Producentprisindeks for tjenester efter branche, enhed og tid
columns: erhverv, enhed, tid (time), indhold (unit Indeks)
tid range: 2006-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- pris1521 is the only table here. It covers quarterly producer price indices for service industries from 2006 to 2025.
- Two critical filters required for every query: (1) filter enhed to one value — 100 for the base index, 210 for quarter-on-quarter % change, 310 for year-on-year % change; (2) filter the dim.db join by d.niveau to avoid phantom matches.
- The table spans three DB07 hierarchy levels in a single column (erhverv): 8 broad service categories at niveau 2, 5 sub-groups at niveau 3, and 13 detailed groups at niveau 4. Not all service categories have sub-codes — use ColumnValues("db", "titel", for_table="pris1521") to see which codes are available before querying.
- Code 6970 (229 rows) is absent from dim.db and will be silently dropped by any JOIN.