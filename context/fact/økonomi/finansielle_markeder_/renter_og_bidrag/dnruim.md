table: fact.dnruim
description: Udestående indenlandsk indlån i MFI-sektoren ekskl. Nationalbanken efter datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
measure: indhold (unit -)
columns:
- data: values [PL00EFFR=Effektiv rentesats (pct.), PL00PAAR=Rentebetalinger inkl. bidrag (mio. kr.), PL00GNSB=Forretningsomfang (mio. kr.)]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1200=- 1200: Finansielle selskaber, 12CC=- - heraf 12cc: Forsikringsselskaber og pensionskasser, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, S1A=Over 1 år]
- tid: date range 2013-06-01 to 2025-09-01
notes:
- data is a measurement selector: PL00EFFR=effective interest rate (pct), PL00PAAR=interest payments (mio. kr.), PL00GNSB=outstanding deposit volume (mio. kr.). Always filter to one value.
- indsek has hierarchy: 1000=all sectors (total), 1100/1200/1300/1400/1500 are top-level, 12CC/1410/1430 are sub-sectors. Pick one hierarchy level.
- valuta: Z01=all currencies (total), DKK and EUR are subsets. Don't sum across Z01+DKK+EUR.
- lobetid1: ALLE=all maturities, M1A and S1A are sub-totals. Filter to ALLE for aggregate.
- This table covers MFI-sector (excl. Nationalbanken) deposits from 2013-06 onwards. For pengeinstitutter specifically (longer series from 2003), use dnruipi.
