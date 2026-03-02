table: fact.nasd11
description: 1 Produktion og BVT (detaljeret) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P11K=P.11 Markedsmæssig produktion, P12K=P.12 Produktion til eget brug, P13K=P.13 ikke-markedsmæssig produktion, P131K=P.131 Betaling for ikke-markedsmæssig produktion, P132K=P.132 Anden ikke-markedsmæssig produktion, P11A12A131K=P.11+P.12+P.131 Markedsmæssig produktion, produktion til eget brug samt betaling for ikke-markedsmæssig produktion, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester, P2D=P.2 Forbrug i produktionen, P6D=P.6 Eksport af varer og tjenester, P61D=P.61 Eksport af varer, P62D=P.62 Eksport af tjenester, B1GD=B.1g Bruttoværditilvækst, BVT, B11D=B.11 Udlandskontoens vare- og tjenestebalance, P51CD=P.51c Forbrug af fast realkapital, B1ND=B.1n Nettoværditilvækst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Full subsector breakdown including S11, S12, S121, S122A123 (=S.122+S.123 combined), S124-S129, S13, S14, S15, S2, plus aggregates S1, S1M. Use ColumnValues("nasd11", "sektor") for full label list.
- S122A123 is a combined code (Pengeinstitutter + Pengemarkedsforeninger) with no matching dim.esa entry — a LEFT JOIN on dim.esa returns NULL for this code. Use ColumnValues labels directly when you need its name.
- Most detailed production and BVT table (chapter 1, 1995-2024). For overview use naso1. transakt codes cover production type breakdown (P11K=markedsmæssig, P12K=eget brug, P13K=ikke-markedsmæssig) and value-added components (B1GD=BVT, B1ND=net value added).