table: fact.ofats4
description: Danske datterselskaber i udlandet efter land, enhed og tid
measure: indhold (unit Antal)
columns:
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- enhed: values [DSANTAL=Datterselskaber, DSANSAT=Ansatte]
- tid: date range 2007-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md

notes:
- enhed is a measurement selector: every land/tid combination exists twice — DSANTAL (antal datterselskaber) and DSANSAT (antal ansatte). Always filter to one value.
- land joins dim.lande_uhv at niveau 4 (individual countries, alpha-2 codes). 151 distinct land codes; 146 match the dim. The 5 non-matching codes are:
  - TOT = world total aggregate (exclude when summing across countries)
  - GG = Guernsey, IM = Isle of Man (British Crown Dependencies), RS = Serbia, AN = Netherlands Antilles (dissolved territory) — real countries/territories just absent from the GEONOM dim. Use them as direct label codes or look up manually.
- Use LEFT JOIN dim.lande_uhv to preserve all 151 land codes including the unmatched ones.
- lande_uhv has a deep hierarchy (verdensdel → region → underregion → land → område). For continent-level aggregation from this table, join at niveau 1–3 via parent_kode chains rather than summing fact rows directly.
- ColumnValues("lande_uhv", "titel", for_table="ofats4") will show the 146 matched countries with labels.