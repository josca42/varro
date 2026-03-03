table: fact.forsk111
description: Erhvervslivets finansiering af udgifter til købte FoU-tjenester efter branche - størrelsesgruppe - region mv, finansieringskilde og tid
measure: indhold (unit Mio. kr.)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- finanskilde: values [10=Finansiering af FoU i alt, 20=Private erhverv i alt, 30=Egen finansiering, 40=Danske virksomheder i samme koncern, 50=Andre danske virksomheder, 60=Private ikke profitdrevne organisationer i Danmark i alt, 70=Offentlige myndigheder/institutioner i Danmark i alt, 80=Videnskabsministeriet, 90=Andre statslige institutioner, 100=Regioner og kommuner, 110=Vækstfonden, 120=Udlandet i alt, 130=Udenlandske virksomheder i samme koncern, 140=Andre udenlandske virksomheder, 150=Private ikke profitdrevne organisationer i udlandet, 160=EU-midler, 170=Udenlandske offentlige myndigheder/institutioner]
- tid: date range 2013-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown.
- finanskilde='10' = grand total. Same hierarchy as forsk110: 10 = 20 + 60 + 70 + 120 with sub-items. Never sum sub-codes with parent totals.
- Covers financing of purchased R&D (købt). For financing of own R&D, use forsk110.
- Map: /geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
