table: fact.ani6
description: Slagtninger og produktion af fjerkræ efter kategori, enhed og tid
measure: indhold (unit -)
columns:
- dyrkat: values [FJERKRIALT=Slagtninger af fjerkræ i alt, FJERKREKS=Slagtninger og eksport af fjerkræ i alt, KYLLING=Slagtninger af kyllinger, HONS=Slagtninger af høns, AENDER=Slagtninger af ænder, GAES=Slagtninger af gæs, KALKUN=Slagtninger af kalkuner, EKSPORT=Eksport af levende fjerkræ i alt, EKSPORTDAG=Eksport af daggammelt fjerkræ, EKSPORTANDET=Eksport af andet fjerkræ, SLPRODUCENT=Slagtninger hos Producent]
- enhed: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), PROD=Produktion (mio.kg.), PRISKYL=Noteringer for fjerkræ (øre pr. kg levende vægt), SALG=Salgsværdi (mio. kr.)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- `enhed` is a measurement selector — filter to one: SLAGEKS (count, 1.000 stk.), PROD (mio.kg), PRISKYL (price, øre/kg levende vægt), SALG (mio.kr). PRISKYL is only available for KYLLING.
- `dyrkat` hierarchy: FJERKREKS (total incl. live exports) = FJERKRIALT (slaughter only) + EKSPORT (live exports). EKSPORT = EKSPORTDAG + EKSPORTANDET. SLPRODUCENT (slaughtered at producer) is part of FJERKRIALT but is also listed separately. Species: KYLLING, HONS, AENDER, GAES, KALKUN — but note GAES and HONS have shorter series (not all years have data).
- FJERKRIALT ≠ simple sum of species because SLPRODUCENT is included separately; the species rows don't cover all slaughter.
- Annual data (1990-2024). For quarterly data from 1995, use ani61.