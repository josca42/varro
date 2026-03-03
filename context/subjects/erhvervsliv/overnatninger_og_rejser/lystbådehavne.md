<fact tables>
<table>
id: lyst1
description: Overnatninger i lystbådehavne efter område, gæstens nationalitet, periode og tid
columns: omrade, nation1, periode, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-01-01
</table>
<table>
id: lyst2
description: Overnatninger i lystbådehavne efter farvand, gæstens nationalitet, periode og tid
columns: farvand, nation1, periode, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-01-01
</table>
<table>
id: lyst10
description: Overnatninger i lystbådehavne efter område, gæstens nationalitet, periode, overnatningsform og tid
columns: omrade, nation1, periode, overnatf, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: lyst11
description: Overnatninger i lystbådehavne efter farvand, gæstens nationalitet, periode, overnatningsform og tid
columns: farvand, nation1, periode, overnatf, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: lyst12
description: Lystbådehavne efter størrelse, kapacitet og tid
columns: storrelse, kapacitet, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: lyst13
description: Lystbådehavne efter område, kapacitet og tid
columns: omrade, kapacitet, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All overnight-stay tables (lyst1, lyst2, lyst10, lyst11) share a critical periode overcounting trap: values 1=Hele året, 2=År til dato, 5-9=individual months (May–Sep). Always filter to exactly one periode — never aggregate across periode values.
- All overnight-stay tables also have nation1='TOT' as the grand total across nationalities. Filter to TOT unless you want a specific nationality breakdown.
- Geography split: lyst1/lyst10 break by administrative region (regioner/landsdele via dim.nuts), lyst2/lyst11 break by farvand (sea area, 12 coastal zones). Use lyst1/lyst10 for administrative questions, lyst2/lyst11 for coastal/maritime geography.
- Overnatningsform split: lyst1 and lyst2 give a combined total of overnight stays. lyst10 and lyst11 add the overnatf column separating personovernatninger (210) from gæstebådsovernatninger (215) — two different metrics, never sum them.
- For marina capacity/infrastructure (not overnight stays): use lyst12 (by marina size) or lyst13 (by region/landsdel). Both use kapacitet as a measure selector — always filter to one kapacitet value. lyst13 splits guest boat nights into paid vs. free harbour scheme; lyst12 does not.
- lyst12 is the only table with marina size breakdown (storrelse). lyst13 is the only capacity table with regional geography.
- tid is annual for all tables (Jan 1 of each year). lyst1/lyst2 run to 2025; lyst10–lyst13 only to 2024.
- Map: lyst1 and lyst10 support choropleth at regioner (niveau 1) or landsdele (niveau 2) via /geo/regioner.parquet / /geo/landsdele.parquet. lyst13 supports landsdele (niveau 2) only. Merge on omrade=dim_kode, exclude omrade=0. lyst2/lyst11 (farvand) and lyst12 (storrelse) have no geo join.