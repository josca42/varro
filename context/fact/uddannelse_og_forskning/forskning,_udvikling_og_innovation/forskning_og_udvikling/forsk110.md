table: fact.forsk110
description: Erhvervslivets finansiering af udgifter til egen FoU efter branche - størrelsesgruppe - region mv, finansieringskilde og tid
measure: indhold (unit Mio. kr.)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- finanskilde: values [10=Finansiering af FoU i alt, 20=Private erhverv i alt, 30=Egen finansiering, 40=Danske virksomheder i samme koncern, 50=Andre danske virksomheder, 60=Private ikke profitdrevne organisationer i Danmark i alt, 70=Offentlige myndigheder/institutioner i Danmark i alt, 80=Videnskabsministeriet, 90=Andre statslige institutioner, 100=Regioner og kommuner, 110=Vækstfonden, 120=Udlandet i alt, 130=Udenlandske virksomheder i samme koncern, 140=Andre udenlandske virksomheder, 150=Private ikke profitdrevne organisationer i udlandet, 160=EU-midler, 170=Udenlandske offentlige myndigheder/institutioner]
- tid: date range 2013-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown (industry 1000–1090, technology level, IT, knowledge services, size groups, regions).
- finanskilde='10' = Finansiering af FoU i alt (grand total). The hierarchy: 10 = 20 (private erhverv) + 60 (private nonprofit) + 70 (offentlige) + 120 (udlandet). Under 20: 30+40+50. Under 70: 80+90+100+110. Under 120: 130+140+150+160+170. Never sum sub-codes with their parent totals.
- Covers financing of own R&D (intern). For financing of purchased R&D, use forsk111.
- Map: context/geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
