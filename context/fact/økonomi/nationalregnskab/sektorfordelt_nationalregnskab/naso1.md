table: fact.naso1
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (oversigtstabel) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P11A12A131K=P.11+P.12+P.131 Markedsmæssig produktion, produktion til eget brug samt betaling for ikke-markedsmæssig produktion, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester ... P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B2ND=B.2n Nettooverskud af produktion, B3ND=B.3n Blandet nettoindkomst, B1ND=B.1n Nettoværditilvækst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. 9 sectors: S11, S12, S13, S14, S15, S2, plus aggregates S1=Hele økonomien, S1M=S.14+S.15, S1W=private sector. Use ColumnValues("naso1", "sektor") for labels.
- Annual overview table for production, BVT and income formation (chapter 1-2.1.1), 1995-2024. Quarterly equivalent: nkso1 (1999+). For more transaction detail: nasd11 (production) and nasd12 (income formation).
- transakt: filter to the specific flow you need. Key codes: B1GD=Bruttoværditilvækst, P1K=Produktion, D1D=Aflønning af ansatte, B2A3GD=Bruttooverskud.