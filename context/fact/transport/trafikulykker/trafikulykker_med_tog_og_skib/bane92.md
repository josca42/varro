table: fact.bane92
description: Dræbte og tilskadekomne ved jernbanetrafik efter banenet, uheldstype, personskade og tid
measure: indhold (unit Antal)
columns:
- bane: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- utype: values [0=I alt, 3035=Kollission (ekskl. uheld i overskæring), 3040=Afsporing, 3045=Uheld i overskæring forårsaget af rullende materiel, 3050=Anden personulykke forårsaget af rullende materiel, 3055=Brand i rullende materiel, 3060=Andet]
- uheld: values [1=Dræbte, 2=Alvorligt tilskadekomne]
- tid: date range 2002-01-01 to 2024-01-01

notes:
- bane codes are identical to bane91: 10010=total, 10020=Banedanmarks net, 10130=Metro, 10140=Letbane. bane=10010 is the aggregate of the others. bane=10120 (ANDRE BANER) documented but not present in data.
- utype=0 (I alt) is the aggregate across all accident types. Other values (3035=Kollision, 3040=Afsporing, 3045=Uheld i overskæring, 3050=Anden personulykke, 3055=Brand, 3060=Andet) are mutually exclusive; they sum to utype=0.
- uheld has only 2 values with no aggregate: 1=Dræbte, 2=Alvorligt tilskadekomne. Same as bane91 — independent outcomes, summing gives total casualties.
- Shorter time series than bane91 (from 2002 vs 1993). Use bane91 for longer historical series or person-category breakdown; use bane92 when accident type (kollision, afsporing, etc.) is needed.