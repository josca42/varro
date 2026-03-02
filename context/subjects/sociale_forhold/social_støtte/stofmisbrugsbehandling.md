<fact tables>
<table>
id: smdbv001
description: Stofmisbrugsbehandling efter område, aktivitet i året og tid
columns: omrade, akti, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: smdbv002
description: Stofmisbrugsbehandling efter område, nøgletal og tid
columns: omrade, aktp, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: smdbv003
description: Stofmisbrugsbehandling efter nøgletal, køn, alder og tid
columns: aktp, kon, alder1, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: smdbv004
description: Stofmisbrugsbehandling efter område, behandlingsgaranti og tid
columns: omrade, ventetidgaranti, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: smdbv005
description: Stofmisbrugsbehandling efter myndighedskommune, afslutningsstatus og tid
columns: myndighedskom, afslutstatus, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All five tables cover 2015–2024 (annual). No sub-annual granularity available.
- For treatment activity by geography: use smdbv001 (ANMOD/IVAERK/BEHSLUT by region/kommune).
- For key metrics (kontaktforløb, behandlingsforløb, personer i behandling) by geography: use smdbv002.
- For key metrics by gender and age (no geography): use smdbv003. Age splits are coarse: under 18 vs 18+.
- For treatment guarantee compliance (14-day guarantee): use smdbv004. Has counts and percentages in same column (ventetidgaranti) — always filter to one group.
- For treatment outcomes (stoffri / reduceret forbrug / andet) by responsible municipality: use smdbv005. Also mixes counts and pct in the same column (afslutstatus).
- Geography pattern shared by smdbv001/002/004/005: omrade or myndighedskom joins dim.nuts (niveau 1=5 regioner, niveau 3=98 kommuner). Code '0' = national total, not in dim.nuts — query directly. Never mix niveau 1 and 3 in the same aggregation.
- smdbv004 and smdbv005 have mixed-measure columns (counts + percentages). Always filter to either counts OR percentages per query — summing across all values is meaningless and will inflate results.
- Map: smdbv001, smdbv002, smdbv004 (omrade) and smdbv005 (myndighedskom) support choropleth maps via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1).