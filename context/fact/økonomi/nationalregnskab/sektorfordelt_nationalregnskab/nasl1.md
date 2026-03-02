table: fact.nasl1
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (hovedposter) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester, P2D=P.2 Forbrug i produktionen, P6D=P.6 Eksport af varer og tjenester, P61D=P.61 Eksport af varer, P62D=P.62 Eksport af tjenester, B1GD=B.1g Bruttoværditilvækst, BVT, B11D=B.11 Udlandskontoens vare- og tjenestebalance, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, D29D=D.29 Andre produktionsskatter, D39D=D.39 Andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B1ND=B.1n Nettoværditilvækst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1971-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Only 4 aggregate sectors: S1=Hele økonomien, S13=Offentlig forvaltning og service, S1W=S.11+S.12+S.14+S.15 (private sector), S2=Udlandet. S1 and S1W are pre-computed aggregates not present in dim.esa — use ColumnValues("nasl1", "sektor") to see their labels.
- transakt rows represent distinct national accounts flows (production, value-added, compensation, etc.) — they are independent entries. Filter WHERE transakt = 'B1GD' to get BVT (gross value added), WHERE transakt = 'D1D' for compensation of employees, etc.
- This is the long historical series (1971-2024) but covers only 4 pre-aggregated sectors and a subset of transaction types (Produktion og indkomstdannelse, chapter 1-2.1.1). For finer sector breakdown use naso1 (1995+). For the full ESA sector hierarchy use nasd11.