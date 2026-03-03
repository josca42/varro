<fact tables>
<table>
id: hotel1
description: Overnatninger på hoteller og feriecentre efter område, gæstens nationalitet, enhed, periode og tid
columns: omrade, nation1, tal, periode, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-01-01
</table>
<table>
id: hotel2
description: Overnatninger på hoteller og feriecentre efter område, gæstens nationalitet, type, enhed, periode og tid
columns: omrade, nation1, type, tal, periode, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-01-01
</table>
<table>
id: hotel4
description: Hoteller og feriecentre efter område, kapacitet og tid
columns: omrade, kapacitet, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: hotel3
description: Hoteller og feriecentre efter område, kapacitet og tid
columns: omrade, kapacitet, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2025-08-01
</table>
<table>
id: hotel5
description: Hoteller og feriecentre efter område, kapacitet, type og tid
columns: omrade, kapacitet, type, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2025-08-01
</table>
<table>
id: hotel6
description: Hoteller og feriecentre efter område, kapacitet, type og tid
columns: omrade, kapacitet, type, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: hotel7
description: Overnatninger på hoteller og feriecentre efter område, formål med rejse, periode og tid
columns: omrade, seg, periode, tid (time), indhold (unit Antal)
tid range: 2004-01-01 to 2025-01-01
</table>
<table>
id: hotel8
description: Overnatninger på hoteller og feriecentre efter område, formål med rejse, type, periode og tid
columns: omrade, seg, type, periode, tid (time), indhold (unit Antal)
tid range: 2004-01-01 to 2025-01-01
</table>
<table>
id: hotel31
description: Hoteller og feriecentre efter størrelse, kapacitet og tid
columns: storrelse, kapacitet, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2025-08-01
</table>
<table>
id: turist3
description: Hoteller og feriecentre efter certificering, kapacitet og tid
columns: cert, kapacitet, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2024-12-01
</table>
<table>
id: vandrer
description: Overnatninger på vandrerhjem efter område, gæstens nationalitet, periode og tid
columns: omrade, nation1, periode, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- Overnights by guest nationality: use hotel1 (regioner + landsdele, from 1992) or hotel2 (regioner only, adds hotel vs. feriecenter type split). Both have the same nation1 dimension with 54 country codes.
- Overnights by travel purpose (business vs. leisure): use hotel7 (regioner + landsdele, from 2004) or hotel8 (regioner only, adds hotel vs. feriecenter type). Data starts 2004 for both.
- Youth hostel overnights: use vandrer (regioner only, from 1998). No tal selector — always overnights.
- Capacity (count of hotels/rooms/beds + utilization %): two pairs of tables. Monthly data: hotel3 (regioner + landsdele, no type) and hotel5 (regioner only, with type). Annual data with seasonal max/min: hotel4 (regioner + landsdele, no type) and hotel6 (regioner only, with type).
- Hotel size distribution: use hotel31 (national only, monthly, hotels with ≥40 beds). Includes overnights and sold rooms per size band — unique in this subject.
- Green Key certification: use turist3 (national only, 2019–2024). The only sustainability table in this subject.
- CRITICAL — periode encoding collision: all overnatning tables (hotel1, hotel2, hotel7, hotel8, vandrer) use a `periode` column where codes 1 and 2 each encode TWO rows per dimension combination: 1 = "Hele året" (annual total) AND "Januar"; 2 = "År til dato" (YTD) AND "Februar". Never SUM across all periode values. For annual totals, filter periode=1 and take MAX(indhold) per group. Months 3–12 are unambiguous.
- CRITICAL — kapacitet is a measurement selector: all capacity tables (hotel3–hotel6, hotel31, turist3) mix counts and percentages in the same column. Always filter to exactly one kapacitet value.
- omrade code 0 = Hele landet is present in all regional tables but is NOT in dim.nuts — filter it out or handle separately when joining.
- Table naming pattern: odd numbers (hotel3, hotel5, hotel7) have finer geographic breakdown (landsdele); even numbers (hotel4, hotel6, hotel8) trade geographic granularity for an additional type dimension (hoteller vs. feriecentre).
- Map: hotel1, hotel3, hotel4, hotel7 support choropleth at both region and landsdel level (/geo/regioner.parquet / /geo/landsdele.parquet). hotel2, hotel5, hotel6, hotel8, vandrer support regioner only. hotel31 and turist3 are national-only — no map possible.