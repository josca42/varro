<fact tables>
<table>
id: barsel04
description: Forældres orlov før fødslen samt i barnets første leveår efter enhed, berettigelse, mors uddannelse, fars uddannelse, område og tid
columns: tal, beret, morud, farud, omrade, tid (time), indhold (unit Dage)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: barsel06
description: Ikke samboende forældres orlov før fødslen samt i barnets første leveår efter enhed, dagpengeret, eksistens, uddannelseskombination, område og tid
columns: tal, dagpengeret, eksistens, uddkomb, omrade, tid (time), indhold (unit Dage)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: barsel11
description: Dage med barselsdagpenge (forældreårgange) efter enhed, berettigelse, sektor, social status, branche og tid
columns: enhed, beret, sektor, socialstatus, branche, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: barsel14
description: Dage med barselsdagpenge (forældreårgange) efter enhed, berettigelse, branche og tid
columns: enhed, beret, erhverv, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: barsel25
description: Orlov før fødslen og i barnet to første leveår for samboende forældre med mere end 46 ugers barselsorlov efter enhed, berettigelse, mors uddannelse, fars uddannelse, område og tid
columns: tal, beret, morud, farud, omrade, tid (time), indhold (unit Dage)
tid range: 2016-01-01 to 2022-01-01
</table>
<table>
id: barlov1
description: Orlov før fødslen samt i barnets første leveår afholdt af samboende forældre til et barn (født 2. august - 31. december) efter enhed, berettigelse, mors uddannelse, fars uddannelse, område og tid
columns: tal, beret, morud, farud, omrade, tid (time), indhold (unit Dage)
tid range: AUG - DEC 2019 to AUG - DEC 2023
</table>
<table>
id: barlov2
description: Samboende forældre på barselsorlov i barnets første leveår (børn født 2. august - 31. december) efter enhed, berettigelse, mors uddannelse, fars uddannelse, uger og tid
columns: tal, beret, morud, farud, uger, tid (time), indhold (unit Antal)
tid range: AUG - DEC 2019 to AUG - DEC 2023
</table>
<table>
id: barlov3
description: Samboende forældre på barselsorlov i barnets første leveår (børn født 2. august - 31. december) efter enhed, berettigelse, område, uger og tid
columns: tal, beret, omr20, uger, tid (time), indhold (unit Antal)
tid range: AUG - DEC 2019 to AUG - DEC 2023
</table>
<table>
id: ligefb1
description: Forældrepar efter barnets familieforhold, forældrenes dagpengeret, moderens højest fuldførte uddannelse, faderens højeste fuldførte uddannelse, område og tid
columns: barnfam, foraeldredagpenge, morudd, farudd, omrade, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: ligefi1
description: Ligestillingsindikator for barselsdagpengedage til forældrepar (gennemsnit) efter indikator, moderens højest fuldførte uddannelse, faderens højeste fuldførte uddannelse, forældrenes uddannelsesniveau, område og tid
columns: indikator, morudd, farudd, foraeldreudd, omrade, tid (time), indhold (unit Dage)
tid range: 2016-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All tables cover parent cohorts by child's birth year (forældreårgange), not calendar-year flows. "2020" means children born in 2020 and their parents' leave over the following 1–2 years.
- **Measurement selector pattern**: barsel04, barsel06, barsel25, barlov1, barlov2, barlov3 all have a `tal` column that selects the measure (antal par, avg maternal days, avg paternal days, etc.). Every other dimension combination is repeated for each `tal` value — always filter to one `tal` or you will overcount by 8–15×. barsel11 and barsel14 use `enhed` the same way.
- **Main tables by population**:
  - Cohabiting parents, all births, annual 2015–2023: **barsel04** (region to kommune level, separate mother+father education).
  - Non-cohabiting parents, all births, annual 2015–2023: **barsel06** (landsdele only, combined education).
  - Cohabiting parents with >46 weeks leave, annual 2016–2022: **barsel25** (same structure as barsel04, subset only — not representative).
  - Cohabiting parents, Aug–Dec births only (post-reform cohorts), 2019–2023: **barlov1** (totals with region+education), **barlov2** (week-by-week distribution × education), **barlov3** (week-by-week × region). Do not compare magnitudes to barsel04 (partial birth year).
- **Industry breakdown**: **barsel11** (12 coarse NACE divisions via dim.db, + sektor + socialstatus, no region), **barsel14** (128 granular proprietary codes, no region — do not join to dim.db, treat erhverv as inline-coded).
- **Equality indicators**: **ligefb1** (count of parent pairs by family + education + region) and **ligefi1** (avg leave days with mother/father/gap indicator). ligefi1 values are averages — never SUM.
- **Regional coverage**: barsel04, barsel25, barlov1, barlov3 have both landsdele (niveau 2) and kommuner (niveau 3). barsel06, ligefb1, ligefi1 have landsdele only. omrade/omr20 code `0` = national total, not joinable to dim.nuts.
- **beret totals**: barsel04/barsel25/barlov1 use `beret='3'` for all parents. barsel11/barsel14/barlov2/barlov3 have no "all parents" total in beret.
- **Map**: barsel04, barsel25, barlov1, barlov3 support kommune (niveau 3) and landsdele (niveau 2) choropleths via /geo/kommuner.parquet and /geo/landsdele.parquet. barsel06, ligefb1, ligefi1 support landsdele only. barsel11 and barsel14 have no geographic column.