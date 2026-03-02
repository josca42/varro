<fact tables>
<table>
id: hand01
description: Handicapydelser efter område, ydelsestype og tid
columns: omrade, ydelsestype, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-10-01
</table>
<table>
id: hand02a
description: Modtagere af handicapydelser efter ydelsestype, alder, køn og tid
columns: ydelsestype, alder, kon, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-10-01
</table>
<table>
id: hand03a
description: Handicapydelser efter ydelsestype, målgruppe og tid
columns: ydelsestype, mlgrp, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-10-01
</table>
<table>
id: hand05
description: Handicapydelser efter område, ydelsestype og tid
columns: omrade, ydelsestype, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: hand06
description: Handicapydelser (Antal pr. 1.000 indbyggere) efter område, ydelsestype og tid
columns: omrade, ydelsestype, tid (time), indhold (unit Pr. 1.000 indb.)
tid range: 2015-01-01 to 2024-10-01
</table>
<table>
id: hand07
description: Modtagere af handicapydelser efter område, ydelsestype og tid
columns: omrade, ydelsestype, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-10-01
</table>
<table>
id: handbu01
description: Handicapindsatser til børn og unge mellem 0-17 år efter kommune, indsats, køn og tid
columns: kommunedk, indsatser, kon, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: handbu02
description: Handicapindsatser til børn og unge mellem 0-17 år efter kommune, indsats, alder og tid
columns: kommunedk, indsatser, alder, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: handbu03
description: Handicapindsatser til børn og unge mellem 0-17 år efter landsdel, indsats og tid
columns: landsdel, indsatser, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: handbu04
description: Handicapindsatser til børn og unge mellem 0-17 år efter indsats, alder, køn og tid
columns: indsatser, alder, kon, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: handbil1
description: Bevilget støtte til handicapbil efter område, enhed og tid
columns: omrade, tal, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: handbil2
description: Afslag af støtte til handicapbil efter område, enhed og tid
columns: omrade, tal, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Adult services (hand-prefix): hand01=services count (decimal averages, by kommune/ydelsestype), hand07=recipient headcount (integers, by kommune/ydelsestype), hand02a=recipients by age/gender (national), hand03a=recipients by disability type/målgruppe (national), hand06=rate per 1000 inhabitants by kommune (never sum across geographies). hand05 is older and superseded by hand01.
- When you want "how many people receive a service": use hand07 (by region) or hand02a (by age/gender). When you want "how many service-days were delivered": use hand01.
- hand06 is the only table with normalized rates — use it for municipality comparisons. For absolute figures use hand01/hand07.
- Children's services (handbu-prefix): handbu01=by kommune/gender, handbu02=by kommune/age, handbu03=by landsdel/indsatstype, handbu04=by indsatstype/age/gender. Coverage is 2022–2024 only. All handbu tables have two indsatser aggregate codes: 100=total interventions, 110=unique children — never sum these two together.
- Handicapbil (vehicle support): handbil1=approved applications, handbil2=rejected applications. Both use a tal measurement selector (5=cases, 6=avg processing time in weeks; handbil1 also has 7=total granted kr.). Always filter to one tal value — the three measures share the indhold column but have completely different units.
- All tables with omrade/kommunedk/landsdel include a code=0 national total (not in dim.nuts) except hand01/hand05/hand06/hand07 which only have kommuner (niveau=3, no code=0). Use code=0 rows for national figures in the handbu and handbil tables.
- ydelsestype codes are the same set across all adult tables (hand01, hand02a, hand03a, hand05, hand06, hand07) — 21 types in the current tables, 17 in hand05.
- Map: kommune-level choropleth available for hand01, hand05, hand06, hand07, handbu01, handbu02, handbil1, handbil2 via context/geo/kommuner.parquet (merge on omrade/kommunedk=dim_kode). handbu03 supports landsdel-level maps via context/geo/landsdele.parquet (merge on landsdel=dim_kode).
