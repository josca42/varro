<fact tables>
<table>
id: enebr
description: Industriens energiforbrug efter branche (DB07), enhed og tid
columns: branche07, enhed, tid (time), indhold (unit -)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: enegeo
description: Industriens energiforbrug efter kommune og tid
columns: komk, tid (time), indhold (unit 1.000 GJ (gigajoule))
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: enetype
description: Industriens energiforbrug efter energitype, enhed og tid
columns: energi1, enhed, tid (time), indhold (unit -)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: enevp
description: Varmepumper i råstofindvinding og industri efter branche (DB07), nøgletal og tid
columns: branche07, bnogle, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2024-01-01
</table>
<table>
id: brande01
description: Boliger med brænde- eller træpilleovn og forbrug af brænde eller træpiller efter nøgletal og tid
columns: aktp, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2023-01-01
</table>
<table>
id: brande02
description: Boliger med brændeovn og forbrug af brænde efter primær varmekilde, enhed og tid
columns: pvarmekilde, enhed, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: brande03
description: Boliger med brændeovn og forbrug af brænde efter boligtype, enhed og tid
columns: boltyp, enhed, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: pille02
description: Boliger med træpilleovn og forbrug af træpiller efter primær varmekilde, enhed og tid
columns: pvarmekilde, enhed, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: pille03
description: Boliger med træpilleovn og forbrug af træpiller efter boligtype, enhed og tid
columns: boltyp, enhed, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: gaslager
description: Naturgaslagre  (eksperimentel statistik) efter uger og tid
columns: uger, tid (time), indhold (unit TJ (terajoule))
tid range: 2019-01-01 to 2025-01-01
</table>
<table>
id: gasbrug
description: Naturgasforbrug ekskl. bionaturgas pr. uge (eksperimentel statistik) efter uger og tid
columns: uger, tid (time), indhold (unit TJ (terajoule))
tid range: 2019-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- For industrial energy consumption by branch: enebr (2012-2024 biennially, by DB07 branch). For breakdown by energy type: enetype (same coverage). For geographic breakdown by municipality/region: enegeo (2012-2024 biennially, joins dim.nuts). These three cover the same population (råstofindvinding og industri) from different angles.
- enebr and enetype both have an enhed selector (GJFAK vs. PCTAEND). Always filter to one enhed — failing to do so silently doubles all row counts. enegeo has no enhed (always 1.000 GJ).
- For heat pump statistics in industry: enevp (2020-2024, by branch and nøgletal). bnogle encodes incompatible metrics with different units — pick one metric per query.
- For wood/pellet heating in homes: brande01 gives a national time series (odd years 2013-2023) of counts and consumption. brande02/brande03 and pille02/pille03 give 2023-only cross-sections by primary heat source and housing type respectively.
- For gas storage and weekly consumption: gaslager (storage level, TJ) and gasbrug (weekly consumption, TJ), both 2019-2025, experimental statistics. Time is indexed by tid (year) + uger (week U01-U53) together.
- The brande/pille tables all have enhed selectors using numeric codes (1300-1450). boltyp and pvarmekilde include total rows (1140/1045). Enfamilieshuse (1160) splits into sub-codes 1162 and 1164 — don't sum parent + children.
- Map: enegeo supports choropleth maps — kommune-level (niveau 3) via context/geo/kommuner.parquet or region-level (niveau 1) via context/geo/regioner.parquet, merge on komk=dim_kode.