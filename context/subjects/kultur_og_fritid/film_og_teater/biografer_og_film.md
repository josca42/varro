<fact tables>
<table>
id: bio1
description: Danske biografer, biografsale og faste siddepladser efter biografer/sale/sæder, biografstørrelse og tid
columns: sader, biograf, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: bio2
description: Aktivitet i danske biografer efter biograffilm/billetter, nationalitet og tid
columns: bio, nation2, tid (time), indhold (unit -)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: bio9
description: Biografer efter område, nøgletal, biografstørrelse og tid
columns: omrade, bnogle, biostor, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: bio4ta
description: Biograffilm/premierefilm efter biograffilm/billetter, type/målgruppe, filmens danske urpremiere, nationalitet og tid
columns: bio, typmal, urprim, nation2, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bio5
description: Biograffilm efter biograffilm/billetter, filmkategori, type/målgruppe, censur, nationalitet og tid
columns: bio, filmkat, typmal, censur, nation2, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bio6
description: Biograffilm efter nøgletal, spilleuge, nationalitet, type/målgruppe og tid
columns: aktp, spilleuge, nation2, typmal, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: kv2fs1
description: Forbrug af film og serier efter oprindelsesland, hyppighed, køn, alder og tid
columns: oprindland, hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fs2
description: Forbrug af film og serier efter lokation, køn, alder og tid
columns: lokation, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fs3
description: Forbrug af film og serier efter adgang, køn, alder og tid
columns: adgang, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fs4
description: Barrierer for brug af biografer efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: filmfin1
description: Finansiering af danske spillefilm efter finansieringstype, nøgletal og tid
columns: finanstype, aktp, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: filmfin2
description: Finansiering af danske spillefilm efter finansieringstype, målgruppe, nøgletal og tid
columns: finanstype, mlgrp, aktp, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: filmomk1
description: Omkostninger til produktion af danske spillefilm efter nøgletal, målgruppe og tid
columns: aktp, mlgrp, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: filmind1
description: Indtægter til danske spillefilm efter indtægtstype, målgruppe, nøgletal og tid
columns: indttype, mlgrp, aktp, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2021-01-01
</table>
</fact tables>

notes:
**Cinema infrastructure and activity (bio1, bio2, bio9)**
- bio1: counts of cinemas, screens, and seats by size category — 1980–2024. No geographic breakdown.
- bio2: ticket sales, revenue, and film counts by film nationality — 1980–2024. No geographic breakdown. Longest activity time series.
- bio9: same metrics as bio1/bio2 but broken down by geography and cinema size — 2014–2024 only. The omrade column mixes 4 geographic schemes (regioner, landsdele, specific large cities, city-size bands); pick one scheme per query. Supports choropleth maps: context/geo/regioner.parquet (omrade 81–85) or context/geo/landsdele.parquet (omrade 1–11) — merge on omrade=dim_kode.
- All three tables have measurement selector columns (sader/bio/bnogle) — always filter to a single metric before aggregating.

**Film statistics by type, nationality, and age rating (bio4ta, bio5, bio6)**
- bio4ta: most detailed — cross-tabulates film type (spillefilm/dok), audience (voksne/børn), premiere year, and nationality. 2007–2024.
- bio5: similar but adds censur (age rating) and filmkategori (foreviste vs. premierefilm). Fewer nationality options than bio4ta.
- bio6: percentage retention by week of cinema run (how long films stay in theaters). Values are not distributions — do not sum across spilleuge.
- All three share the same typmal hierarchy: 27=all → 47=all spillefilm (28+29) → 48=all dok (30+31). Filter to one level to avoid double-counting.

**Consumer survey data (kv2fs1–4, 2024 only)**
- Single-year survey (2024). Use for questions about how Danes consume film/series content.
- kv2fs1: viewing frequency by content type (dansk/udenlandsk film/serie) × age/gender. Content types are independent — do not sum.
- kv2fs2: where people watch (home, cinema, etc.). Locations are non-exclusive — do not sum.
- kv2fs3: access method (streaming, TV, DVD, etc.). Methods are non-exclusive — do not sum.
- kv2fs4: barriers to cinema attendance. Barriers are non-exclusive — do not sum. No age breakdown.

**Danish film economics (filmfin1, filmfin2, filmomk1, filmind1)**
- filmfin1: financing split by DK-vs-abroad origin (FI01=DK total, FI06=udland total). 2010–2023.
- filmfin2: financing split by type (offentlig/privat) and audience group (børn/voksne). Same period. filmfin2 F00 = filmfin1 FI01+FI06 (grand total).
- filmomk1: production costs (salary vs. other) by audience group. N00=N01+N02. 2010–2023.
- filmind1: revenue by channel (biograf, TV, streaming, udland) by audience group. Only goes to 2021 — most outdated of the four.
- All four share aktp or similar as a measurement selector (film count vs. money). Always filter to one metric.