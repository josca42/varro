table: fact.tec01
description: Udenrigshandel med varer (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, virksomhedsstørrelse og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [IMP=Import, EXP=Eksport]
- branche: join dim.db on branche=kode::text [approx]; levels [2, 3]
- virkstrrda: values [TOT=I alt, 0-9=0-9 ansatte, 10-49=10-49 ansatte, 50-249=50-249 ansatte, 250OV=250 ansatte eller derover, EJ_FORDEL=Uoplyst]
- tid: date range 2023-01-01 to 2024-01-01
dim docs: /dim/db.md

notes:
- Always filter indud to either 'IMP' or 'EXP'. The table contains both directions as separate rows — failing to filter doubles all values.
- branche contains two distinct levels mixed together: (1) letter codes (AB, C, DE, F, G, H, J, K, M, N, OTH, TOT) are custom NACE-style aggregates with no match in dim.db, and (2) numeric codes (10–33, 45–47) are DB07 Afsnit codes that join to dim.db at niveau 2. The numeric codes only cover Manufacturing (C, codes 10–33) and parts of Trade (G, codes 45–47) in detail — other letter-coded sectors have no numeric sub-breakdown.
- When joining branche to dim.db, always add WHERE d.niveau = 2. Without it, many numeric codes match at both niveau 2 and niveau 3 (e.g. code 11 matches both "Fremstilling af drikkevarer" at niveau 2 and "Dyrkning af etårige afgrøder" at niveau 3), producing duplicate rows.
- Letter codes and numeric codes are not additive with each other. C (Manufacturing aggregate) ≠ sum of codes 10–33 because the aggregate includes firms not individually classified. Use either letter codes for sector totals or numeric codes for detailed breakdown, not both in the same query.
- virkstrrda total is 'TOT'. Filter to 'TOT' unless breaking down by firm size. Size bands: 0-9, 10-49, 50-249, 250OV. EJ_FORDEL = uoplyst.
- This table has 2 years of data (2023, 2024). tec02 and tec06 only have 2023.