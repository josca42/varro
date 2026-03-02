<fact tables>
<table>
id: laby49
description: Andel af befolkningen med adgang til offentlig transport efter kommunegruppe, serviceniveau og tid
columns: komgrp, sdgservice, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: pkm1
description: Persontransport efter transportmiddel og tid
columns: transmid, tid (time), indhold (unit Mio. personkm)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: bane21
description: Jernbanetransport af passagerer efter enhed, transporttype og tid
columns: enhed, transport, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: bane22
description: International jernbanetransport af passagerer til og fra Danmark efter land og tid
columns: land, tid (time), indhold (unit 1.000 personer)
tid range: 2002-01-01 to 2024-01-01
</table>
<table>
id: bane25
description: Jernbanetransport af passagerer efter enhed, transporttype og tid
columns: enhed, transport, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2025-04-01
</table>
<table>
id: bane32
description: Togtrafik på en hverdag efter banestrækning, enhed og tid
columns: banes, enhed, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2024-01-01
</table>
<table>
id: skib31
description: Indenrigs færgetransport efter færgerute, enhed og tid
columns: faerge, enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: skib32
description: Udenrigs færgetransport efter færgerute, enhed og tid
columns: faerge, enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: skib33
description: Indenrigs færgetransport efter færgerute, enhed og tid
columns: faerge, enhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2025-06-01
</table>
<table>
id: skib34
description: Udenrigs færgetransport efter færgerute, enhed og tid
columns: faerge, enhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2025-06-01
</table>
<table>
id: skib35
description: Krydstogtskibe på danske havne efter havn, enhed og tid
columns: havn, maengde4, tid (time), indhold (unit -)
tid range: 2002-01-01 to 2024-01-01
</table>
<table>
id: flyv31
description: Passagerer på større offentlige, betjente danske lufthavne efter lufthavn, passagerkategori og tid
columns: lufthavn, passager, tid (time), indhold (unit 1.000 stk.)
tid range: 2003-01-01 to 2024-01-01
</table>
<table>
id: flyv32
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne efter lufthavn, transporttype, flyvning og tid
columns: lufthavn, transport, flyvning, tid (time), indhold (unit 1.000 stk.)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: flyv33
description: Passagertransport med rute- og charterfly mellem danske lufthavne efter påstigning, afstigning og tid
columns: pastig1, afstig1, tid (time), indhold (unit 1.000 personer)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: flyv34
description: Flyrejser med rute- og charterfly mellem større, offentlige, betjente lufthavne og udlandet efter lufthavn, destinationsland, retning og tid
columns: lufthavn, desti, ret, tid (time), indhold (unit 1.000 stk.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: flyv35
description: Passagerer på udenrigsflyvninger efter rejselængde, flyvning, enhed og tid
columns: rejse, flyvning, maengde4, tid (time), indhold (unit 1.000 personer)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: flyv91
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne efter lufthavn, transporttype, flyvning og tid
columns: lufthavn, transport, flyvning, tid (time), indhold (unit 1.000 personer)
tid range: 2001-01-01 to 2025-04-01
</table>
<table>
id: flyv92
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne efter transporttype, flyvning og tid
columns: transport, flyvning, tid (time), indhold (unit 1.000 personer)
tid range: 2001-01-01 to 2025-06-01
</table>
<table>
id: flyv93
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne (sæsonkorrigeret) efter transporttype, flyvning og tid
columns: transport, flyvning, tid (time), indhold (unit 1.000 personer)
tid range: 2001-01-01 to 2025-06-01
</table>
<table>
id: flyv36
description: Persontransportarbejde med fly efter transporttype og tid
columns: transport, tid (time), indhold (unit Mio. personkm)
tid range: 1990-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables with an enhed or maengde4 column use it as a measurement selector (multiple incompatible units in one table). Always filter to exactly one value — failing to do so silently multiples counts.
- Tables with total-rows embedded in dimension columns (faerge=10002, lufthavn=10010, transport=0, etc.) require filtering to avoid double-counting when summing across categories.

**Rail (bane):**
- bane21: annual rail passengers/personkm by transport type, 1990–2024. bane25: same codes but quarterly, 2006–2025 Q1. Prefer bane25 for current data, bane21 for long history.
- transport column is hierarchical in both: 10010=total, 10020=BaneDanmarks net (includes S-tog, landsdækkende, international), plus Metro/Andre baner/Letbane as separate lines.
- bane22: international rail passengers by country, 2002–2024 annual. 28 European countries at niveau 4. Use IA code directly for the total.
- bane32: train frequency by track segment (persontog/godstog, daily/peak hour). Useful for infrastructure load, not passenger counts. Segment codes changed in 2018.

**Ferry (skib):**
- skib31/skib32: domestic/international ferry annual data 1990–2024. skib33/skib34: same routes but monthly 2000–2025. Prefer skib33/34 for current or monthly analysis; use skib31/32 for long historical annual series.
- enhed has 20 values covering passengers, vehicles by type, and freight tonnage — always filter to one.
- skib35: cruise ships only, by port, annual 2002–2024. Separate from regular ferry traffic.

**Aviation (flyv):**
- For current departing passengers (monthly, all airports combined): flyv92. For seasonal adjustment: flyv93.
- For current departing passengers by airport (quarterly): flyv91 (5 airports, 2001–2025 Q1).
- For departing passengers with full airport detail (11 airports) or long history: flyv32 (annual, 1990–2024).
- For total airport throughput (arrivals + departures) by airport and passenger category: flyv31 (annual, 2003–2024).
- For international routes by destination country: flyv34. For distance bands: flyv35 (also has personkm). For transport work (Mio. personkm) long series: flyv36 (annual 1990–2024).
- flyv33: origin-destination matrix for domestic flights between Danish airports — use for route-level flows, not totals.

**Modal comparison:**
- pkm1: the only table combining all transport modes (road, rail, ship, air) in Mio. personkm, annual 1980–2024. Use for modal split analysis.
- laby49: public transport access by municipality group, only 2 snapshots (2019 and 2023).