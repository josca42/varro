<fact tables>
<table>
id: rst01
description: Råstofindvinding (1000 m3) efter område, råstoftype og tid
columns: omrade, rastoftype, tid (time), indhold (unit 1.000 m3)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: rst04
description: Losning af råstoffer fra havet (1000 m3) efter område, råstoftype og tid
columns: omrade, rastoftype, tid (time), indhold (unit 1.000 m3)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: rst3
description: Råstoffer indvundet fra Farvande (1000 m3) efter område, råstoftype og tid
columns: omrade, rastoftype, tid (time), indhold (unit 1.000 m3)
tid range: 1990-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Three tables covering raw material extraction in Denmark, all measuring in 1.000 m³:
  - rst01: land-based extraction by region/kommune (NUTS join, 2006–2024)
  - rst04: sea extraction offloaded/landed by region/kommune (NUTS join, 2007–2024)
  - rst3: sea extraction by named sea area (inline omrade, 1990–2024)
- For sea extraction: rst3 answers "from which sea area?" while rst04 answers "where was it landed?". They cover the same activity from different geographic perspectives.
- For historical sea data before 2007, only rst3 is available.
- All three tables include aggregate rows: omrade '0' = national total; rastoftype TOTLAND (rst01) or TOTHAV (rst04/rst3) = total across material types. Always filter these out when summing to avoid double-counting.
- rst01 and rst04 both have NUTS-linked omrade at multiple hierarchy levels (niveau 1 = regioner, niveau 3 = kommuner). Filter to one niveau before aggregating or you will double-count.
- Map: rst01 and rst04 support choropleth maps via /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1). rst04 also has niveau 2 → /geo/landsdele.parquet. rst3 uses inline sea area names with no geo file match.