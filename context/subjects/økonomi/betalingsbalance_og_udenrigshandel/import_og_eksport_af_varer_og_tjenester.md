<fact tables>
<table>
id: uhm
description: Udenrigshandel månedlig efter poster, im- og eksport, land, enhed, sæsonkorrigering og tid
columns: post, indud, land, enhed, saeson, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2025-08-01
</table>
<table>
id: uhq
description: Udenrigshandel kvartalsvis efter poster, im- og eksport, land, sæsonkorrigering og tid
columns: post, indud, land, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 2010-01-01 to 2025-04-01
</table>
<table>
id: vuhq
description: Versionstabel af UHQ - Udenrigshandel kvartalsvis efter version, poster, im- og eksport, land, sæsonkorrigering og tid
columns: version, post, indud, land, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 2010-01-01 to 2025-07-01
</table>
<table>
id: uhfastp1
description: Udenrigshandel i faste priser månedlig (eksperimentel statistik) efter poster, im- og eksport, prisenhed, sæsonkorrigering og tid
columns: post, indud, prisenhed, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 2010-01-01 to 2025-09-01
</table>
</fact tables>

notes:
- For current trade data: use uhq (quarterly, Mio. kr.) for the richest country and service breakdown, or uhm (monthly) if you need monthly granularity. uhm has fewer countries (8 niveau-4 + 2 niveau-2) and fewer service subcategories than uhq.
- uhm vs uhq key difference: uhm has an enhed column (4 measurement types: level in Mio. kr., pct/month, pct/3 months, pct/year) — always filter `enhed = 93` for level data. uhq has no enhed column (fixed unit: Mio. kr.) making it simpler to query.
- For fixed-price volume comparison: use uhfastp1 (monthly, experimental). It only covers goods (no services, no land breakdown) but provides both current and 2021-price series via prisenhed.
- For revision analysis: use vuhq — same structure as uhq but with a version dimension tracking 50 monthly publication vintages. Not suitable for regular trade analysis.
- Common pitfall across all tables: post is hierarchical (dot notation). 1.A (total) > 1.A.A (varer) + 1.A.B (tjenester) > subcategories. Parent rows are pre-computed totals — summing all posts massively double-counts. Always filter to one post level.
- Common pitfall: saeson (1=ikke sæsonkorrigeret, 2=sæsonkorrigeret) must always be filtered. Not all combinations have both values, so failing to filter inflates sums unpredictably.
- W1 (Verden) is the world total and appears in all tables except uhfastp1, but is NOT in dim.lande_uht_bb — use `land = 'W1'` directly. I9/J8/J9/P4/P7 are service-only aggregate regions also absent from the dim, appearing only for 1.A.B.* posts.