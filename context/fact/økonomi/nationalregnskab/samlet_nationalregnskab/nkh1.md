table: fact.nkh1
description: 0 Varer og tjenester efter transaktion, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1D=P.1 Produktion, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, P7D=P.7 Import af varer og tjenester, P71D=P.71 Import af varer, P72D=P.72 Import af tjenester ... P53K=P.53 Anskaffelser minus afhændelser af værdigenstande, P6K=P.6 Eksport af varer og tjenester, P61K=P.61 Eksport af varer, P62K=P.62 Eksport af tjenester, TUPRK=Anvendelse i alt]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- TWO measurement selectors that both inflate row counts: prisenhed (V=løbende priser, LKV=2020-priser kædede værdier — note LKV not LAN as in annual tables) and saeson (N=ikke sæsonkorrigeret, Y=sæsonkorrigeret). Always filter both.
- For trend analysis use saeson='Y'; for national accounts level consistency use saeson='N'.
- tid is quarterly (2024-01-01 = Q1 2024, 2024-04-01 = Q2 2024, etc.). Annual equivalent: nah1 (from 1966).
- transakt codes cover supply/use — same structure as nah1. TUPRK='Anvendelse i alt'.
