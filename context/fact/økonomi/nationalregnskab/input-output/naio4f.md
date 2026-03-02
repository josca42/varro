table: fact.naio4f
description: Input-output tabel. Totaler for tilgang fordelt efter anvendelse og prisenhed. (69-gruppering) efter tilgangstype, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [TP1_BP=Dansk produktion, i alt, TP7AD2121=Import i alt inkl. told, TD211A214X31=Produktskatter, netto + moms, TP2=Forbrug i produktionen / endelig anvendelse, køberpriser, B1G=Bruttoværditilvækst (BVT), P1=Produktionsværdi]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Same as naio4 but limited to the 69-groupering (niveau 4) for `anvendelse`. Covers to 2024 vs 2022.
- **prisenhed must be filtered** and **tilgang1 must be filtered**. See naio4 notes for value semantics.