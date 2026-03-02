table: fact.dnfpafkl
description: Forsikrings- og pensionssektorens afkast af investeringer, efter virksomhedstype, værdier, investeringstype, sektor, land og tid
measure: indhold (unit Mia. kr.)
columns:
- virktypnb: values [ALL=1. Forsikrings- og pensionssektoren i alt, PEN=1.1. Pensionsselskaber, LIV=1.1.1. Livsforsikringsselskaber, PKS=1.1.2. Pensionskasser, SKADE=1.2. Skadesforsikringsselskaber, LOOKTHR=2. Forsikrings- og pensionssektoren i alt, hvor danske investeringsforeninger er gennemlyst]
- vaerdi1: values [AFKPCT=1. Afkast i procent, AFKDKK=2. Afkast, AFKUVAL=3. Afkast uden valutaændringer]
- investnat: values [ALLINV=1. Investeringer, i alt, AKTIER=1.1. Aktier og andre kapitalandele, NONNOT=1.1.1. Ikke-børsnoteret , INVFOR=1.2. Investeringsforeninger, OBL=1.3. Obligationer, STATER=1.3.1. Statsobligationer, REALER=1.3.2. Realkreditobligationer, DERIVAT=1.4. Derivater, RENDER=1.4.1. Rentederivater, VALDER=1.4.2. Valutaderivater, LIKVID=1.5. Indskud og nettoudlån, LAAN=1.5.1. Nettoudlån]
- sektornat: values [1000=1. Alle sektorer, 1100=1.1. Ikke-finansielle selskaber, 11LZ=1.1.1. Ejendomme, 1200=1.2. Finansielle selskaber]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 3, 4]
- tid: date range 2015-01-01 to 2025-09-01
dim docs: /dim/lande_uht_bb.md

notes:
- vaerdi1 is critical: AFKPCT is return as a percentage rate — never sum it. AFKDKK is return in Mia. kr., AFKUVAL is return excluding currency changes in Mia. kr. Always filter vaerdi1 to a single type before aggregating.
- land joins dim.lande_uht_bb at [approx] because 8 codes are custom aggregate groups not in that dim: W0=Hele verden, DK=Danmark, W1=Resten af verden, B5=EU-28 inkl. Danmark, I8=Eurolande, P1=OECD-lande, R7=BRIK-lande, R12=Offshore centre, A6=Nord- og Mellemamerika. Use ColumnValues("dnfpafkl", "land") to see all 29 codes with labels. For individual countries, the 17 matched codes (DE, FR, GB, US, etc.) join dim.lande_uht_bb at niveau=4. W0 is the "all countries" total — use it for a sector-wide figure.
- virktypnb is hierarchical: ALL > PEN > LIV, PKS; ALL > SKADE. LOOKTHR is an independent alternative aggregate (look-through of domestic investment funds), not a child of ALL. Filter to one value. For sector totals use ALL.
- investnat is hierarchical: ALLINV > AKTIER > NONNOT; ALLINV > INVFOR; ALLINV > OBL > STATER, REALER; ALLINV > DERIVAT > RENDER, VALDER; ALLINV > LIKVID > LAAN. Never sum all investnat values. Filter to ALLINV for totals or pick non-overlapping children.
- sektornat: 1000=all sectors (total). 1100 (non-financial) and 1200 (financial) are children but do not sum to 1000 — 11LZ (real estate, child of 1100) is not shown at top level. Use 1000 for totals.
- Minimal total query: WHERE virktypnb='ALL' AND vaerdi1='AFKDKK' AND investnat='ALLINV' AND sektornat='1000' AND land='W0'.