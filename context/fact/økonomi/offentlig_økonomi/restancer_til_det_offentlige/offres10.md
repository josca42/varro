table: fact.offres10
description: Offentlige restancer efter restancetype, gældstype, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- restance: values [101=Samlede restancer, 102=1. SKATs egne krav, 103=2. Andre offentlige restancer, 104=2.1 Kommunale krav, 105=2.2 Statslige krav, 106=2.3 Krav fra andre offentlige virksomheder mv.]
- deltyp: values [601=Samlet restance i alt, 602=Fordringer, 603=Renter]
- prisenhed: values [401=Nominel værdi, 402=Kursværdi]
- tid: date range 2013-01-01 to 2024-01-01

notes:
- prisenhed is a measurement selector: 401=Nominel værdi, 402=Kursværdi. Every restance/deltyp/tid combination appears twice (once per prisenhed). Always filter to one: WHERE prisenhed=401 for nominal values (most common), prisenhed=402 for market value.
- restance has a two-level hierarchy. Level 0: 101=Samlede restancer (total). Level 1: 102=SKATs egne krav, 103=Andre offentlige restancer. Level 2 (within 103): 104=Kommunale krav, 105=Statslige krav, 106=Krav fra andre offentlige virksomheder mv. Filter to one level to avoid double-counting. For breakdown by main creditor type: WHERE restance IN (102, 103).
- deltyp is also hierarchical: 601=Samlet restance i alt (total), 602=Fordringer, 603=Renter. 601 = 602 + 603. Always filter to one. For total outstanding debt: WHERE deltyp=601.
- A minimal "total outstanding debt, nominal" query: WHERE restance=101 AND deltyp=601 AND prisenhed=401. This gives one row per tid.
- For creditor breakdown: WHERE restance IN (102, 103) AND deltyp=601 AND prisenhed=401. Sums to 101.
- offres10 covers all public debt (SKAT + other public creditors). For SKAT detail, use offres20; for non-SKAT detail, use offres30.