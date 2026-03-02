<fact tables>
<table>
id: hjemsyg
description: Modtagere af hjemmesygepleje (eget hjem) efter område, alder, køn og tid
columns: omrade, alder1, koen, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: hjemsyg2
description: Leveret hjemmesygepleje (eget hjem) efter område, alder, køn, dage og tid
columns: omrade, alder1, koen, dage, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For "how many citizens receive hjemmesygepleje": use hjemsyg (recipient count).
- For "how many days of care are delivered" or "average days per recipient": use hjemsyg2. Its dage column selects between total days (252) and average days per citizen (353) — always filter to one.
- Both tables cover 2016–2024, municipality level only (98 kommuner, dim.nuts niveau 3). Neither has regional or national aggregates in the omrade column.
- Both tables require filtering koen and alder1 to avoid overcounting: koen=100 (alle) and alder1=50 (alle aldre) for totals, or pick specific categories.
- Map: both tables support choropleth at kommune level — context/geo/kommuner.parquet, merge on omrade=dim_kode. Exclude omrade=0.