table: fact.forsk09
description: Erhvervslivets FoU-driftsudgifter efter branche - størrelsesgruppe - region mv, forskningstype og tid
measure: indhold (unit Mio. kr.)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- fui14: values [440=Grundforskning, 450=Anvendt forskning, 460=Udviklingsarbejde]
- tid: date range 2013-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown (industry 1000–1090, technology level, IT, knowledge services, size groups, regions).
- fui14 has only three exhaustive research-type codes with no aggregate total — sum all three to get combined driftsudgifter.
- This table covers driftsudgifter only (not capital investments). For total FoU spending including investments, use forsk01 (fui08='10').
- Udviklingsarbejde (460) dominates: ~57% of driftsudgifter in 2023, followed by anvendt forskning ~37%, grundforskning ~5%.
- Map: context/geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
