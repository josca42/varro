<fact tables>
<table>
id: straf70
description: Anholdelser efter køn, overtrædelsens art, afslutningsmåde, alder og tid
columns: kon, overtraed, afslut, alder, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: straf71
description: Anholdelser efter køn, alder, bopæl i Danmark og tid
columns: kon, alder, bopdk, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: straf72
description: Anholdelser efter bopæl i Danmark, overtrædelsens art og tid
columns: bopdk, overtraed, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: straf73
description: Anholdelser efter køn, alder, uddannelse og tid
columns: kon, alder, uddannelse, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: straf74
description: Anholdelser efter overtrædelsens art, uddannelse og tid
columns: overtraed, uddannelse, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All 5 tables cover the same period (2015–2024, annual) and measure arrests (anholdelser) in count (Antal). None have regional breakdown.
- Pick by what you need to cross-tabulate:
  - straf70: offense type × completion method (løsladt/varetægt/afsoning) × kon × alder — most dimensions, use for rich demographic/crime-type breakdowns.
  - straf71: kon × alder × residency in Denmark — cleanest table for "who gets arrested" without crime type.
  - straf72: offense type × residency in Denmark — use when the question involves citizens vs non-residents by crime.
  - straf73: kon × alder × education level — demographics + education, no crime type.
  - straf74: offense type × education level — crime type + education, no other demographics.
- overtraed column (straf70, 72, 74): joins dim.overtraedtype on `f.overtraed::text = d.kode::text`. Niveau 1 (3 main categories), 2 (12 categories), and 3 (~40 subcategories) are all present simultaneously in the fact table. Always add `AND d.niveau = X` to the join to pick one level. About 29% of overtraed codes are aggregate-only (TOT, AVA-suffix subtotals, concatenated range codes) and have no dim match — they fall out automatically on the join.
- Every table has total rows in every dimension. Failing to filter totals in non-target dimensions silently multiplies counts. Pattern: kon='TOT', alder='TOT', bopdk='0', afslut='B00', uddannelse='TOT', overtraed='TOT'.