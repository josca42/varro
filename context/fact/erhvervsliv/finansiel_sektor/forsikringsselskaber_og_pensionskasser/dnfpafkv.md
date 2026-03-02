table: fact.dnfpafkv
description: Forsikrings- og pensionssektorens afkast af investeringer efter virksomhedstype, værdier, investeringstype, sektor, valuta og tid
measure: indhold (unit Mia. kr.)
columns:
- virktypnb: values [ALL=1. Forsikrings- og pensionssektoren i alt, PEN=1.1. Pensionsselskaber, LIV=1.1.1. Livsforsikringsselskaber, PKS=1.1.2. Pensionskasser, SKADE=1.2. Skadesforsikringsselskaber, LOOKTHR=2. Forsikrings- og pensionssektoren i alt, hvor danske investeringsforeninger er gennemlyst]
- vaerdi1: values [AFKPCT=1. Afkast i procent, AFKDKK=2. Afkast, AFKUVAL=3. Afkast uden valutaændringer]
- investnat: values [ALLINV=1. Investeringer, i alt, AKTIER=1.1. Aktier og andre kapitalandele, NONNOT=1.1.1. Ikke-børsnoteret , INVFOR=1.2. Investeringsforeninger, OBL=1.3. Obligationer, STATER=1.3.1. Statsobligationer, REALER=1.3.2. Realkreditobligationer, DERIVAT=1.4. Derivater, RENDER=1.4.1. Rentederivater, VALDER=1.4.2. Valutaderivater, LIKVID=1.5. Indskud og nettoudlån, LAAN=1.5.1. Nettoudlån]
- sektornat: values [1000=1. Alle sektorer, 1100=1.1. Ikke-finansielle selskaber, 11LZ=1.1.1. Ejendomme, 1200=1.2. Finansielle selskaber]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2015-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- vaerdi1 is critical: AFKPCT is return as a percentage rate — never sum it. AFKDKK is return in Mia. kr., AFKUVAL is return excluding currency changes in Mia. kr. Always filter vaerdi1 to one type.
- valuta joins dim.valuta_iso but two codes are custom aggregates not in the dim: Z01=Alle valutaer (all currencies, the total), Z41=Udenlandsk valuta i alt ekskl. derivater (total foreign currency ex. derivatives). The 8 individual currencies (DKK, EUR, USD, CHF, GBP, JPY, NOK, SEK) are matched. Note: column_values shows all valuta labels with "(ekskl. derivater)" suffix — derivatives are recorded separately in investnat. Use ColumnValues("dnfpafkv", "valuta") to see all 10 codes.
- virktypnb, investnat, sektornat hierarchies: same structure as dnfpafkl — see those notes. LOOKTHR is a parallel aggregate, not a child of ALL.
- Minimal total query: WHERE virktypnb='ALL' AND vaerdi1='AFKDKK' AND investnat='ALLINV' AND sektornat='1000' AND valuta='Z01'.