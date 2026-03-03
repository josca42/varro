<fact tables>
<table>
id: pen114
description: Folkepensionister efter område, køn, alder, ydelsestype, modtagere og tid
columns: omrade, kon, alder, ydelsestype, modtag1, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2025-06-01
</table>
<table>
id: pen113
description: Førtidspensionister efter område, køn, alder, ydelsestype, modtagere og tid
columns: omrade, kon, alder, ydelsestype, modtag1, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2025-06-01
</table>
<table>
id: pen124
description: Ydelse til folkepensionister med bopæl i Danmark efter køn, alder, ydelsestype, familietype, enhed og tid
columns: kon, alder, ydelsestype, famtype, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2025-06-01
</table>
<table>
id: pen123
description: Ydelse til førtidspensionister med bopæl i Danmark efter køn, alder, ydelsestype, familietype, enhed og tid
columns: kon, alder, ydelsestype, famtype, enhed, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2025-06-01
</table>
<table>
id: pen200
description: Befolkningen (67 år og derover) efter pensions- og beskæftigelsesstatus, alder, køn, ydelsestype, løntimer pr. uge og tid
columns: pensionstatus, alder, kon, ydelsestype, ltimer, tid (time), indhold (unit Antal)
tid range: 2022-07-01 to 2025-06-01
</table>
</fact tables>

notes:
- pen114 (folkepensionister) and pen113 (førtidspensionister) are the regional count tables. Both break down by omrade (landsdele niveau 2 + kommuner niveau 3), kon, alder, ydelsestype, and modtag1 (measurement selector). Use these for "how many pensioners in region X" questions.
- pen124 (folkepension) and pen123 (førtidspension) are the benefit-amount tables — no regional breakdown, but add famtype and the enhed selector (7=gennemsnitlig ydelse kr., 71=antal modtagere). Use these for "what is the average benefit paid" questions.
- pen200 is unique: it covers the population aged 67+ by pensions- AND employment status simultaneously. Use this for questions about pensioners who continue working. Shortest time series (from 2022-07).
- All 5 tables share the same time range (monthly from 2021, except pen200 from 2022-07) and all run to 2025-06.
- modtag1 in pen114/pen113 and enhed in pen124/pen123 are measurement selectors — every row combination exists once per selector value. Always filter to a single value before aggregating.
- ydelsestype=46 (pen114/pen124) and ydelsestype=40 (pen113/pen123) are the "i alt" totals. The sub-types (47–50 for folk, 41–45/55/60 for førtid) should not be summed with their respective totals.
- For regional queries in pen113/pen114: omrade=0 is the national total, omrade=997 is people outside Denmark / unknown address (not in dim.nuts). Join via dim.nuts and always filter by niveau to avoid cross-level double-counting.
- Map: pen113 and pen114 support choropleth maps at kommune (niveau 3) and landsdele (niveau 2) level via /geo/kommuner.parquet and /geo/landsdele.parquet — merge on omrade=dim_kode, exclude omrade IN (0, 997). pen123, pen124, pen200 have no geographic breakdown.