<fact tables>
<table>
id: ferieh1
description: Udlejning af feriehuse på månedsbasis efter gæstens nationalitet, enhed, periode og tid
columns: nation1, tal, periode, tid (time), indhold (unit Antal)
tid range: 2004-01-01 to 2025-01-01
</table>
<table>
id: ferieh2
description: Fremtidige bookede hus-uger, feriehuse efter gæstens nationalitet, fremtidig år, fremtidig måned og tid
columns: nation1, fremar, fremmd, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2025-08-01
</table>
<table>
id: ferieh3
description: Udlejning af feriehuse efter område, gæstens nationalitet, enhed og tid
columns: omrade, nation1, tal, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: ferieh4
description: Antal udlejede hus-uger i feriehuse efter enhed, periode og tid
columns: enhed, periode, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ferieh5
description: Feriehuse til udlejning efter kapacitet og tid
columns: kapmedie, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: ferieh6
description: Udlejning af feriehuse på månedsbasis efter område, gæstens nationalitet, enhed, periode og tid
columns: omrade, nation1, tal, periode, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- For national monthly totals by nationality (overnatninger, hus-uger, kontrakter): ferieh1 (2004–2025). No regional breakdown.
- For regional annual data (region/landsdel level, long history): ferieh3 (1992–2024). Only 3 measures (no Disponible husuger).
- For regional monthly data down to kommune level: ferieh6 (2017–2025). Most comprehensive table — has area × nationality × measure × month. Use this for regional questions from 2017 onward.
- For week-by-week granularity: ferieh4 (2008–2024) breaks data into U01–U53 by nationality (enhed column) rather than a nation1 dimension.
- For advance booking forecasts: ferieh2 (2005–2025) is uniquely forward-looking — it tracks how booked house-weeks for a future month accumulate over time. The only table for "how many weeks are booked for summer 2025?"
- For rental capacity (number of houses available): ferieh5 (2012–2024). 13 rows total, one per year — trivially simple.
- Common pitfall in ferieh1 and ferieh6: periode=1 and periode=2 are overloaded codes that each map to TWO different rows per combination (annual total + monthly value). Filtering to periode=1 gives 14 rows instead of 12 per group. Use periode >= 3 for unambiguous months, or handle periods 1–2 carefully.
- All tables with a tal or enhed column treat it as a measurement selector — always filter to one value to avoid inflated counts.
- Map: ferieh6 supports kommune/landsdel/region choropleths (/geo/kommuner.parquet, landsdele.parquet, regioner.parquet); ferieh3 supports region/landsdel only. Merge on omrade=dim_kode.