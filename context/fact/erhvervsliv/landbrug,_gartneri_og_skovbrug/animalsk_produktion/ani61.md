table: fact.ani61
description: Slagtninger og produktion af fjerkræ efter kategori, enhed og tid
measure: indhold (unit -)
columns:
- dyrkat: values [FJERKRIALT=Slagtninger af fjerkræ i alt, FJERKREKS=Slagtninger og eksport af fjerkræ i alt, KYLLING=Slagtninger af kyllinger, HONS=Slagtninger af høns, AENDER=Slagtninger af ænder, GAES=Slagtninger af gæs, KALKUN=Slagtninger af kalkuner, EKSPORT=Eksport af levende fjerkræ i alt, EKSPORTDAG=Eksport af daggammelt fjerkræ, EKSPORTANDET=Eksport af andet fjerkræ, SLPRODUCENT=Slagtninger hos Producent]
- enhed: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), PROD=Produktion (mio.kg.), PRISKYL=Noteringer for fjerkræ (øre pr. kg levende vægt), SALG=Salgsværdi (mio. kr.)]
- tid: date range 1995-01-01 to 2025-04-01

notes:
- Same structure as ani6 (annual fjerkræ table) but quarterly frequency.
- `enhed` selector — filter to one: SLAGEKS, PROD, PRISKYL (KYLLING only), SALG.
- `dyrkat` hierarchy: FJERKREKS = FJERKRIALT + EKSPORT (verified). EKSPORT = EKSPORTDAG + EKSPORTANDET. Species (KYLLING, HONS, AENDER, GAES, KALKUN) don't sum to FJERKRIALT because SLPRODUCENT is included separately. GAES and HONS have incomplete year coverage.
- Quarterly data from 1995. For annual aggregates back to 1990, use ani6.