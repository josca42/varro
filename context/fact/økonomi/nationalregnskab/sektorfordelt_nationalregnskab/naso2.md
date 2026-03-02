table: fact.naso2
description: 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (oversigtstabel) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D2K=D.2 Modtaget produktions- og importskatter, D3K=D.3 Betalt subsidier, D4K=D.4 Modtaget formueindkomst ... P51C5D=P.51c Forbrug af fast realkapital, P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. 9 sectors: S11, S12, S13, S14, S15, S2, plus aggregates S1, S1M, S1W. Use ColumnValues("naso2", "sektor") for labels.
- Annual overview table for income, consumption, savings and investment (chapter 2.1.2–3.1), 1995-2024. Quarterly equivalent: nkso2 (1999+). More detailed transactions available in nasd22, nasd23, nasd24.
- transakt: K-suffix = received, D-suffix = paid. Key codes: B6GD=Disponibel bruttoindkomst, B8GD=Bruttoopsparing, P51GD=Faste bruttoinvesteringer, B9D=Fordringserhvervelse netto.