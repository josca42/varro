table: fact.dnruuri
description: Udestående indenlandsk udlån fra realkreditinstitutter efter datatype, indenlandsk sektor, valuta og tid
measure: indhold (unit -)
columns:
- data: values [AL51EFFR=Effektiv rentesats inkl. bidrag (pct.) (kun nominallån), AL51BIDS=Bidragssats (pct.) (kun nominallån), AL50PAAR=Rentebetalinger inkl. bidrag (mio. kr.), AL50GNSB=Forretningsomfang (mio. kr.)]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1200=- 1200: Finansielle selskaber, 12CC=- - heraf 12cc: Forsikringsselskaber og pensionskasser, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md
notes:
- data is a measurement selector — four values encoding both the metric type and loan category: AL51EFFR=effective rate incl. bidrag (pct, nominallån only), AL51BIDS=bidragssats (pct, nominallån only), AL50PAAR=interest+contribution payments (mio. kr.), AL50GNSB=outstanding volume (mio. kr.). Always filter to one.
- indsek has hierarchy: 1000=alle sektorer (total), 1100/1200/1300/1400/1500 are top-level sectors, 12CC/1410/1430 are sub-sectors. Pick one hierarchy level to avoid double-counting.
- valuta: Z01=alle valutaer (total), DKK and EUR are subsets. Don't sum Z01 with DKK/EUR. Z01 does not join to dim.valuta_iso.
- For total outstanding realkreditlån: data='AL50GNSB', indsek='1000', valuta='Z01'.
- This table is realkreditinstitutter only (not MFI/pengeinstitutter). For MFI total, see dnruum.
