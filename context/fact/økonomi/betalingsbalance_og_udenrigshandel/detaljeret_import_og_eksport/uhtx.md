table: fact.uhtx
description: Tjenestebalance, kvartal efter im- og eksport, poster, land og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [1=Import, 2=Eksport, 4=Nettoeksport]
- post: join dim.ebops on post=kode::text; levels [1]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 3, 4]
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/ebops.md, /dim/lande_uht_bb.md

notes:
- post joins dim.ebops with a non-obvious coding: the fact uses dotted notation (e.g. "10.1", "10.1.1", "10.1.1.2") while dim.ebops uses concatenated integers ("101", "1011", "10112"). Correct join: JOIN dim.ebops d ON REPLACE(f.post, '.', '') = d.kode::text. This gives 100% match.
- All 4 dim.ebops hierarchy levels appear in the fact table (niveau 1–4). If you join without filtering niveau you will double/triple count parent categories. Filter: WHERE d.niveau = 1 for service type totals (13 categories), niveau = 4 for finest detail.
- land similarly spans all 4 lande_uht_bb levels (verdensdel to individual country). Filter by d.niveau to pick granularity. Use ColumnValues("lande_uht_bb", "titel", for_table="uhtx") to see available countries.
- indud=4 (Nettoeksport) is pre-computed (eksport minus import). Never sum all three indud values together.
- Quarterly data 2005–2025. Services trade (tjenester) only — use SITC/KN tables for goods trade.