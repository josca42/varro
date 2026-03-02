table: fact.stec01
description: Udenrigshandel med tjenester (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, virksomhedsstørrelse og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [IMP=Import, EXP=Eksport]
- branche: join dim.db on branche=kode::text [approx]
- virkstrrda: values [_T=I alt, E0T49=0-49 ansatte, E50T249=50-249 ansatte, EGE250=250 ansatte og derover, _U=Uoplyst]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Always filter indud to either 'IMP' or 'EXP'. Both directions are separate rows.
- branche contains only letter codes (AB, C, DE, F, G, H, J, K, M, N, _O, _T, _U). None match dim.db — do not join to dim.db. Use branche values directly as inline categories. '_T' = total, '_U' = uoplyst (unknown), '_O' = other.
- virkstrrda uses different coding than the goods table tec01. Here the smallest band is E0T49 (0–49 employees combined), not split into 0–9 and 10–49. '_T' = total; filter to '_T' unless disaggregating by firm size.
- Only 2023 data.