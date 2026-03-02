table: fact.naho3
description: 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (oversigt) efter transaktion og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D2K=D.2 Modtaget produktions- og importskatter, D3K=D.3 Betalt subsidier, D4K=D.4 Modtaget formueindkomst ... P52_53D=P.52+P.53 Lagerforøgelse mv., P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- No prisenhed column (løbende priser only). Single measure per transakt×tid — straightforward to query.
- Annual income/consumption/savings/investment aggregates from 1966. 'Oversigt' version — covers multiple national accounts stages in one table. Quarterly version with saeson: nkho3. Detailed breakdown by stage: nahd31, nahd32, nahd33, nahd34.
- transakt codes span from primary income allocation through capital account — not additive across all codes; pick the specific aggregate you need (e.g., B6GQD=disponibel bruttonationalindkomst, B8GD=bruttoopsparing, B9D=fordringserhvervelse netto).
