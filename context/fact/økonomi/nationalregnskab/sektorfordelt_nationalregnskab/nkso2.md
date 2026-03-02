table: fact.nkso2
description: 2.1.2-3.1 Indkomst,forbrug, opsparing og investering (oversigtstabel) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D2K=D.2 Modtaget produktions- og importskatter, D3K=D.3 Betalt subsidier, D4K=D.4 Modtaget formueindkomst ... P51C5D=P.51c Forbrug af fast realkapital, P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1999-01-01 to 2025-04-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Sectors: S1, S11, S12, S13, S1M, S1W, S2 (no individual S14/S15 — use naso2 for those). Aggregates have no dim.esa entry — use ColumnValues("nkso2", "sektor") for labels.
- Quarterly table, tid = first day of each quarter (1999Q1–2025Q1). Annual equivalent: naso2 (1995-2024). Covers income distribution, consumption, savings, investment (chapter 2.1.2–3.1).
- transakt: K-suffix = received (ressource side), D-suffix = paid (anvendelse side). Each code is an independent flow.