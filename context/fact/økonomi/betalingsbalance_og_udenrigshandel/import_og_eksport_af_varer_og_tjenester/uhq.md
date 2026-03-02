table: fact.uhq
description: Udenrigshandel kvartalsvis efter poster, im- og eksport, land, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- post: values [1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.0-4X2-3=Næringsmidler, drikkevarer, tobak mv., 1.A.A.1.2=Råstoffer, ikke spiselige, undt. brændsel ... 1.A.B.8=Royalties og licenser, 1.A.B.9=Telekommunikation, computer- og informationstjenester, 1.A.B.10=Andre forretningstjenester, 1.A.B.11=Audiovisuelle tjenester samt tjenester ifm. uddannelse, sundhed, kultur og rekreation, 1.A.B.12=Offentlige tjenester]
- indud: values [1=Import, 2=Eksport]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 4]
- saeson: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- tid: date range 2010-01-01 to 2025-04-01
dim docs: /dim/lande_uht_bb.md

notes:
- saeson must be filtered. Not every land/post combination has a sæsonkorrigeret version (saeson=2). Use `saeson = 1` for unadjusted data; forgetting this inflates sums where both values exist.
- post is hierarchical (dot notation). 1.A covers 1.A.A (varer) and 1.A.B (tjenester); those cover sub-categories. Parent rows are pre-aggregated totals — summing all posts double-counts. Filter to a single post level. uhq has much finer service detail than uhm (12 tjeneste subcategories vs 3).
- land has 27 distinct codes: B6 (EU-27) and D6 (Extra EU-27) at niveau 2; 21 individual countries at niveau 4; plus W1, I9, J9, P7 which are NOT in dim.lande_uht_bb. W1=Verden (world total, covers all posts). I9, J9, P7 are service-only aggregate regions — they only appear for 1.A.B.* posts and are not covered by the dim table (likely OECD/EFTA/other groupings used for service trade).
- For country-level analysis: join dim.lande_uht_bb with `d.niveau = 4`. For EU vs non-EU split: use land IN ('B6','D6') directly. For world total: `land = 'W1'`.
- ColumnValues("lande_uht_bb", "titel", for_table="uhq") shows the 23 matchable codes. W1/I9/J9/P7 won't appear — use them directly if needed.
- Typical query: filter `saeson = 1`, pick a single `post`, join dim with `d.niveau = 4` for country labels.