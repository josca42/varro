table: fact.tec06
description: Udenrigshandel med varer (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, ejerskab og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [IMP=Import, EXP=Eksport]
- branche: join dim.db on branche=kode::text [approx]; levels [2, 3]
- ejerskab: values [_T=I alt, D=Dansk ejede firmaer i alt, DI=Dansk ejede firmaer uden datterselskaber i udlandet, DM=Dansk ejede firmaer med datterselskaber i udlandet, F=Udenlandsk ejede firmaer, _U=Uoplyst]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Always filter indud to either 'IMP' or 'EXP'. Both directions are separate rows.
- branche has the same two-level structure as tec01: letter codes (NACE aggregates, not in dim.db) and numeric DB07 Afsnit codes (10–33, 45–47) that match dim.db at niveau 2. Always add WHERE d.niveau = 2 when joining to dim.db.
- ejerskab hierarchy: '_T' = I alt (total). 'D' = Dansk ejede firmaer i alt, which is the sum of 'DI' (without foreign subsidiaries) + 'DM' (with foreign subsidiaries). Do not sum D + DI + DM together. 'F' = Udenlandsk ejede firmaer. '_U' = Uoplyst.
- Only 2023 data. One snapshot year — no time trend possible.