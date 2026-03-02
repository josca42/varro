<fact tables>
<table>
id: serv2501
description: It-servicevirksomhed efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2503
description: Reklamevirksomhed efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2512
description: Omsætning for reklamevirksomhed efter medier og tid
columns: medier, tid (time), indhold (unit Pct.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2502
description: Vikarbureauer og anden personaleformidling efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2511
description: Solgte vikartimer efter branche og tid
columns: erhverv, tid (time), indhold (unit Timer)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2504
description: Juridisk bistand efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2509
description: Rådgivende ingeniørvirksomhed efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2508
description: Teknisk afprøvning og analyse efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2507
description: Arkitektvirksomhed efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv2510
description: Markedsanalyse og offentlig meningsmåling efter serviceydelser og tid
columns: servyd, tid (time), indhold (unit 1.000 kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: serv1406
description: Bogføring- og revisionsvirksomhed efter serviceydelser, omsætning og eksport og tid
columns: servyd, omseks, tid (time), indhold (unit 1.000 kr.)
tid range: 2012-01-01 to 2022-01-01
</table>
<table>
id: serv1407
description: Anden virksomhedsrådgivning efter serviceydelser, omsætning og eksport og tid
columns: servyd, omseks, tid (time), indhold (unit 1.000 kr.)
tid range: 2012-01-01 to 2022-01-01
</table>
</fact tables>
notes:
- All tables are single-year snapshots (2023) except serv1406 (bogføring/revision, 2012–2022) and serv1407 (virksomhedsrådgivning, 2012–2022). For time-series analysis, only those two are available.
- All tables measure revenue (1.000 kr.) except serv2511 (sold temp hours, timer) and serv2512 (media shares, Pct.).
- All servyd columns include a total aggregate row (TOT or TOTSERV). Always exclude it when aggregating across service types to avoid double-counting. The exact total code varies: most tables use TOT, but serv2504/serv1406/serv1407 use TOTSERV.
- serv1406 and serv1407 have an extra omseks dimension (TOTOMS=total turnover, EKST=export). EKST is a subset of TOTOMS — never add them. Always filter omseks explicitly in queries.
- For advertising: serv2503 = revenue by type of advertising service; serv2512 = percentage share by media channel (print, TV, internet, etc.). Use serv2503 for amounts, serv2512 for channel mix.
- For temp/staffing: serv2502 = revenue by service/personnel type; serv2511 = hours sold by client industry. The erhverv codes in serv2511 (T70020...) correspond to the 70xxx codes in serv2502.
- For professional/technical services each has its own table: serv2504 (juridisk), serv2507 (arkitekt), serv2508 (teknisk afprøvning), serv2509 (ingeniørrådgivning), serv2510 (markedsanalyse). No cross-sector table exists.
