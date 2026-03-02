table: fact.ani51
description: Slagtninger og produktion af svin efter kategori, enhed og tid
measure: indhold (unit -)
columns:
- dyrkat: values [SVINIALT=Svin, i alt, POLTE=Polte, SOER=Søer, ORNER=Orner, SLAGTSVIN=Slagtesvin, PRODUCENT=For producent, KASSERED=Kasserede, SLPRODUCENT=Slagtninger hos Producent, EKSPORT1=Eksport af levende svin i alt]
- enhed: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), GENSLAG=Gennemsnitlig slagtet vægt (kg.), PROD=Produktion (mio.kg.), PRISER=Gennemsnitspriser (øre pr. kg. slagtet vægt), SALG=Salgsværdi (mio. kr.)]
- tid: date range 1995-01-01 to 2025-08-01

notes:
- Same structure as ani5 (annual svin table) but monthly frequency. Note: ani51 does not have PRISRELA in enhed (only in ani5 annual).
- `enhed` selector — always filter to one: SLAGEKS, GENSLAG, PROD, PRISER, SALG.
- `dyrkat` is NOT a clean hierarchy — mixes animal-type categories (SLAGTSVIN, SOER, POLTE, ORNER) with slaughter-location categories (PRODUCENT, SLPRODUCENT, KASSERED) and EKSPORT1. SVINIALT is the grand total. Never sum all dyrkat values.
- Monthly data from 1995. For annual aggregates back to 1990, use ani5.