<fact tables>
<table>
id: fiks11
description: Firmaernes køb og salg efter branche (DB07), beløb, sæsonkorrigering og tid
columns: branche07, belob, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 2009-01-01 to 2025-08-01
</table>
<table>
id: fiks22
description: Firmaernes køb og salg (19-grupperingen) efter branche (DB07), beløb, sæsonkorrigering og tid
columns: branche07, belob, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 2009-01-01 to 2025-08-01
</table>
<table>
id: fiks33
description: Firmaernes køb og salg (36 og 127-grupperingen) efter branche (DB07), beløb og tid
columns: branche07, belob, tid (time), indhold (unit Mio. kr.)
tid range: 2009-01-01 to 2025-08-01
</table>
<table>
id: fiks44
description: Firmaernes køb og salg (detaljeret) efter branche (DB07), beløb og tid
columns: branche07, belob, tid (time), indhold (unit Mio. kr.)
tid range: 2009-01-01 to 2025-04-01
</table>
<table>
id: fiks55
description: Firmaernes køb og salg efter branche (DB07), beløb og tid
columns: branche07, belob, tid (time), indhold (unit Mio. kr.)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: fiks9
description: Firmaernes køb og salg, historisk sammendrag efter beløb og tid
columns: belob, tid (time), indhold (unit Mio. kr.)
tid range: 1969-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables measure firms' purchases and sales in Mio. kr. (indhold). belob is a measurement selector present in every table — always filter to one value: 0=Indenlandsk køb, 1=Indenlandsk salg, 3=Køb i alt, 4=Salg i alt. Summing across belob values is always wrong.
- Time granularity by table: fiks11/fiks22/fiks33 = monthly, fiks44 = quarterly, fiks55/fiks9 = annual.
- For trend analysis over time with industry breakdown: use fiks11 (monthly, from 2009) or fiks55 (annual, from 2009). Both have numeric division codes + letter section aggregates for branche07. fiks11 also has saeson (seasonal adjustment selector — must filter to EJSÆSON or SÆSON).
- For the broadest industry grouping (19 NACE sections A–S): use fiks22 (monthly). branche07 codes are letter codes with no dim.db join — use ColumnValues("fiks22", "branche07") for labels.
- For the most detailed industry breakdown (DB07 niveau 5, ~524 sub-groups): use fiks44 (quarterly). branche07 codes are 6-digit and join to dim.db niveau 5 via LTRIM(f.branche07,'0')=d.kode::text AND d.niveau=5.
- For 127-gruppe breakdown (DST-specific grouping between section and niveau-5 detail): use fiks33 (monthly). branche07 has a custom coding scheme that does not join to dim.db — use ColumnValues("fiks33", "branche07").
- For historical data pre-2009 or firm counts: use fiks9 (annual 1969–2024, no branche). Only table with belob=5 (Antal virksomheder).
- fiks11 vs fiks55: same branche structure, fiks11 is monthly with seasonal adjustment choice, fiks55 is annual only. Prefer fiks11 for monthly resolution or when seasonal adjustment matters.