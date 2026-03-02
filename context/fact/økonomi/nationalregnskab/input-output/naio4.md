table: fact.naio4
description: Input-output tabel. Totaler for tilgang fordelt efter anvendelse og prisenhed efter tilgangstype, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [TP1_BP=Dansk produktion, i alt, TP7AD2121=Import i alt inkl. told, TD211A214X31=Produktskatter, netto + moms, TP2=Forbrug i produktionen / endelig anvendelse, køberpriser, B1G=Bruttoværditilvækst (BVT), P1=Produktionsværdi]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Supply totals — the column sums of the full IO table (naio1 + naio2 + naio3). Use to check accounting identities or get total supply/demand by industry without joining multiple tables.
- **prisenhed must be filtered** (V or Y).
- **tilgang1 must be filtered**: TP1_BP=Dansk produktion i alt, TP7AD2121=Import i alt inkl. told, TD211A214X31=Produktskatter+moms, TP2=Forbrug i produktionen/endelig anvendelse (køberpriser), B1G=Bruttoværditilvækst, P1=Produktionsværdi. Each is an independent total — summing them is double-counting.
- `anvendelse` = A-prefixed industry/demand codes. Join via `SUBSTRING(f.anvendelse, 2) = d.kode`. Use `AA00000` to get grand totals across all demand categories.