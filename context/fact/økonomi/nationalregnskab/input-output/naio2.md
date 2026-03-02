table: fact.naio2
description: Input-output tabel. Ikke branchefordelt import efter anvendelse og prisenhed efter tilgangstype, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [UNSPI=Ikke varefordelt import, i alt, 1UNSPI=Transaktioner vedr. olieaktivitet i Nordsø, 2UNSPI=Turistindtægter og -udgifter osv., 3UNSPI=Danske skibes udgifter i fremmede havne, 4UNSPI=Uspecificeret import i.a.n., 5UNSPI=Uspecificeret offentlig import]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Covers non-industry-allocated imports (tourist spending, oil activities, unspecified import categories). Complement to naio1 which covers industry-allocated supply.
- **prisenhed must be filtered** (V=løbende, Y=foregående års priser).
- **tilgang1 must be filtered**: UNSPI=i alt, 1UNSPI=olieaktivitet (Nordsø), 2UNSPI=turistindtægter/-udgifter, 3UNSPI=danske skibes udgifter i fremmede havne, 4UNSPI=uspecificeret i.a.n., 5UNSPI=uspecificeret offentlig import. Filter to UNSPI for the total or to a specific sub-type. Summing all 6 overcounts (UNSPI is the sum of 1-5).
- `anvendelse` uses A-prefixed nr_branche codes. Join via `SUBSTRING(f.anvendelse, 2) = d.kode`. Represents which industry/final demand category this import feeds into.