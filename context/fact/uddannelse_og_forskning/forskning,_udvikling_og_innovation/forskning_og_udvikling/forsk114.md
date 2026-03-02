table: fact.forsk114
description: FoU-årsværk i erhvervslivet efter branche - størrelsesgruppe - region mv, personaletype, køn og tid
measure: indhold (unit Årsværk)
columns:
- fui01: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1020=Bygge og anlæg, 1030=Handel, 1040=Transport ... 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland, 81=Region Nordjylland]
- perstyp: values [400=FoU-årsværk i alt, 410=Forskere, 420=Andet personale, inkl. teknisk personale]
- koen: values [0=Køn i alt, 2=Mænd, 1=Kvinder]
- tid: date range 2013-01-01 to 2023-01-01
notes:
- fui01 encodes multiple classification perspectives — pick exactly ONE per query. See forsk01 notes for the full breakdown (industry 1000–1090, technology level, IT, knowledge services, size groups, regions).
- perstyp='400' = FoU-årsværk i alt (total). 410=Forskere and 420=Andet personale are sub-components summing to 400.
- koen='0' = Køn i alt (total), koen='1' = Kvinder, koen='2' = Mænd. Gender breakdown not available for all years and fui01 sub-categories — use koen='0' for safe totals.
- This measures FTE (årsværk). For headcount (Antal), use forsk113.
- Map: context/geo/regioner.parquet — filter fui01 IN (81,82,83,84,85) for the region perspective, then merge on fui01=dim_kode.
