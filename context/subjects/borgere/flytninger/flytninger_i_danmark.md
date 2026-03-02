<fact tables>
<table>
id: fly
description: Samtlige flytninger efter køn, alder og tid
columns: kon, alder, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: fly33
description: Flytninger inden for kommuner efter område, alder, køn og tid
columns: omrade, alder, kon, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: fly55
description: Flytninger mellem regioner efter køn, alder, tilflytningsregion, fraflytningsregion og tid
columns: koen, alder, tilreg, frareg, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: fly66
description: Flytninger mellem kommuner efter tilflytningskommune, fraflytningskommune, alder, køn og tid
columns: tilkommune, frakommune, alder, kon, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: flydag
description: Flytninger efter flyttedag, flyttemåned og tid
columns: flyttedag, flyttedmaned, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: flyung1
description: Flytninger blandt unge (15-29-årige) efter flyttetype, fraflytningskommune, tilflytningssted og tid
columns: flyttetype, frakommune, tilflytomr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: flyung2
description: Flytninger blandt unge (15-29-årige) efter flyttetype, tilflytningskommune, tilflytningssted og tid
columns: flyttetype, tilkommune, tilflytomr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: flyung3
description: Flytninger blandt unge (15-29-årige) efter flyttetype, fraflytningslandsdel, aldersgruppe og tid
columns: flyttetype, fraflytland, agebygroup, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: flyung4
description: Flytninger blandt unge (15-29-årige) efter flyttetype, tilflytningslandsdel, aldersgruppe og tid
columns: flyttetype, tilflytland, agebygroup, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: flyung5
description: Flytninger blandt unge (15-29-årige) efter flyttetype, fraflytningslandsdel, tilflytningslandsdel og tid
columns: flyttetype, fraflytland, tilflytland, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: flyung6
description: Flytninger blandt unge (15-29-årige) efter flyttetype, alder, tilflytningssted og tid
columns: flyttetype, alder, tilflytomr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- **fly** is the master national table (1980–2024) with individual ages 0–99 and kon M/K. Use for long time series or age profiles without geography. No total rows — safe to sum directly.
- **fly33** (within-municipality moves), **fly55** (between-region moves), **fly66** (between-municipality moves) partition the move types. They don't overlap: fly33 = intra-municipal, fly66 = inter-municipal, fly55 = aggregation of fly66 to region level. For all moves combined use fly.
- **fly55** uniquely uses `koen` with integer codes 1/2 instead of the M/K `kon` used by all other tables. Watch for this when writing SQL across tables.
- **fly55** and **fly66** are origin-destination matrices. To get moves *into* a region/municipality filter on `tilreg`/`tilkommune`; for moves *out* filter on `frareg`/`frakommune`. Sum across all rows for the national total without double-counting.
- **flydag** breaks moves down by day-of-month and month, nationally. Has TOT aggregate codes in both dimensions — always filter one to TOT when grouping by the other.
- **flyung1–flyung6** all cover only young people aged 15–29 (from 2007). They classify moves by `flyttetype` (101=fra forældre, 102=til forældre, 103=med/mellem forældre, 104=øvrige). All flyung tables have aggregate code `0` for overall moves.
- flyung1 (by frakommune) / flyung2 (by tilkommune): municipality-level with extra aggregate codes TOTFK/TOTTK outside dim.nuts — filter or use LEFT JOIN when joining.
- flyung3 (fra landsdel) / flyung4 (til landsdel) / flyung5 (fra×til landsdel matrix): landsdel codes are zero-padded strings (01–09, 10, 11). Join with `f.col::int = d.kode::int AND d.niveau = 2` — the standard text join only works for 10 and 11.
- flyung6: national young-people moves by individual age (15–29) and move type — use when you need single-year age detail for young movers without geography.
- Map support: fly33, fly66 (kommune, kommuner.parquet), fly55 (region, regioner.parquet), flyung1/flyung2 (kommune, kommuner.parquet, cast to int), flyung3/flyung4/flyung5 (landsdel, landsdele.parquet, cast to int). fly, flydag, flyung6 have no geographic column.