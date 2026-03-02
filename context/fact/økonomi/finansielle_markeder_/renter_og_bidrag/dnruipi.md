table: fact.dnruipi
description: Udestående indenlandsk indlån i pengeinstitutter efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
measure: indhold (unit -)
columns:
- instrnat: values [PL00=Indlån i alt, PL10= - Transferable indlån (anfordring), PL20= - Dag til dag-indskud, PL30= - Elektroniske penge, PL4P= - Tidsindskud ekskl. puljer, PL5P= - Indlån med opsigelse ekskl. puljer, PL6P= - Repoindlån ekskl. puljer]
- data: values [EFFR=Effektiv rentesats (pct.), PAAR=Rentebetalinger (mio. kr.), GNSB=Forretningsomfang (mio. kr.)]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1200=- 1200: Finansielle selskaber, 12CC=- - heraf 12cc: Forsikringsselskaber og pensionskasser, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, 3M=- Op til og med 3 mdr., 1A=- Over 3 mdr. og op til og med 1 år, S1A=Over 1 år, 2A=- Over 1 år og op til og med 2 år, S2A=- Over 2 år, 5A=- - Over 2 år og op til og med 5 år, S5A=- - Over 5 år]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- data is a measurement selector: EFFR=effective interest rate (pct), PAAR=interest payments (mio. kr.), GNSB=outstanding deposit volume (mio. kr.). Always filter to one value.
- instrnat has hierarchy: PL00=all deposits (total), PL10/PL20/PL30/PL4P/PL5P/PL6P are sub-categories. Filter to PL00 for the total.
- indsek has hierarchy: 1000=all sectors (total), 1100/1200/1300/1400/1500 are top-level, 12CC/1410/1430 are sub-sectors. Pick one level.
- valuta is inline here (no dim join): Z01=all currencies (total), DKK and EUR are subsets. Don't sum Z01+DKK+EUR.
- lobetid1 has nested aggregates: ALLE=all maturities, M1A includes 3M and 1A; S1A includes 2A and S2A. Filter to ALLE for the total, or pick one non-overlapping leaf.
- This is pengeinstitutter deposits (indlån). For MFI-sector total deposits, see dnruim.
