<fact tables>
<table>
id: livmus01
description: Antallet af publikummer til koncerter efter koncertarrangør, koncertstørrelse og tid
columns: koncertarrangor, koncertstorrelse, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
<table>
id: livmus02
description: Antal koncerter efter koncertarrangør, koncertstørrelse og tid
columns: koncertarrangor, koncertstorrelse, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
<table>
id: livmus03
description: Antal koncertarrangører efter arrangørtype, sektor, branche (DB07) og tid
columns: arrangeor, sektor, branchekult, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
<table>
id: livmus04
description: Antal koncertarrangører efter arrangørtype, sektor, landsdel og tid
columns: arrangeor, sektor, landsdel, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
<table>
id: kv2mk5
description: Forbrug af koncerter efter hovedgenre, hyppighed, køn, alder og tid
columns: hovedgenre, hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk6
description: Forbrug af koncerter efter spillestedets placering, køn, alder og tid
columns: spilplac, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk7
description: Forbrug af koncerter efter ledsager, køn, alder og tid
columns: ledsag, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk8
description: Barrierer for forbrug af koncerter og musikfestivaler efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- livmus01 = audience numbers (publikummer), livmus02 = concert counts. Same dimensions (organizer type + concert size), same time range (2018–2023). Use livmus01 for "how many people attended", livmus02 for "how many concerts were held".
- livmus03 = organizer counts by industry sector and branch (national, no geography). livmus04 = organizer counts by region (landsdel). For regional breakdown use livmus04; for sector/industry breakdown use livmus03.
- kv2mk5–kv2mk8 are all survey-based percentage tables from 2024 only, covering the consuming public (not the supply side). They answer: how often (kv2mk5), where (kv2mk6), with whom (kv2mk7), and why not (kv2mk8).
- In livmus01/02: koncertstorrelse='0' is the "I alt" total — filter to it for organizer-level totals, or filter it OUT to break down by venue size.
- In livmus03/04: sektor='TOT' is the total across sectors. In livmus03 also branchekult='TOT'. Always filter totals to avoid double-counting.
- kv2mk6/kv2mk7/kv2mk8 all have NON-mutually-exclusive category columns. Do not sum across spilplac, ledsag, or aarsag. In kv2mk5, frequency (hyp) IS mutually exclusive within a genre, but the two genres are not.
- All kv2mk tables have kon='10' (total) and alder='TOT' as aggregate rows — filter these when breaking down by gender or age.
- Map: livmus04 supports choropleth at landsdel level (niveau 2, 11 regions) via /geo/landsdele.parquet. All other tables are national-only.