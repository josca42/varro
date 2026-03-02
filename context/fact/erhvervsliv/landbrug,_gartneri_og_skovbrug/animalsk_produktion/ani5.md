table: fact.ani5
description: Slagtninger og produktion af svin efter kategori, enhed og tid
measure: indhold (unit -)
columns:
- dyrkat: values [SVINIALT=Svin, i alt, POLTE=Polte, SOER=Søer, ORNER=Orner, SLAGTSVIN=Slagtesvin, PRODUCENT=For producent, KASSERED=Kasserede, SLPRODUCENT=Slagtninger hos Producent, EKSPORT1=Eksport af levende svin i alt]
- enhed: values [SLAGEKS=Slagtninger og eksport af levende dyr (1.000 stk.), GENSLAG=Gennemsnitlig slagtet vægt (kg.), PROD=Produktion (mio.kg.), PRISER=Gennemsnitspriser (øre pr. kg. slagtet vægt), SALG=Salgsværdi (mio. kr.), PRISRELA=Prisrelation svinekød/foderbyg (relationstal)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- `enhed` is a measurement selector — always filter to exactly one: SLAGEKS (count, 1.000 stk.), GENSLAG (avg weight, kg), PROD (mio.kg), PRISER (price, øre/kg), SALG (mio.kr), PRISRELA (price relation svinekød/foderbyg). PRISER and PRISRELA are only available for SLAGTSVIN, not SVINIALT.
- `dyrkat` is NOT a clean hierarchy — the values mix two classification systems: (1) by animal type at abattoirs: SLAGTSVIN, SOER, POLTE, ORNER; (2) by slaughter location/status: PRODUCENT (for producer), SLPRODUCENT (slaughtered at producer), KASSERED (rejected). EKSPORT1 = live pig exports. SVINIALT = grand total including all. These categories overlap — never sum all dyrkat values.
- SVINIALT is significantly larger than SLAGTSVIN+SOER+POLTE+ORNER because SVINIALT includes producer-side slaughter not broken out by animal type.
- Annual data (1990-2024). For monthly data from 1995, use ani51.