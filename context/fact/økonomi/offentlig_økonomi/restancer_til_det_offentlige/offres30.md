table: fact.offres30
description: Andre offentlige restancer efter restancetype, gældstype, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- restance: values [301=Andre offentlige restancer, 302=1. Kommunale krav, 303=1.1 Boligstøtte, 304=1.2 Dagsinstitution mv., 305=1.3 Ejendomsskat ... 331=3.6 Øvrige offentlige krav, 332=3.7 Opkrævningsrente, 333=3.8 Inddrivelsesrente, 334=3.9 Civilretslige krav, 335=3.10 Gebyr, retsafgift mv.]
- deltyp: values [601=Samlet restance i alt, 602=Fordringer, 603=Renter]
- prisenhed: values [401=Nominel værdi, 402=Kursværdi]
- tid: date range 2013-01-01 to 2024-01-01

notes:
- prisenhed is a measurement selector: 401=Nominel, 402=Kursværdi. Always filter to one. WHERE prisenhed=401 for nominal values.
- restance has a three-level hierarchy. Level 0: 301=Andre offentlige restancer (total). Level 1: 302=1. Kommunale krav, 313=2. Statslige krav, 325=3. Krav fra andre offentlige virksomheder mv. Level 2: 303-312 (within 302), 314-324 + 336 (within 313), 326-335 (within 325). Use ColumnValues("offres30", "restance") to see all 35 codes with labels.
- deltyp: 601=total, 602=Fordringer, 603=Renter. Filter to one.
- For creditor-type breakdown: WHERE restance IN (302, 313, 325) AND deltyp=601 AND prisenhed=401. These are non-SKAT public creditors (municipalities, state agencies, public enterprises like DR/A-kasser/regioner).
- Note: code 310 (1.8 Inddrivelsesrente, kommunal) has only 1 row — effectively absent. Code 336 (2.12 Kontrolafgifter personbefordring) is a newer addition to category 313.
- This table is the detailed drilldown of "Andre offentlige restancer" (offres10 code 103).