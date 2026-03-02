table: fact.naio3f
description: Input-output tabel. Primære input fordelt efter anvendelse og prisenhed. (69-gruppering) efter tilgangstype, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [D214X31=Produktskatter, netto ekskl. told og moms, D211=Moms, D29X39=Andre produktionsskatter, netto, D1=Aflønning af ansatte, B2A3G=Bruttooverskud af produktion og blandet indkomst, PRIMINP=Primære input, i alt]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Same as naio3 but limited to the 69-groupering (niveau 4) for `anvendelse`. Covers to 2024 vs 2022.
- **prisenhed must be filtered** and **tilgang1 must be filtered**. See naio3 notes for value semantics.