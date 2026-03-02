table: fact.nkhl4
description: 5 Danmark og udlandet efter transaktion, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P6D=P.6 Eksport af varer og tjenester, P61D=P.61 Eksport af varer, P62D=P.62 Eksport af tjenester, D1K=D.1 Modt. Aflønning af ansatte, D3K=D.3 Modt. Subsidier ... B111D=Varebalance, B112D=Tjenestebalance, B11D=B.11 Udlandskontoens vare- og tjenestebalance, B12D=B.12 Saldo på udlandskontoens løbende poster, B9D=B.9 Fordringserhvervelse, netto]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- saeson (N/Y) doubles row counts — always filter. No prisenhed (løbende priser only).
- Quarterly Denmark external account from 1990. Annual equivalent: nahl4 (from 1966). More detail: naho4/nahd4 (annual from 1995).
- Balance codes (B11D, B12D, B9D) are net saldos — do not sum with component flows.
