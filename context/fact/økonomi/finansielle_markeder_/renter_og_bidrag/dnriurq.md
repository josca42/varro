table: fact.dnriurq
description: Realkreditinstitutternes udestående indenl. realkreditudlån - Kvartalsvis ydelse efter datatype, indenlandsk sektor, valuta og tid
measure: indhold (unit Pct.)
columns:
- data: values [AL51EFFRKV=Effektiv rentesats inkl. bidrag (pct.) (kun nominallån), AL51BIDSKV=Bidragssats (pct.) (kun nominallån), AL50YDEL=Samlet ydelse (mio. kr.), AL50PAARKV=Rentebetalinger inkl. bidrag (mio. kr.), AL50BIDBKV=Bidragsbetalinger (mio. kr.), AL50OA=Ordinære afdrag (mio. kr.)]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- tid: date range 2013-10-01 to 2025-07-01
notes:
- data is a measurement selector with mixed units: AL51EFFRKV=effective rate incl. bidrag (pct), AL51BIDSKV=bidragssats (pct), AL50YDEL=total quarterly payment (mio. kr.), AL50PAARKV=interest+contribution payments (mio. kr.), AL50BIDBKV=contribution payments (mio. kr.), AL50OA=principal repayments (mio. kr.). Always filter to one.
- indsek has no total row. Values: 1100, 1400, 1410, 1430, 1500. Avoid summing 1400 with sub-sectors 1410/1430.
- valuta: Z01=all currencies, DKK and EUR are subsets. Don't sum across them.
- Quarterly frequency (tid is quarter-start dates). Data from 2013-Q4 only — shortest series in this subject.
- Covers only nominallån (nominal-rate mortgage loans) for the rate/contribution metrics — indexed loans excluded.
- AL50YDEL = AL50PAARKV + AL50OA (total payment = interest/contribution + principal). Don't double-count by summing sub-components.
