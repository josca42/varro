<fact tables>
<table>
id: skov11
description: Skovarealet efter område, bevoksning og tid
columns: omrade, bevoksning, tid (time), indhold (unit ha)
tid range: 1990-01-01 to 2023-01-01
</table>
<table>
id: skov55a
description: Hugsten i skove og plantager i Danmark efter område, træsort og tid
columns: omrade, traesort, tid (time), indhold (unit 1.000 m3)
tid range: 1950-01-01 to 1989-01-01
</table>
<table>
id: skov55
description: Hugsten i skove og plantager i Danmark efter område, træsort og tid
columns: omrade, traesort, tid (time), indhold (unit 1.000 m3)
tid range: 2006-01-01 to 2023-01-01
</table>
<table>
id: skov6
description: Hugsten i skove og plantager i Danmark efter område, træsort, areal og tid
columns: omrade, traesort, areal1, tid (time), indhold (unit 1.000 m3)
tid range: 1990-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For forest area (skovareal in ha): use skov11 (1990–2023). It has regional breakdown (5 regioner or 5 landsdele + combined Sjælland area) and detailed bevoksning (løvtræ/nåletræ species). The only table with both regional and species detail.
- For timber harvest (hugst in 1000 m3): three tables with different time coverage and geographic detail:
  - skov55 (2006–2023): regional breakdown (5 landsdele + 5 regioner), detailed traesort including energitræ
  - skov55a (1950–1989): Jylland/Øerne only, simpler traesort (no energitræ codes), not annual before 1961
  - skov6 (1990–2023): Jylland/Øerne only, continuous annual data, adds farm-size dimension (areal1)
- For a long national hugst series: combine skov55a (1950–1989) + skov6 (1990–2023) using omrade=000. Or skov55a + skov55 for 1950–1989 + 2006–2023 with the note that 1990–2005 are only in skov6.
- For farm-size breakdown of harvesting: skov6 is the only option. Use areal1=4 for total, and pick either [1,2,3] or [5,6,7] for a size breakdown — these are two different grouping schemes, do not sum all seven codes.
- Both bevoksning (skov11) and traesort (skov55/skov55a/skov6) are deeply nested hierarchies with aggregate and detail codes coexisting in the table. Always filter to a single level — use the top-level total (200 / 00010) or one consistent breakdown. Summing all codes massively overcounts.
- skov11 and skov55 share the same omrade coding: 0=Hele landet plus dim.nuts region/landsdel codes. Codes 0 and 15 (combined Copenhagen/Sjælland area) are not in dim.nuts. After 2015, code 15 disappears and only regions 81–85 cover the full country.
- Map: skov11 and skov55 support choropleth maps at landsdel (niveau 2) and region (niveau 1) level via /geo/landsdele.parquet and /geo/regioner.parquet. skov55a and skov6 use only Jylland/Øerne codes — no geo join possible.