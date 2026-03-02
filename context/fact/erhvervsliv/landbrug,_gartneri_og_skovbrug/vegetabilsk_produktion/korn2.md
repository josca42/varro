table: fact.korn2
description: Lager og omsætning af korn efter afgrøde, aktører og tid
measure: indhold (unit Mio. kg)
columns:
- afgrode: values [H95=KORN I ALT, H105=Hvede, H130=Rug, H145=Byg, H146=Havre inkl. blandsæd, H147=Triticale, H148=Majs m.v., H149=Foderærter]
- ak: values [K10=Lager ultimo, hos kornhandlere, K20=Lager ultimo, hos landmænd, K30=Indvejet hos kornhandlere, K40=Afregnet af kornhandlere]
- tid: date range 2000-01-01 to 2024-07-01

notes:
- ak has 4 conceptually distinct values: K10=Lager hos kornhandlere (stock at traders), K20=Lager hos landmænd (stock at farms), K30=Indvejet hos kornhandlere (intake), K40=Afregnet af kornhandlere (settled). These are different concepts (stocks vs. flows) and must not be summed.
- afgrode=H95 (KORN I ALT) is the aggregate. Specific crops (H105-H149) are children. Don't sum H95 with specific crops.
- The tid column goes to monthly granularity (e.g. 2024-07-01), making this useful for within-year stock monitoring.
- No regional breakdown. National-level only.