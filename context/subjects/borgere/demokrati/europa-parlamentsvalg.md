<fact tables>
<table>
id: evkom1
description: Europa-Parlamentsvalg efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: evpandel
description: Partiernes stemmeandel (Europa-Parlamentsvalg) efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Pct.)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: evbpct
description: Europa-Parlamentsvalg efter valgresultat og tid
columns: valres, tid (time), indhold (unit Antal)
tid range: 1979-01-01 to 2024-01-01
</table>
<table>
id: evpct
description: Europa-Parlamentsvalg efter valgresultat og tid
columns: valres, tid (time), indhold (unit Pct.)
tid range: 1979-01-01 to 2024-01-01
</table>
<table>
id: ev24tot
description: Europa-Parlamentsvalget 2024 efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: ev24tota
description: Europa-Parlamentsvalget 2024 efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: ligedi4
description: Ligestillingsindikator for opstillede og valgte kandidater til Europa-Parlamentsvalg efter kandidater, indikator og tid
columns: kandidat, indikator, tid (time), indhold (unit -)
tid range: 1994-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For voter turnout / stemmeprocent over time (1979–2024): use evpct (STEMPCT). For raw vote and voter counts at national level: use evbpct. Both tables cover all EP elections since 1979.
- For party vote shares by municipality (2009–2024): use evpandel (Pct.) or evkom1 (Antal). Both join dim.nuts at niveau 3 (kommuner). evpandel has omrade='0' for national totals; evkom1 does not.
- For 2024 election with sub-municipal detail: use ev24tot (valgkredse, ~106 areas) or ev24tota (individual polling stations, 1404 areas). These use electoral geography, not NUTS — no dim table.
- For gender balance among candidates/elected MEPs (1994–2024): use ligedi4.
- All tables with party-level valres rows also include aggregate rows (GYLD_IALT, VAELG, etc.). Always filter valres to either aggregate rows OR party rows — never mix them in a sum.
- Party codes are numeric IDs (e.g. 5891=Socialdemokratiet, 5903=Venstre). Use ColumnValues("evkom1", "valres") to get the full id→name mapping.
- Map: evkom1 and evpandel support kommune-level choropleth via context/geo/kommuner.parquet (omrade=dim_kode). ev24tot supports storkredse (omrade 10–19, subtract 9) and valgkredse (omrade 20–111, subtract 19) via context/geo/storkredse.parquet and context/geo/valgkredse.parquet.