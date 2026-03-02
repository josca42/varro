<fact tables>
<table>
id: paaroe01
description: Gennemsnitsafstand (km) til 0-24-åriges bedsteforældre 1. januar efter relationstype, hovedpersonens bopæl, hovedpersonens alder og tid
columns: relationtyp, hovedbopael, hoald, tid (time), indhold (unit Km)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: paaroe02
description: Befolkningen (0-24-årige) 1. januar efter hovedpersonens alder, antal relationer og tid
columns: hoald, antalrela, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2025-01-01
</table>
<table>
id: paaroe03
description: Befolkningen 1. januar efter relation, hovedpersonens bopæl og tid
columns: relation, hovedbopael, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2025-01-01
</table>
<table>
id: paaroe04
description: Befolkningen 1. januar efter relation, hovedpersonens alder og tid
columns: relation, hoald, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2025-01-01
</table>
<table>
id: paaroe05
description: Befolkningen 1. januar efter relation, hovedpersonens alder og tid
columns: relation, hoald, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2025-01-01
</table>
<table>
id: paaroe30
description: Befolkningens kontakt til praktiserende læge (0-17 år) efter relation, nøgletal, alder, køn og tid
columns: parorendeforhold, bnogle, alerams, koen, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: paaroe31
description: Befolkningens kontakt til praktiserende læge (18 år eller derover) efter relation, nøgletal, alder, køn og tid
columns: parorendeforhold, bnogle, alerams, koen, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: paaroe50
description: Personer visiteret til hjemmehjælp (andel af 65-84-årige) efter indikator, område, alder, relation og tid
columns: indikator, omrade, alder, parorendeforhold, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2024-01-01
</table>
<table>
id: paaroe51
description: Visiteret hjemmehjælp, tid pr. person efter indikator, område, alder, relation og tid
columns: indikator, omrade, alder, parorendeforhold, tid (time), indhold (unit Gns. antal timer pr. uge)
tid range: 2019-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- The tables split into three thematic groups: (1) family structure of the general population (paaroe02–05), (2) GP contact by family type (paaroe30–31), (3) home care for elderly by family type (paaroe50–51). paaroe01 stands alone as a distance-to-grandparents table.
- For "how many Danes have [relation type]": use paaroe03 (by region, kommuner) or paaroe04 (by age group). Both use mutually exclusive K00–K15 combination codes — safe to sum and compute shares. paaroe05 also counts by individual relation type but those counts are NOT mutually exclusive (one person appears in multiple relation rows).
- paaroe03 vs paaroe04: identical population, different cross-tabulation. paaroe03 has regional breakdown (kommuner only, no regioner), paaroe04 has broad age groups. Neither has both together.
- For 0–24 year olds specifically: paaroe02 (number of living parents/grandparents, 2020–2025) and paaroe01 (distance to grandparents, 2024 only).
- For GP contact: paaroe30 = children 0–17 (by 1 vs 2 parents), paaroe31 = adults 18+ (by partner/relative combinations). bnogle is a measurement selector in both — always filter to 1000 (count) or 1010 (pct).
- For home care (elderly 65–84): paaroe50 = share receiving home care (pct.), paaroe51 = hours per week per person. Query together for full picture. indikator is a gender measurement selector in both — always filter.
- The parorendeforhold codes used in paaroe31/50/51 are the same four adult categories (PR810–PR840). This allows direct comparison of GP contact and home care uptake by family structure.
- All tables with koen/alerams/hoald include total-row codes (10/IALT/9817/9924/TOT). Always filter these to avoid double-counting across dimensions.
- Map: paaroe01 (distance to grandparents), paaroe03 (population by family structure), paaroe50 (home care share), paaroe51 (home care hours) all support choropleth maps via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1).