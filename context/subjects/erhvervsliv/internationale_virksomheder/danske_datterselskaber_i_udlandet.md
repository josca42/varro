<fact tables>
<table>
id: ofats1
description: Danske datterselskaber i udlandet efter branche, enhed og tid
columns: branche, enhed, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: ofats2
description: Danske datterselskaber i udlandet efter lande, enhed og tid
columns: lande, enhed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2023-01-01
</table>
<table>
id: ofats3
description: Danske datterselskaber i udlandet efter lande, branche, enhed og tid
columns: lande, branche, enhed, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2023-01-01
</table>
<table>
id: ofats4
description: Danske datterselskaber i udlandet efter land, enhed og tid
columns: land, enhed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All four tables share the same enhed column (DSANTAL=datterselskaber, DSANSAT=ansatte). Always filter enhed to one value — failing to do so silently doubles all counts.
- Choose table by what breakdown you need:
  - **ofats2** — by broad world region (EU-15, EU-27, Nordamerika, Asien, etc.), from 2007.
  - **ofats1** — by industry (DB07 10-groupering, niveau 1), from 2010.
  - **ofats3** — by region AND industry combined, from 2010. Note: branche 3910 is a special aggregate of sparse industries (landbrug, bygge og anlæg, offentlig admin, kultur) — it has no dim.db_10 match.
  - **ofats4** — by individual country (alpha-2 codes, ~150 countries), from 2007. Most granular geography.
- All tables have TOT rows in their categorical columns (lande, branche, land). Exclude TOT when computing your own aggregates to avoid double-counting.