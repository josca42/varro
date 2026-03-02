table: fact.dnruum
description: Udestående indenlandsk udlån fra MFI-sektoren ekskl. Nationalbanken efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid), formål og tid
measure: indhold (unit -)
columns:
- instrnat: values [AL00=Udlån i alt, AL20=- Kassekreditter (revolverende lån) og overtræk, AL00EXAL20=- Ekskl. kassekreditter (revolverende lån) og overtræk]
- data: values [EFFR=Effektiv rentesats (pct.), PAAR=Rentebetalinger inkl. bidrag (mio. kr.), GNSB=Forretningsomfang (mio. kr.)]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1200=- 1200: Finansielle selskaber, 12CC=- - heraf 12cc: Forsikringsselskaber og pensionskasser, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, S1A=Over 1 år]
- formal: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, EXB=Ej boligformål for udlån til husholdninger]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md
notes:
- data is a measurement selector — three incompatible units: EFFR=effective interest rate (pct), PAAR=interest+contribution payments (mio. kr.), GNSB=outstanding loan volume (mio. kr.). Always filter data to a single value; mixing them silently produces nonsense.
- instrnat has hierarchy: AL00=all loans (total), AL20=kassekreditter (sub-total), AL00EXAL20=excl. kassekreditter (sub-total). Filter to AL00 for the full total, or to one sub-category.
- indsek has hierarchy: 1000=alle sektorer (total), 1100/1200/1300/1400/1500 are top-level sectors, 12CC/1410/1430 are sub-sectors. To avoid double-counting, pick one hierarchy level: e.g. filter indsek IN ('1100','1200','1300','1400','1500') for top-level breakdown, or use 1000 for the grand total.
- valuta: Z01=alle valutaer (aggregate total), DKK and EUR are subsets of Z01. Do not sum Z01 with DKK and EUR — they overlap. For total, use Z01; for currency breakdown, use DKK and EUR. Z01 does not join to dim.valuta_iso.
- lobetid1: ALLE=all maturities (total), M1A and S1A are sub-totals. Filter to ALLE for the aggregate.
- formal: ALLE=alle formål (total), B=boligformål, EXB=ej boligformål. These are only meaningful for husholdninger loans (indsek=1400/1410/1430).
- For a clean query of total outstanding MFI loans: data='GNSB', instrnat='AL00', indsek='1000', valuta='Z01', lobetid1='ALLE', formal='ALLE'.
