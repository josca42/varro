table: fact.dnfdioui
description: Danske direkte investeringer i udlandet efter udenlandsk branche (DB07), instrument, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- udlbranche: join dim.db on udlbranche=kode::text [approx]
- instrnat: values [2.0=2.0: Direkte investeringer (I alt), 2.1=2.1: Egenkapital investeringer, 2.2=2.2: Koncernlån mv.]
- data: values [F=Transaktioner, S=Beholdninger (ultimo året), I=Formueindkomst]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/db.md

notes:
- DO NOT join dim.db. The udlbranche column uses NACE section letter codes (A, B, C…) not the DB07 numeric codes that dim.db uses. The join matches 0 rows.
- Use ColumnValues("dnfdioui", "udlbranche") to see all 17 branch codes with labels. Key codes: ALL=total, letter codes A–M are NACE sections, compound codes (C21, C28, H50, K64.2, M70) are subsectors within their parent, D+E=Forsyningsvirksomhed, EJ1100_2100=Øvrige brancher og ukendt.
- C21 and C28 are subcategories of C; H50 of H; K64.2 of K; M70 of M. Do not sum ALL + subsectors or parent + child — you will double-count. For a breakdown, use only the top-level letters (A, B, C, D+E, G, H, J, K, L, M).
- data is a required selector: F=Transaktioner, S=Beholdninger, I=Formueindkomst. Always filter to one.
- instrnat is also a selector: 2.0=total, 2.1=egenkapital, 2.2=koncernlån. Always filter to one.
- Short series: data starts 2015 (vs 2004 for the country-breakdown tables).