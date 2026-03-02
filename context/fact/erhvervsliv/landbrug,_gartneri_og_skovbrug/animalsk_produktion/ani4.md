table: fact.ani4
description: Slagtninger og produktion af kvæg efter kategori, enhed og tid
measure: indhold (unit -)
columns:
- dyrkat: values [KVAEGIALT=Kvæg, i alt, VOKSKVAEGIALT=Voksent kvæg, i alt, KALVEIALT=Kalve, I alt, HANDYR=Handyr, TYRE=Tyre, UNGTYRE=Ungtyre, STUDE=Stude, KVIER=Kvier, KOER=Køer, FEDEKALVE=Fedekalve, SPAEDEKALVE=Spædekalve, VOKSKVAEGEKS=Voksent kvæg, eksport af levende dyr, KALVEEKS=Kalve, eksport af levende dyr]
- enhed: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), GENSLAG=Gennemsnitlig slagtet vægt (kg.), PROD=Produktion (mio.kg.), PRISER=Gennemsnitspriser (øre pr. kg. slagtet vægt), SALG=Salgsværdi (mio. kr.)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- `enhed` is a measurement selector — always filter to exactly one value. The 5 measures are: SLAGEKS (count, 1.000 stk.), GENSLAG (avg slaughter weight, kg), PROD (production, mio.kg), PRISER (price, øre/kg slagtet vægt), SALG (value, mio.kr). Summing across enhed is nonsensical.
- `dyrkat` has a 3-level aggregate hierarchy: KVAEGIALT (all cattle) > VOKSKVAEGIALT (adult) + KALVEIALT (calves) > TYRE/UNGTYRE/STUDE/KVIER/KOER (adult sub-types) + FEDEKALVE/SPAEDEKALVE (calf sub-types). HANDYR = TYRE + UNGTYRE + STUDE (all adult males). Do not sum multiple hierarchy levels together.
- VOKSKVAEGEKS and KALVEEKS = export of live animals, not domestic slaughter. These are separate from the slaughter hierarchy — KVAEGIALT is not their aggregate.
- Annual data (1990-2024). For monthly data from 1995, use ani41.