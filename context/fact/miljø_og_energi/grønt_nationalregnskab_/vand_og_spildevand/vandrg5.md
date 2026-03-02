table: fact.vandrg5
description: Udledning af spildevand (Monetært vandregnskab) efter branche, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- erhverv: join dim.nr_branche on REPLACE(erhverv, 'V', '')=kode::text [approx: Industry codes prefixed with V (e.g., V01000 -> 01000). Aggregate codes like ETOT, EHUSHOLD, EV, VA not in dimension.]
- enhed: values [BAS=Basispriser, SPLAFG=Spildevandsafgift, MOMS=Moms, MARK=Markedspriser]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- erhverv joins dim.nr_branche using: REPLACE(REPLACE(f.erhverv, 'V', ''), '_', '-') = TRIM(d.kode). EHUSHOLD and ETOT are aggregate codes not in the dim.
- enhed is a price-decomposition selector — MARK = BAS + SPLAFG + MOMS. Never sum across enhed; always filter to one (typically MARK for total cost).
- 5 hierarchy levels in dim (1–5); filter by d.niveau to avoid cross-level double-counting.
- Monetary counterpart to vandrg4 (physical volumes). Use vandrg4 for m3, vandrg5 for expenditure in Mio. kr.
