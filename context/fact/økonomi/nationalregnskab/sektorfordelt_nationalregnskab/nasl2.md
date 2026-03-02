table: fact.nasl2
description: 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (hovedposter) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D2K=D.2 Modtaget produktions- og importskatter, D3K=D.3 Betalt subsidier, D4N=D.4 Formueindkomst, netto ... P51GD=P.51g Faste bruttoinvesteringer, P51C5D=P.51c Forbrug af fast realkapital, P52_53D=P.52+P.53 Lagerforøgelse mv., NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1971-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Only 4 aggregate sectors: S1=Hele økonomien, S13=Offentlig forvaltning og service, S1W=S.11+S.12+S.14+S.15 (private sector), S2=Udlandet. Use ColumnValues("nasl2", "sektor") for labels.
- transakt covers income distribution, consumption, savings and investment (chapter 2.1.2–3.1). Each code is an independent flow — filter to the one needed (e.g. B6GD=Disponibel bruttoindkomst, B8GD=Bruttoopsparing, P51GD=Faste bruttoinvesteringer). K-suffix = received (ressource), D-suffix = paid (anvendelse).
- Long historical series (1971-2024) with only 4 aggregate sectors. For individual sectors S.11/S.12/S.14/S.15 use naso2 (1995+).