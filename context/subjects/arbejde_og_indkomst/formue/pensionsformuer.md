<fact tables>
<table>
id: tjen01
description: Optjent tjenestemandspension for aktive tjenestemænd efter sektor, enhed, køn, faggruppe aldersgrupper og tid
columns: sektor, enhed, koen, faggrp, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: tjen02
description: Optjent tjenestemandspension for pensionerede tjenestemænd efter sektor, enhed, køn og tid
columns: sektor, enhed, koen, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: pensoc
description: Husholdningernes pensionsrettigheder i socialforsikringsordninger efter pensionsordninger, konto og tid
columns: pensord, konto, tid (time), indhold (unit Mio. kr.)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: penfor11
description: Pensionsformue for personer bosat i Danmark efter pensionsform, beskatning, alder, køn, enhed og tid
columns: pensionsform, beskat, alder, koen, enhed, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: penfor12
description: Personers pensionsformue efter familietype, alder, køn, prisenhed, pensionsformue og tid
columns: famtyp, alder, koen, prisenhed, penformue, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: penfor20
description: Pensionsformue efter pensionsform, selskabstype, alder, population, beskatning, enhed og tid
columns: pensionsform, seltype, alder, popu, beskat, enhed, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: penindb1
description: Personer med pensionsindbetalinger efter område, enhed, køn, alder, pensionstype og tid
columns: omrade, enhed, koen, alder1, pentyp, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: laby15
description: Pensionformue for personer mindre end 5 år fra folkepensionsalderen (median) efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2023-01-01
</table>
</fact tables>
notes:
- For pension wealth by age/gender/type (individual level): penfor11 (persons resident in Denmark, includes ATP, has GNS/median/quartiles) or penfor20 (also covers non-residents via popu=ALLE, breaks down by financial institution type seltype, no ATP). Both cover 2014-2024.
- For wealth distribution histogram (how many persons in each bracket): penfor12 — gives count of persons by penformue bracket and familietype. Use penfor11 for summary statistics instead.
- For geographic breakdown of pension contributions (indbetalinger, not formue): penindb1 — the only table with regional/kommune level data (nuts). Covers 2005-2024.
- For near-retirement pension preparedness by municipality type: laby15 — median pensionsformue for persons <5 years from folkepensionsalderen, by kommunegruppe/kommune. 2014-2023.
- For civil servant (tjenestemænd) pension data: tjen01 (aktive tjenestemænd, with faggruppe and aldersgruppe breakdown) and tjen02 (pensionerede tjenestemænd, no faggruppe). Both cover 2014-2023.
- For macro-level national accounts pension liabilities: pensoc — husholdningssektorens samlede pensionsrettigheder i Mio. kr., with accounting flow/stock breakdown (konto). 2015-2023. No individual/geographic breakdown.
- enhed/prisenhed measurement selector pitfall: tjen01, tjen02, penfor11, penfor20, and penindb1 all have a measurement selector column (enhed) that repeats every dimension combination for each stat type. Always filter to exactly one value or results will be inflated 3-5x.
- tjen01 faggrp gotcha: the column mixes two classification schemes (A-prefix=aldersgrupper, B-prefix=faggrupper). Always filter to one scheme; never sum A and B rows together.
- Map: penindb1 supports choropleth maps via context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. No other tables in this subject have geographic breakdowns.
