table: fact.dnfdiuie
description: Ultimativt investorland for udlandets direkte investeringer i Danmark efter land, instrument, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 4]
- instrnat: values [2.0=2.0: Direkte investeringer (I alt), 2.1=2.1: Egenkapital, 2.2=2.2: Koncernlån mv.]
- data: values [S=Beholdninger (ultimo året), I=Formueindkomst]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- Tracks the "ultimativt investorland" — the ultimate beneficial owner country, not the immediate investor country. Differs from dnfdiinc which uses the immediate counterpart country.
- data has only S=Beholdninger and I=Formueindkomst (no F=Transaktioner). Always filter to one.
- instrnat selector: 2.0=total, 2.1=egenkapital, 2.2=koncernlån. Always filter to one.
- land joins dim.lande_uht_bb at niveaux 1, 2, and 4. Unmatched codes: W1 (world total), I9, R12 (custom BoP aggregates), and DK (Denmark — ultimate investor is a Danish entity, i.e. round-tripping investment). DK has no entry in the dim table.
- Use ColumnValues("lande_uht_bb", "titel", for_table="dnfdiuie") to see the ~43 matched country/region codes. Short series: 2016–2024 only.