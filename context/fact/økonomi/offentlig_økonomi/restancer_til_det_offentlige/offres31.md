table: fact.offres31
description: Andre offentlige restancer efter restancetype, gældstype, konto og tid
measure: indhold (unit Mio. kr.)
columns:
- restance: values [301=Andre offentlige restancer, 302=1. Kommunale krav, 303=1.1 Boligstøtte, 304=1.2 Dagsinstitution mv., 305=1.3 Ejendomsskat ... 331=3.6 Øvrige offentlige krav, 332=3.7 Opkrævningsrente, 333=3.8 Inddrivelsesrente, 334=3.9 Civilretslige krav, 335=3.10 Gebyr, retsafgift mv.]
- deltyp: values [601=Samlet restance i alt, 602=Fordringer, 603=Renter]
- konto1: values [501=Primo saldo, 502=Tilgang, 503=Afskrivning, 504=Korrektion, 505=Provenu, 506=Ultimo saldo]
- tid: date range 2019-01-01 to 2024-01-01

notes:
- konto1 represents account movements (same as offres11): 501=Primo saldo, 502=Tilgang, 503=Afskrivning (negative), 504=Korrektion (negative), 505=Provenu (negative), 506=Ultimo saldo. Never sum across konto1. Use konto1=506 for outstanding balance, konto1=502 for new non-SKAT public debt added annually.
- restance has a three-level hierarchy (same as offres30): 301=total, level 1 categories are 302, 313, 325, with level 2 subcategories beneath. Use ColumnValues("offres31", "restance") to see all 35 codes.
- deltyp: 601=total, 602=Fordringer, 603=Renter. Filter to one.
- This is the account-movements view of non-SKAT public arrears. Only from 2019. For stock levels from 2013, use offres30.