<fact tables>
<table>
id: byg62
description: Omkostningsindeks for anlæg efter indekstype, enhed og tid
columns: indekstype, tal, tid (time), indhold (unit Indeks)
tid range: 1986-07-01 to 2025-04-01
</table>
<table>
id: byg71
description: Omkostningsindeks for anlæg efter indekstype, enhed og tid
columns: indekstype, tal, tid (time), indhold (unit -)
tid range: 1987-01-01 to 2024-01-01
</table>
<table>
id: byg33
description: Byggeomkostningsindeks for boliger efter hovedindeks, art, enhed og tid
columns: hindeks, art, enhed, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2024-01-01
</table>
<table>
id: byg43
description: Byggeomkostningsindeks for boliger efter hovedindeks, delindeks, art, enhed og tid
columns: hindeks, dindeks, art, tal, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2025-04-01
</table>
<table>
id: byg53
description: Byggeomkostningsindeks for boliger efter hovedindeks, delindeks, art, enhed og tid
columns: hindeks, dindeks, art, tal, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2024-01-01
</table>
<table>
id: pris90
description: Producentprisindeks for byggeri af boliger efter boligtype, enhed og tid
columns: boltyp, enhed, tid (time), indhold (unit Indeks)
tid range: 2015-01-01 to 2025-04-01
</table>
<table>
id: pris91
description: Producentprisindeks for renovering og vedligeholdelse efter arbejdets art, enhed og tid
columns: arbart, tal, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: bygpro1
description: Produktionsindeks for bygge- og anlægssektoren efter branche og tid
columns: branche, tid (time), indhold (unit Indeks)
tid range: 2008-01-01 to 2025-08-01
</table>
</fact tables>

notes:
- UNIVERSAL GOTCHA: Every table except bygpro1 has a measurement selector column (`tal` or `enhed`) that mixes index levels and percentage changes in the same column. Always filter to a single `tal`/`enhed` value before reading `indhold` — forgetting this silently multiplies row counts by 2–3x.
- Two families of tables: **anlæg** (infrastructure cost index) and **boliger** (residential construction cost index).
  - Anlæg: byg62 (quarterly, 1986–2025) and byg71 (annual, 1987–2024). Same indekstype categories covering veje, jordarbejde, asfalt, beton, jernkonstruktioner, lastvogn, drift.
  - Boliger cost index: byg43 (quarterly, 2003–2025, most detailed) / byg53 (annual, 2003–2024) have hindeks×dindeks×art breakdown. byg33 (annual, 2003–2024) is the simplified version with only hindeks×art (no dindeks).
- For the **most current data**: byg62 (anlæg, quarterly to 2025-Q2), byg43 (boliger, quarterly to 2025-Q2), pris90 (producentpris boliger, quarterly to 2025-Q2), bygpro1 (production index, monthly to 2025-08).
- byg33 is the only boligomkostning table where hindeks has no "boliger i alt" total (only enfamiliehuse and etageboliger). For a total, use byg43/byg53 with `hindeks=1`.
- **pris vs byg**: pris90/pris91 are producer price indexes (what builders charge); byg33/byg43/byg53 are cost indexes (what inputs cost builders). Different economic concepts.
- **pris90** only covers enfamiliehuse (boltyp=111) despite the dim.ejendom join. Do not join dim.ejendom without `WHERE d.niveau=1` — kode 111 appears at both niveau 1 and 2, doubling rows.
- **bygpro1** (production volume index, monthly) is structurally different: no measurement selector, branche codes are non-standard (F41/F42/F43/20100) and cannot be joined to dim.db. Use code 20100 for the sector total.
- **pris91** covers renovation and maintenance — distinct topic from new construction. Annual only, 2014–2024.