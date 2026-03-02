table: fact.dnfdiinc
description: Udlandets direkte investeringer i Danmark efter land, instrument, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 4]
- instrnat: values [2.0=2.0: Direkte investeringer (I alt), 2.1=2.1: Egenkapital, 2.2=2.2: Koncernlån mv.]
- data: values [F=Transaktioner, S=Beholdninger (ultimo året), I=Formueindkomst]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- Mirror of dnfdiouc but for inward FDI (udlandets investeringer i Danmark). Identical structure and same caveats apply.
- data is a required selector: F=Transaktioner, S=Beholdninger, I=Formueindkomst. Always filter to one to avoid triple-counting.
- instrnat is also a selector: 2.0=total, 2.1=egenkapital, 2.2=koncernlån. Always filter to one.
- land joins dim.lande_uht_bb at niveaux 1, 2, and 4. Unmatched codes W1 (world total), I9 and R12 (custom BoP aggregates) — exclude when working at individual country level.
- To query individual countries: JOIN dim.lande_uht_bb d ON f.land = d.kode WHERE d.niveau = 4. Continents at niveau=1, EU grouping B6 at niveau=2.