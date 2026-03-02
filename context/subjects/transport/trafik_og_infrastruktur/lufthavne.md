<fact tables>
<table>
id: flyv3
description: Aktivitet på offentlige betjente lufthavne efter lufthavn, enhed og tid
columns: lufthavn, maengde4, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: flyv21
description: Flyoperationer på større, betjente danske lufthavne efter lufthavn, flyvning, transporttype og tid
columns: lufthavn, flyvning, transport, tid (time), indhold (unit 1.000 stk.)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: flyv1
description: Offentlige betjente lufthavne efter lufthavn, banelængde og tid
columns: lufthavn, banel, tid (time), indhold (unit -)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: flyv2
description: Faste investeringer i lufthavne efter investeringstype, enhed og tid
columns: invest, maengde4, tid (time), indhold (unit Mio. kr.)
tid range: 1992-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For traffic questions (passengers, cargo, operations): use flyv3 (broader — includes Øvrige lufthavne, 3 metrics via maengde4) or flyv21 (narrower airport coverage but richer flight-type breakdown: scheduled/charter/other × national/international).
- flyv1 is infrastructure data only (runway counts, areas in 1000 sqm) — not traffic. Use it for questions about airport capacity or physical size.
- flyv2 is investment data in Mio. kr. with no airport breakdown — use for total Danish airport investment spending.
- All traffic/infrastructure tables share the same lufthavn codes (10010–10070). 10010=LUFTHAVNE IALT is always an aggregate; exclude it when summing across individual airports.
- Every table has a measurement-selector column that causes silent overcounting if not filtered: flyv3 has maengde4 (3 measure types), flyv21 has flyvning×transport (12 combinations per airport/year), flyv1 has banel (11 different metrics), flyv2 has invest×maengde4 (up to 12 combinations per year). Always filter these before aggregating.
- Time coverage: flyv3/flyv21 from 1990, flyv1 from 1997, flyv2 from 1992 (ends 2023).