table: fact.offres20
description: Skatterestancer efter restancetype, gældstype, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- restance: values [201=SKATs egne krav, 202=1. Personskatter, 203=1.1 Restskat, 204=1.2 B-skat, 205=1.3 AM-bidrag - restbidrag mv. ... 218=4.1 Opkrævningsrente, 219=4.2 Inddrivelsesrente, 220=5. Civilretslige krav, 221=5.1 Civilretslige krav, 222=5.2 Gebyr, retsafgift mv.]
- deltyp: values [601=Samlet restance i alt, 602=Fordringer, 603=Renter]
- prisenhed: values [401=Nominel værdi, 402=Kursværdi]
- tid: date range 2013-01-01 to 2024-01-01

notes:
- prisenhed is a measurement selector (same as offres10): 401=Nominel, 402=Kursværdi. Always filter to one. WHERE prisenhed=401 for nominal values.
- restance has a three-level hierarchy. Level 0: 201=SKATs egne krav (total). Level 1 (main categories): 202=1. Personskatter, 207=2. Virksomhedskatter, 216=3. Vægtafgift, 217=4. Renter, 220=5. Civilretslige krav. 201 = sum of level-1 codes exactly. Level 2 (subcategories): 203-206 (within 202), 208-215 (within 207), 218-219 (within 217), 221-222 (within 220). 216 is a leaf with no subcategories. Use ColumnValues("offres20", "restance") to see all 22 codes with labels.
- deltyp: 601=total, 602=Fordringer, 603=Renter. Filter to one.
- For breakdown by main tax type: WHERE restance IN (202, 207, 216, 217, 220) AND deltyp=601 AND prisenhed=401.
- Note: code 219 (4.2 Inddrivelsesrente) only has 5 years of data (partial series).
- This table is a detailed drilldown of SKAT's own claims (offres10 code 102). For the aggregate, use offres10.