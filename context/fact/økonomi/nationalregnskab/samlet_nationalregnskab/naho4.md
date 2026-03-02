table: fact.naho4
description: 5 Danmark og udlandet (oversigt) efter transaktion og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P6D=P.6 Eksport af varer og tjenester, P61D=P.61 Eksport af varer, P62D=P.62 Eksport af tjenester, D1K=D.1 Modt. Aflønning af ansatte, D3K=D.3 Modt. Subsidier ... B11D=B.11 Udlandskontoens vare- og tjenestebalance, B12D=B.12 Saldo på udlandskontoens løbende poster, B9D=B.9 Fordringserhvervelse, netto, D41FD=Memopost: Bet. Renter før FISIM korrektion, D41FK=Memopost: Modt. Renter før FISIM korrektion]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- No prisenhed column (løbende priser only). Single measure per transakt×tid.
- 'Oversigt' version of Denmark's external account from 1995. Annual equivalent with longer history: nahl4 (from 1966). Detailed version: nahd4. Quarterly: nkhl4.
- Balance codes (B11D, B12D, B9D) are net saldos. D41FD/D41FK are memo items (renter før FISIM korrektion) — not part of the main accounting identity.
