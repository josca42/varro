table: fact.aku120k
description: Arbejdsmarkedstilknytning efter beskæftigelsesstatus, område og tid
measure: indhold (unit 1.000 personer)
columns:
- beskstatus: values [BESTOT=Beskæftigede, AKUL=AKU-ledige, UARBST=Uden for arbejdsstyrken]
- omrade: join dim.nuts on omrade=kode; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 only (5 regioner: 81=Nordjylland, 82=Midtjylland, 83=Syddanmark, 84=Hovedstaden, 85=Sjælland). Code 0 = national total, not in dim. Use ColumnValues("nuts", "titel", for_table="aku120k") to see the 5 regions.
- Quarterly data (tid steps quarterly: 2008-01-01, 2008-04-01, ...). For annual comparison use the annual table aku110a.
- 3 beskstatus values (BESTOT, AKUL, UARBST) are mutually exclusive labour market categories — never sum across all three. Pick the category you need, or sum all three to get the 15-74 population.
- For a region-level breakdown, filter omrade != '0' to exclude the national aggregate.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade='0'.