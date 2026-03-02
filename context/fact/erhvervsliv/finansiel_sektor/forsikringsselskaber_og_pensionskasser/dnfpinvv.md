table: fact.dnfpinvv
description: Forsikrings- og pensionssektorens investeringer efter virksomhedstype, markedsværdier, investeringstype, sektor, valuta og tid
measure: indhold (unit Mia. kr.)
columns:
- virktypnb: values [ALL=1. Forsikrings- og pensionssektoren i alt, PEN=1.1. Pensionsselskaber, LIV=1.1.1. Livsforsikringsselskaber, PKS=1.1.2. Pensionskasser, SKADE=1.2. Skadesforsikringsselskaber, LOOKTHR=2. Forsikrings- og pensionssektoren i alt, hvor danske investeringsforeninger er gennemlyst]
- markvaerdi: values [BEHOLD=1. Beholdninger, NETTRANS=2. Nettotransaktioner]
- investnat: values [ALLINV=1. Investeringer, i alt, AKTIER=1.1. Aktier og andre kapitalandele, NONNOT=1.1.1. Ikke-børsnoteret , INVFOR=1.2. Investeringsforeninger, OBL=1.3. Obligationer, STATER=1.3.1. Statsobligationer, REALER=1.3.2. Realkreditobligationer, DERIVAT=1.4. Derivater, RENDER=1.4.1. Rentederivater (valuta ufordelt), VALDER=1.4.2. Valutaderivater (valuta ufordelt), LIKVID=1.5. Indskud og nettoudlån, LAAN=1.5.1. Nettoudlån]
- sektornat: values [1000=1. Alle sektorer, 1100=1.1. Ikke-finansielle selskaber, 11LZ=1.1.1. Ejendomme, 1200=1.2. Finansielle selskaber]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2015-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- Note: this table uses markvaerdi instead of vaerdi1 for the measurement selector, but the values are identical: BEHOLD (market value of holdings) vs NETTRANS (net transactions). Always filter markvaerdi to one type. For portfolio size by currency use BEHOLD.
- valuta: same as dnfpafkv — Z01=Alle valutaer (total), Z41=Udenlandsk valuta i alt ekskl. derivater are custom aggregates not in dim.valuta_iso. Use ColumnValues("dnfpinvv", "valuta") to see all 10 codes. Use valuta='Z01' for all-currency total.
- virktypnb, investnat, sektornat: same hierarchies as dnfpafkl/dnfpinvl.
- Minimal total query: WHERE virktypnb='ALL' AND markvaerdi='BEHOLD' AND investnat='ALLINV' AND sektornat='1000' AND valuta='Z01'.