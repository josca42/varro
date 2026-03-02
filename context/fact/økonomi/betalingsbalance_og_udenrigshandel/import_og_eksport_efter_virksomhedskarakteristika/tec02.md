table: fact.tec02
description: Udenrigshandel med varer (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, poster og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [IMP=Import, EXP=Eksport]
- branche: join dim.db on branche=kode::text [approx]; levels [2, 3]
- post: values [1.A.A=VARER, 1.A.A.1.0-4X2-3=Næringsmidler, drikkevarer, tobak mv., 1.A.A.1.2=Råstoffer, ikke spiselige, undt. brændsel, 1.A.A.1.3=Mineral, brændsels- og smørestoffer o.l., 1.A.A.1.5=Kemikalier og kemiske produkter, 1.A.A.1.6=Forarbejdede varer, primært halvfabrikata, 1.A.A.1.7X78-79=Maskiner, undt. transportmidler, 1.A.A.1.78-79=Transportmidler undt. Skibe og fly, 1.A.A.1.SOGF=Skibe, fly mv., 1.A.A.1.8-9=Færdigvarer og andre varer, _U=Uoplyst]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Always filter indud to either 'IMP' or 'EXP'. Both directions are separate rows.
- branche has the same two-level structure as tec01: letter codes (NACE aggregates, not in dim.db) and numeric DB07 Afsnit codes (10–33, 45–47) that match dim.db at niveau 2. Always add WHERE d.niveau = 2 when joining to dim.db.
- post is hierarchical: '1.A.A' = VARER (all goods, the total). The sub-items (1.A.A.1.0-4X2-3, 1.A.A.1.2, etc.) are individual goods categories. Filter to '1.A.A' for a sector total, or to individual sub-codes for breakdown by goods type. Do not sum sub-codes together with the parent '1.A.A' row.
- Only 2023 data available. For a time series by goods type, this table cannot be used — see tec01 for 2023–2024 but without goods-type breakdown.