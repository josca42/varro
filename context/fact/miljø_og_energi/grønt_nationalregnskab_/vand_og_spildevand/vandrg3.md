table: fact.vandrg3
description: Forbrug af vand (Monetært vandregnskab) efter branche, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- erhverv: join dim.nr_branche on REPLACE(erhverv, 'V', '')=kode::text [approx: Industry codes prefixed with V (e.g., V01000 -> 01000). Aggregate codes like ETOT, EHUSHOLD, EV, VA not in dimension.]
- enhed: values [BAS=Basispriser, AFG=Vandafgifter, MOMS=Moms, MARK=Markedspriser]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- erhverv joins dim.nr_branche using: REPLACE(REPLACE(f.erhverv, 'V', ''), '_', '-') = TRIM(d.kode). EHUSHOLD and ETOT are aggregate codes not in the dim.
- enhed is a price-decomposition selector — MARK = BAS + AFG + MOMS. Never sum across enhed values; always filter to one (typically MARK for total cost, BAS for basic price).
- 5 hierarchy levels in dim (1–5); filter by d.niveau to avoid cross-level double-counting.
- Monetary counterpart to vandrg2 (physical). Use vandrg2 for volumes (1000 m3), vandrg3 for expenditure (Mio. kr.).
