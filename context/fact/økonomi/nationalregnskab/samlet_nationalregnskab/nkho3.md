table: fact.nkho3
description: 2.1.2-3.1 Indkomst, forbrug, opsparing og investering efter transaktion, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D2K=D.2 Modtaget produktions- og importskatter, D3K=D.3 Betalt subsidier, D4K=D.4 Modtaget formueindkomst ... P52_53D=P.52+P.53 Lagerforøgelse mv., P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- saeson (N=ikke sæsonkorrigeret, Y=sæsonkorrigeret) doubles row counts — always filter to one value. No prisenhed column (values in løbende priser only).
- Quarterly income/consumption/savings/investment from 1990. Annual equivalent: naho3 (from 1966).
- transakt covers multiple national accounts stages (allocation, secondary distribution, use of income, capital account) — the codes are not additive across the full set.
