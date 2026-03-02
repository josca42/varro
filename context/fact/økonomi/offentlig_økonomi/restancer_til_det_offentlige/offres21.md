table: fact.offres21
description: Skatterestancer efter restancetype, gældstype, konto og tid
measure: indhold (unit Mio. kr.)
columns:
- restance: values [201=SKATs egne krav, 202=1. Personskatter, 203=1.1 Restskat, 204=1.2 B-skat, 205=1.3 AM-bidrag - restbidrag mv. ... 218=4.1 Opkrævningsrente, 219=4.2 Inddrivelsesrente, 220=5. Civilretslige krav, 221=5.1 Civilretslige krav, 222=5.2 Gebyr, retsafgift mv.]
- deltyp: values [601=Samlet restance i alt, 602=Fordringer, 603=Renter]
- konto1: values [501=Primo saldo, 502=Tilgang, 503=Afskrivning, 504=Korrektion, 505=Provenu, 506=Ultimo saldo]
- tid: date range 2019-01-01 to 2024-01-01

notes:
- konto1 represents account movements (same as offres11): 501=Primo saldo, 502=Tilgang, 503=Afskrivning (negative), 504=Korrektion (negative), 505=Provenu (negative), 506=Ultimo saldo. Primo + flows = Ultimo. Never sum across konto1. Use konto1=506 for outstanding balance, konto1=502 for new debt, konto1=503 for write-offs.
- restance has a three-level hierarchy (same as offres20): 201=total, level 1 categories are 202, 207, 216, 217, 220, with level 2 subcategories beneath each. Use ColumnValues("offres21", "restance") to see all 22 codes.
- deltyp: 601=total, 602=Fordringer, 603=Renter. Filter to one.
- This is the account-movements drilldown for SKAT's own claims. Combines the detail of offres20 with the flow analysis of offres11. Only from 2019.