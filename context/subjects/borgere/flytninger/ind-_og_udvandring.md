<fact tables>
<table>
id: van1kvt
description: Indvandringer (foreløbig opgørelse) efter område, køn, alder, indvandringsland, statsborgerskab og tid
columns: omrade, kon, alder, indvland, statsb, tid (time), indhold (unit Antal)
tid range: 2007-04-01 to 2025-04-01
</table>
<table>
id: van1uge
description: Indvandringer efter område, køn, alder, indvandringsland, statsborgerskab og tid
columns: omrade, kon, alder, indvland, statsb, tid (time), indhold (unit Antal)
tid range: 2021U52 to 2025U39
</table>
<table>
id: van1aar
description: Indvandringer efter område, køn, alder, indvandringsland, statsborgerskab og tid
columns: omrade, kon, alder, indvland, statsb, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: indvan
description: Indvandringer efter køn, alder, statsborgerskab, indvandringsland og tid
columns: kon, alder, statsb, indvland, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: van8k
description: Indvandringer (foreløbig opgørelse) (kvartal) efter statsborgerskab, køn, opholdstilladelse og tid
columns: statsb, koen, ophold, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: van8a
description: Indvandringer (år) efter statsborgerskab, køn, opholdstilladelse og tid
columns: statsb, koen, ophold, tid (time), indhold (unit Antal)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: van2kvt
description: Udvandringer (foreløbig opgørelse) efter område, køn, alder, udvandringsland, statsborgerskab og tid
columns: omrade, kon, alder, udvland, statsb, tid (time), indhold (unit Antal)
tid range: 2007-04-01 to 2025-04-01
</table>
<table>
id: van2aar
description: Udvandringer efter område, køn, alder, udvandringsland, statsborgerskab og tid
columns: omrade, kon, alder, udvland, statsb, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: udvan
description: Udvandringer efter køn, alder, statsborgerskab, udvandringsland og tid
columns: kon, alder, statsb, udvland, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Naming pattern: van1=indvandring, van2=udvandring. Suffix kvt=kvartal (quarterly preliminary), aar=år (annual final), uge=uge (weekly). Prefer aar tables for final figures, kvt for recent/preliminary data.
- For immigration with regional breakdown (region/kommune) + age + gender + country: van1kvt (quarterly, 2007–, preliminary) or van1aar (annual, 2007–, final). They have the same columns — van1kvt is useful for recent quarters, van1aar for completed years.
- For weekly immigration data: van1uge (2021–present, ISO week tid format e.g. '2024U15').
- For the longest historical immigration series (back to 1980) without regional detail: indvan. statsb here is only DANSK/UDLAND — coarse.
- For immigration by permit type (opholdstilladelse — EU/EØS, study, work, family, asylum): van8k (quarterly preliminary, 2016–) or van8a (annual final, 1997–). These are the only tables with ophold column.
- For emigration: exact mirror — van2kvt/van2aar (regional, from 2007) and udvan (no region, from 1980).
- omrade=0 is the national total in all regional tables, not in dim.nuts. For regional joins always filter dim.nuts by niveau (1=regioner, 3=kommuner).
- None of these tables have total/aggregate rows in kon or alder — those columns only contain individual values. Aggregate in SQL.
- indvan/udvan use kon=M/K; all van1/van2/van8 tables use kon or koen=1/2.
- Map: van1kvt, van1uge, van1aar (immigration) and van2kvt, van2aar (emigration) support choropleth maps at kommune (niveau 3) or region (niveau 1) level via /geo/kommuner.parquet or /geo/regioner.parquet — merge on omrade=dim_kode, exclude omrade=0. indvan, udvan, van8k, van8a have no geographic column.