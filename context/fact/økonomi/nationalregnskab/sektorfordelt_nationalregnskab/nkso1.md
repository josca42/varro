table: fact.nkso1
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (oversigtstabel) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P11A12A131K=P.11+P.12+P.131 Markedsmæssig produktion, produktion til eget brug samt betaling for ikke-markedsmæssig produktion, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester ... P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B2ND=B.2n Nettooverskud af produktion, B3ND=B.3n Blandet nettoindkomst, B1ND=B.1n Nettoværditilvækst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1999-01-01 to 2025-04-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. 7 sectors: S11=Ikke-finansielle selskaber, S12=Finansielle selskaber, S13=Offentlig forvaltning og service, S2=Udlandet, plus aggregates S1=Hele økonomien, S1M=S.14+S.15 husholdninger+NPIsH, S1W=S.11+S.12+S.14+S.15 private sector. Aggregates have no dim.esa entry — use ColumnValues("nkso1", "sektor") for labels.
- Quarterly table, tid = first day of each quarter (1999Q1–2025Q1). Annual equivalent: naso1 (1995-2024).
- transakt: each code is a distinct national accounts flow — filter to the one you need. K-suffix = received, D-suffix = paid.