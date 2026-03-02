<fact tables>
<table>
id: camp1
description: Overnatninger på campingpladser efter område, gæstens nationalitet, enhed, periode og tid
columns: omrade, nation1, overnat1, periode, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-01-01
</table>
<table>
id: camp2
description: Campingpladser efter område, kapacitet og tid
columns: omrade, kapacitet, tid (time), indhold (unit -)
tid range: 1992-03-01 to 2025-08-01
</table>
<table>
id: camp3
description: Campingpladser efter område, kapacitet og tid
columns: omrade, kapacitet, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- camp1 = overnight stays (overnatninger) by region, guest nationality, and month — the main table for demand/visitor questions. tid is annual, but the periode column (1–12) provides monthly breakdown within each year. periode=1 is the annual total; periode=3–12 are individual months.
- camp2 = monthly capacity stats (number of sites, camping units, utilization %). Use for "how many pitches exist" or "what is the utilization rate in July" type questions.
- camp3 = annual capacity stats with seasonal min/max values (max/min number of sites and units within the year). Use when you need the annual high/low range for capacity.
- All three tables share the same omrade dimension: 5 regioner (niveau 1, kode 81–85) plus omrade=0 for the national total. No sub-regional breakdown (kommune level) is available.
- All three tables have a kapacitet or overnat1/periode measurement selector — always filter to one value to avoid silently doubling counts. This is the most common pitfall across all tables in this subject.
- Map: all three tables support choropleth maps at region level via context/geo/regioner.parquet — merge on omrade=dim_kode, exclude omrade=0.