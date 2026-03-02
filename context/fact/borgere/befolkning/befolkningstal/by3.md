table: fact.by3
description: Befolkningen 1. januar efter byområder og landdistrikter, folketal areal og befolkningstæthed og tid
measure: indhold (unit -)
columns:
- byer: values [1100=000-01100 Hovedstadsområdet, 10101100=101-01100 København (del af Hovedstadsområdet), 10199999=101-99999 Landdistrikter, 14701100=147-01100 Frederiksberg (del af Hovedstadsområdet), 14799999=147-99999 Landdistrikter ... 86018377=860-18377 Lørslev, 86018378=860-18378 Tårs, 86018403=860-18403 Rakkeby, 86099997=860-99997 Uden fast bopæl, 86099999=860-99999 Landdistrikter]
- folkartaet: values [FOLKETAL=Folketal, AREAL=Areal (km2), BEFTAET=Befolkningstæthed (km2)]
- tid: date range 2017-01-01 to 2025-01-01

notes:
- CRITICAL: folkartaet is a measurement selector with three incompatible units in the same indhold column: FOLKETAL=persons, AREAL=km², BEFTAET=persons/km². Always filter to one folkartaet value. Never sum across all three.
- Each byer area appears three times per tid — once for each folkartaet. The table has ~1700 distinct byer codes.
- Same hierarchical byer coding as by1 (compound codes encode municipality + urban area). Aggregate codes (like 1100=Hoofdstadsområdet) overlap with their sub-areas — do not sum all byer codes.
- Shorter time range (2017–) than by1 (2010–). No age/sex breakdown — use by1 for demographics by urban area.