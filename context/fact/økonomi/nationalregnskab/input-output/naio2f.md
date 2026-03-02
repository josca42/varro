table: fact.naio2f
description: Input-output tabel. Ikke branchefordelt import efter anvendelse og prisenhed. (69-gruppering) efter tilgangstype, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [UNSPI=Ikke varefordelt import, i alt, 1UNSPI=Transaktioner vedr. olieaktivitet i Nordsø, 2UNSPI=Turistindtægter og -udgifter osv., 3UNSPI=Danske skibes udgifter i fremmede havne, 4UNSPI=Uspecificeret import i.a.n., 5UNSPI=Uspecificeret offentlig import]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Same as naio2 but limited to the 69-groupering (niveau 4) for `anvendelse`. Covers to 2024 vs 2022 for naio2.
- **prisenhed must be filtered** and **tilgang1 must be filtered**. See naio2 notes for value semantics.