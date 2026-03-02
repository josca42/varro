table: fact.dnfphen
description: Forsikrings- og pensionssektorens hensættelser efter virksomhedstype, værdier, balancepost og tid
measure: indhold (unit Mia. kr.)
columns:
- virktypnb: values [ALL=1. Forsikrings- og pensionssektoren i alt, PEN=1.1. Pensionsselskaber, LIV=1.1.1. Livsforsikringsselskaber, PKS=1.1.2. Pensionskasser, SKADE=1.2. Skadesforsikringsselskaber]
- vaerdi1: values [ULTIM=1. Hensættelser ultimo, PRAEM=2. Pensionsindbetalinger, YDELS=3. Pensionsudbetalinger, OEVR=4. Øvrige ændringer]
- balpostnat1: values [FPT=1. Hensættelser, i alt, GSP=1.1. Hensættelser til gennemsnitsrenteprodukter, KB=1.1.1. Kollektivt bonuspotentiale, MRP=1.2. Hensættelser til markedsrenteprodukter, PRA=1.3. Præmiehensættelser - skadesforsikring, ERS=1.4. Erstatningshensættelser - skadesforsikring, OEV=1.5. Øvrige hensættelser]
- tid: date range 2015-01-01 to 2025-04-01

notes:
- vaerdi1 represents fundamentally different types of data — NEVER sum across them. ULTIM = stock of provisions at period end; PRAEM = premium payments in (flow); YDELS = pension payouts out (flow); OEVR = other changes (flow). Treat each as a separate dataset.
- virktypnb is hierarchical: ALL > PEN > LIV, PKS; ALL > SKADE. Filter to a single virktypnb to avoid double-counting. For total sector, use virktypnb='ALL'.
- balpostnat1 is hierarchical: FPT (1. total) is the sum of GSP (1.1), MRP (1.2), PRA (1.3), ERS (1.4), OEV (1.5). KB (1.1.1) is a child of GSP. To get total provisions use balpostnat1='FPT'.
- Typical query: SELECT tid, SUM(indhold) FROM fact.dnfphen WHERE virktypnb='ALL' AND vaerdi1='ULTIM' AND balpostnat1='FPT' GROUP BY tid — gives total pension provisions over time.