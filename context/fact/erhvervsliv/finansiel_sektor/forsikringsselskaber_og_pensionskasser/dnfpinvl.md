table: fact.dnfpinvl
description: Forsikrings- og pensionssektorens investeringer efter virksomhedstype, værdier, investeringstype, sektor, land og tid
measure: indhold (unit Mia. kr.)
columns:
- virktypnb: values [ALL=1. Forsikrings- og pensionssektoren i alt, PEN=1.1. Pensionsselskaber, LIV=1.1.1. Livsforsikringsselskaber, PKS=1.1.2. Pensionskasser, SKADE=1.2. Skadesforsikringsselskaber, LOOKTHR=2. Forsikrings- og pensionssektoren i alt, hvor danske investeringsforeninger er gennemlyst]
- vaerdi1: values [BEHOLD=1. Beholdninger, NETTRANS=2. Nettotransaktioner]
- investnat: values [ALLINV=1. Investeringer, i alt, AKTIER=1.1. Aktier og andre kapitalandele, NONNOT=1.1.1. Ikke-børsnoteret , INVFOR=1.2. Investeringsforeninger, OBL=1.3. Obligationer, STATER=1.3.1. Statsobligationer, REALER=1.3.2. Realkreditobligationer, DERIVAT=1.4. Derivater, RENDER=1.4.1. Rentederivater (valuta ufordelt), VALDER=1.4.2. Valutaderivater (valuta ufordelt), LIKVID=1.5. Indskud og nettoudlån, LAAN=1.5.1. Nettoudlån]
- sektornat: values [1000=1. Alle sektorer, 1100=1.1. Ikke-finansielle selskaber, 11LZ=1.1.1. Ejendomme, 1200=1.2. Finansielle selskaber]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 3, 4]
- tid: date range 2015-01-01 to 2025-09-01
dim docs: /dim/lande_uht_bb.md

notes:
- vaerdi1 is a measurement selector: BEHOLD (holdings stock at period end) vs NETTRANS (net transactions during period). Always filter to one — they represent fundamentally different things. For investment portfolio size use BEHOLD.
- land joins dim.lande_uht_bb at [approx] — same 8 custom aggregate codes as dnfpafkl: W0=Hele verden, DK=Danmark, W1=Resten af verden, B5=EU-28, I8=Eurolande, P1=OECD, R7=BRIK, R12=Offshore centre, A6=Nord- og Mellemamerika. Use ColumnValues("dnfpinvl", "land") for all 29 codes with labels. Use land='W0' for total across all countries.
- virktypnb is hierarchical: ALL > PEN > LIV, PKS; ALL > SKADE; LOOKTHR is independent (look-through alternative). Filter to one value.
- investnat is hierarchical: ALLINV > AKTIER > NONNOT; ALLINV > INVFOR; ALLINV > OBL > STATER, REALER; ALLINV > DERIVAT > RENDER, VALDER; ALLINV > LIKVID > LAAN. Note: RENDER and VALDER have "(valuta ufordelt)" label here (unlike dnfpafkl) meaning currency is not broken out for derivatives. Use ALLINV for totals.
- sektornat: 1000=total, use it for sector-wide figures.
- Minimal total query: WHERE virktypnb='ALL' AND vaerdi1='BEHOLD' AND investnat='ALLINV' AND sektornat='1000' AND land='W0'.