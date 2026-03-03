table: fact.forsk112
description: Erhvervslivets udgifter til egen FoU efter branche - størrelsesgruppe - region mv, fag og tid
measure: indhold (unit Mio. kr.)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- vidomr: values [10=Naturvidenskab, 20=Teknisk videnskab, 30=Sundhedsvidenskab, 40=Jordbrugs- og veterinærvidenskab, 50=Samfundsvidenskab, 60=Humaniora]
- tid: date range 2017-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown (industry 1000–1090, technology level, IT, knowledge services, size groups, regions).
- vidomr has 6 scientific field codes (10–60) with no aggregate total — sum all six to get the combined total.
- Shortest time series in the forsk* family: starts 2017. For longer industry-by-spending series, use forsk01.
- Map: /geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
