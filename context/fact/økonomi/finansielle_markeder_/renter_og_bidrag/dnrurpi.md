table: fact.dnrurpi
description: Pengeinstitutternes udestående indenlandske forretninger - Rentemarginaler efter instituttype, datatype, indenlandsk sektor, valuta og tid
measure: indhold (unit Pct.)
columns:
- institype: values [ALLE=Pengeinstitutter i alt, 1=- Store pengeinstitutter, 2=- Mellemstore pengeinstitutter]
- data: values [RENM=Rentemarginal (procentpoint), RENMEXREP=Rentemarginal ekskl. repoforretninger (procentpoint)]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md
notes:
- data is a measurement selector: RENM=interest margin (procentpoint), RENMEXREP=margin excl. repo transactions (procentpoint). Always filter to one.
- valuta: the dim.valuta_iso join fails for Z01 (Alle valutaer). Z01 is an aggregate total — use it directly as a filter value, not a join key. DKK and EUR match the dim but the join is unnecessary since there are only 3 currency values.
- institype: ALLE=all banks combined, 1=store pengeinstitutter, 2=mellemstore pengeinstitutter. Filter to ALLE for overall margin; 1 and 2 are sub-totals (don't sum them to get ALLE).
- indsek: 1000=all sectors (total), 1100/1300/1400/1500 are top-level, 1410/1430 are sub-sectors of 1400.
- Interest margins here represent the spread between lending and deposit rates at the institution level, not per-borrower margins.
