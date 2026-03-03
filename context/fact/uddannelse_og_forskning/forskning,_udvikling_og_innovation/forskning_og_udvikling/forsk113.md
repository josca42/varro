table: fact.forsk113
description: FoU-personale i erhvervslivet efter branche - størrelsesgruppe - region mv, personaletype, køn og tid
measure: indhold (unit Antal)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- perstyp: values [300=FoU-personale i alt, 310=Forskere, 320=Andet personale, inkl. teknisk personale]
- koen: values [0=Køn i alt, 2=Mænd, 1=Kvinder]
- tid: date range 2013-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown (industry 1000–1090, technology level, IT, knowledge services, size groups, regions).
- perstyp='300' = FoU-personale i alt (total). 310=Forskere and 320=Andet personale are sub-components summing to 300.
- koen='0' = Køn i alt (total), koen='1' = Kvinder, koen='2' = Mænd. Filter to koen='0' for totals; use koen='1' or '2' for gender breakdown.
- This counts headcount (Antal). For FTE (årsværk), use forsk114.
- Map: /geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
