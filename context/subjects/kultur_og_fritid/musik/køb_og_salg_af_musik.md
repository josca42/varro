<fact tables>
<table>
id: musik1
description: Salg af indspillet musik efter nationalitet, distributionsform og tid
columns: nation2, distrib, tid (time), indhold (unit Mio. kr.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: musik2
description: Køb af rettigheder til afspilning af musik efter branche (DB07), område og tid
columns: branche07, omrade, tid (time), indhold (unit Kr.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: musik3
description: Indtægter ved salg af musik efter rettighedsejertype, område og tid
columns: rettighed, omrade, tid (time), indhold (unit Kr.)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: musik4
description: Autorers indtægter fra musikrettigheder efter køn, alder, område og tid
columns: kon, alder, omrade, tid (time), indhold (unit Kr.)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: musik5
description: Registrerede musikværker efter musikværker og tid
columns: musvaerk, tid (time), indhold (unit 1.000)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: musik6
description: Autorer (komponister og sangskrivere) med nye registrerede musikværker efter køn, alder og tid
columns: kon, alder, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For recorded music sales by format (physical/streaming/downloads): use musik1. Only annual data, in Mio. kr. Watch out for nation2=TOT which aggregates danish + foreign — filter to specific values or TOT, not both.
- For rights purchase costs by industry: use musik2. Covers 2008–2024 with regional (5 regioner) and industry (DB07) breakdown. omrade=997 is a large non-regional aggregate (especially for foreign income via branche07='Y') — not a sum of the regions.
- For revenue from music rights sales by rights-holder type: use musik3 (2012–2024). Only Autor (6) and Forlag (7) have regional breakdown; Søsterselskab (8), Arving (9), Uoplyst (10) are only in omrade=99 (non-regional). Sum all omrade to get national totals.
- For income of individual authors (composers/lyricists) by gender and age: use musik4 (2012–2024). No total rows for kon or alder — safe to sum, but remember omrade=99 (non-regional) must be included in national totals.
- For registered music works (catalogue size vs. new registrations): use musik5 (2000–2024). Two independent measures: 200=cumulative total, 205=new per year. Values are in thousands.
- For authors with new works by gender and age: use musik6 (2021–2024 only, very short series). Both kon and alder include total rows — filter carefully to avoid double-counting.
- musik2 and musik3 cover complementary sides of the same market: musik2 = who buys rights (licensees, by industry), musik3 = who receives money (rights-holders, by type).
- musik4 and musik6 both cover authors but measure different things: musik4 = income in Kr. (2012–), musik6 = number of active authors with new registered works (2021– only).
- Map: musik2, musik3, musik4 have regional breakdown (5 regioner) via omrade=dim_kode → /geo/regioner.parquet. Filter omrade IN (81,82,83,84,85) before merging.