table: fact.stec02
description: Udenrigshandel med tjenester (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, ejerskab og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [IMP=Import, EXP=Eksport]
- branche: join dim.db on branche=kode::text [approx]
- ejerskab: values [_T=I alt, D=Dansk ejede firmaer i alt, DI=Dansk ejede firmaer uden datterselskaber i udlandet, DM=Dansk ejede firmaer med datterselskaber i udlandet, F=Udenlandsk ejede firmaer, _U=Uoplyst]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Always filter indud to either 'IMP' or 'EXP'. Both directions are separate rows.
- branche contains only letter codes — do not join to dim.db. Use branche values directly as inline categories ('_T' = total, '_U' = uoplyst, '_O' = other).
- ejerskab hierarchy same as tec06: '_T' = I alt, 'D' = Dansk ejede i alt = 'DI' + 'DM' (do not sum all three). 'F' = Udenlandsk ejede. '_U' = Uoplyst.
- Only 2023 data.