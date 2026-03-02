table: fact.ani41
description: Slagtninger og produktion af kvæg efter kategori, enhed og tid
measure: indhold (unit -)
columns:
- dyrkat: values [KVAEGIALT=Kvæg, i alt, VOKSKVAEGIALT=Voksent kvæg, i alt, KALVEIALT=Kalve, I alt, HANDYR=Handyr, TYRE=Tyre, UNGTYRE=Ungtyre, STUDE=Stude, KVIER=Kvier, KOER=Køer, FEDEKALVE=Fedekalve, SPAEDEKALVE=Spædekalve, VOKSKVAEGEKS=Voksent kvæg, eksport af levende dyr, KALVEEKS=Kalve, eksport af levende dyr]
- enhed: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), GENSLAG=Gennemsnitlig slagtet vægt (kg.), PROD=Produktion (mio.kg.), PRISER=Gennemsnitspriser (øre pr. kg. slagtet vægt), SALG=Salgsværdi (mio. kr.)]
- tid: date range 1995-01-01 to 2025-08-01

notes:
- Same structure as ani4 (annual kvæg table) but monthly frequency.
- `enhed` is a measurement selector — always filter to exactly one: SLAGEKS (count), GENSLAG (avg weight), PROD (production), PRISER (price), SALG (value).
- `dyrkat` hierarchy: KVAEGIALT > VOKSKVAEGIALT + KALVEIALT > individual animal types. HANDYR = TYRE + UNGTYRE + STUDE. VOKSKVAEGEKS/KALVEEKS are live animal exports, not part of the slaughter hierarchy.
- Monthly data from 1995. For annual aggregates back to 1990, use ani4.