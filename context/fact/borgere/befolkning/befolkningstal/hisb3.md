table: fact.hisb3
description: Nøgletal om befolkningen efter bevægelsesart og tid
measure: indhold (unit Antal)
columns:
- bevaegelse: values [M+K=Befolkning 1. januar (i 1000), M=Mænd 1. januar (i 1000), K=Kvinder 1. januar (i 1000), LFT=Levendefødte i alt, LFD=Levendefødte drenge ... VIB=Borgerlige vielser, OÆT=Opløste ægteskaber i alt, OKD=Opløste ægteskaber, kones død, OMD=Opløste ægteskaber, mands død, OSK=Skilsmisser]
- tid: date range 1901-01-01 to 2025-01-01

notes:
- CRITICAL mixed units: M+K, M, K are population counts in THOUSANDS (i 1000), while all other bevaegelse codes (LFT, LFD, DT, DK, DM, IND, UDV, etc.) are absolute event counts. The unit label "Antal" is misleading — M+K=5993 means 5,993,000 people, not 5,993.
- Never sum across bevaegelse — each code is a distinct measure.
- 27 distinct bevaegelse codes covering: population stock (M+K, M, K), births (LFT, LFD, LFP), deaths (DT, DK, DM), marriages (VIE, VIB, VIT), divorces/dissolutions (FUÆ, OSK, OÆT, OKD, OMD, UÆF), and immigration/emigration (IND, UDV).
- Back to 1901 for all codes. Best for long-run trend overview of key demographic indicators.
- No geographic breakdown — national aggregates only.