table: fact.dnfpbal
description: Forsikrings- og pensionssektorens balance efter virksomhedstype, værdier, balancepost og tid
measure: indhold (unit Mia. kr.)
columns:
- virktypnb: values [ALL=1. Forsikrings- og pensionssektoren i alt, PEN=1.1. Pensionsselskaber, LIV=1.1.1. Livsforsikringsselskaber, PKS=1.1.2. Pensionskasser, SKADE=1.2. Skadesforsikringsselskaber]
- vaerdi1: values [BEHOLD=1. Beholdninger, NETTRANS=2. Nettotransaktioner]
- balpostnat1: values [FINAKT=1. Finansielle aktiver, i alt, VAERDI=1.1. Værdipapirer, EJERAN=1.1.1. Aktier og investeringsforeninger, OBL=1.1.2. Obligationer, OEVAKT=1.2. Øvrige aktiver, FINPAS=2. Finansielle passiver, i alt, EGNKAP=2.1. Egenkapital, HENSAT=2.2. Hensættelser, GNSRNT=2.2.1. Hensættelser til gennemsnitsrenteprodukter, MARKED=2.2.2. Hensættelser til markedsrenteprodukter, SKADEH=2.2.3. Hensættelser til skadesforsikring, OEVHEN=2.2.4. Øvrige hensættelser, OEVPAS=2.3. Øvrige passiver]
- tid: date range 2015-01-01 to 2025-04-01

notes:
- vaerdi1 is a measurement-type selector: BEHOLD (balance stock at period end) vs NETTRANS (net transactions during period). Always filter to one — mixing them is meaningless. For a balance sheet snapshot use BEHOLD; for flow analysis use NETTRANS.
- virktypnb is hierarchical: ALL (total) > PEN (pension companies) > LIV (life insurance), PKS (pension funds); ALL > SKADE (non-life insurance). Filter to a single niveau to avoid double-counting. ALL is the sector total.
- balpostnat1 is hierarchical. FINAKT (1. Financial assets total) and FINPAS (2. Financial liabilities total) are top-level. Children of FINAKT: VAERDI (1.1), EJERAN (1.1.1), OBL (1.1.2), OEVAKT (1.2). Children of FINPAS: EGNKAP (2.1), HENSAT (2.2), GNSRNT (2.2.1), MARKED (2.2.2), SKADEH (2.2.3), OEVHEN (2.2.4), OEVPAS (2.3). To avoid double-counting, pick one level and filter. A simple sector total: virktypnb='ALL', vaerdi1='BEHOLD', balpostnat1='FINAKT' (or 'FINPAS').
- Total balance check: FINAKT = FINPAS (balance sheet identity). At tid='2025-01-01', virktypnb='ALL', both sides = 5415 Mia. kr.