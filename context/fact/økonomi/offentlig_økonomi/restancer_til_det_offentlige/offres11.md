table: fact.offres11
description: Offentlige restancer efter restancetype, gældstype, konto og tid
measure: indhold (unit Mio. kr.)
columns:
- restance: values [101=Samlede restancer, 102=1. SKATs egne krav, 103=2. Andre offentlige restancer, 104=2.1 Kommunale krav, 105=2.2 Statslige krav, 106=2.3 Krav fra andre offentlige virksomheder mv.]
- deltyp: values [601=Samlet restance i alt, 602=Fordringer, 603=Renter]
- konto1: values [501=Primo saldo, 502=Tilgang, 503=Afskrivning, 504=Korrektion, 505=Provenu, 506=Ultimo saldo]
- tid: date range 2019-01-01 to 2024-01-01

notes:
- konto1 represents account movement types within the year, NOT a measurement selector. Values are: 501=Primo saldo (opening balance), 502=Tilgang (new debt added), 503=Afskrivning (write-offs, negative), 504=Korrektion (adjustments, negative), 505=Provenu (collected payments, negative), 506=Ultimo saldo (closing balance). Verified: primo + tilgang + afskrivning + korrektion + provenu = ultimo (stock-flow identity). Summing across konto1 is meaningless. Pick a specific konto1 for analysis.
- restance is hierarchical (same as offres10): 101=total, 102=SKAT, 103=Andre offentlige (=104+105+106). Filter to one level.
- deltyp: 601=total, 602=Fordringer, 603=Renter. 601 = 602 + 603. Filter to one.
- For current outstanding debt: use konto1=506 (Ultimo saldo). For annual inflow of new debt: konto1=502. For write-offs: konto1=503. For collections: konto1=505.
- This table only goes back to 2019. For longer time series on stock levels, use offres10 (from 2013).