table: fact.dnfdiini
description: Udlandets direkte investeringer i Danmark efter indenlandsk branche (DB07), instrument, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- indlbranche: join dim.db on indlbranche=kode::text [approx]
- instrnat: values [2.0=2.0: Direkte investeringer (I alt), 2.1=2.1: Egenkapital, 2.2=2.2: Koncernlån mv.]
- data: values [F=Transaktioner, S=Beholdninger (ultimo året), I=Formueindkomst]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/db.md

notes:
- DO NOT join dim.db. Same as dnfdioui: indlbranche uses NACE letter codes, not DB07 numeric codes. Join matches 0 rows.
- Use ColumnValues("dnfdiini", "indlbranche") to get the full code-label mapping. Identical 17-code structure as dnfdioui: ALL, A, B, C, C21, C28, D+E, G, H, H50, J, K, K64.2, L, M, M70, EJ1100_2100.
- Inward FDI by domestic branch (udlandets investeringer i Danmark fordelt på dansk branche). Goes back to 2004, vs dnfdioui which only goes back to 2015.
- data selector: F=Transaktioner, S=Beholdninger, I=Formueindkomst. instrnat: 2.0=total, 2.1=egenkapital, 2.2=koncernlån. Always filter both to one value.
- Subcategory doubling: C21, C28 ⊂ C; H50 ⊂ H; K64.2 ⊂ K; M70 ⊂ M — never sum parent with child codes.