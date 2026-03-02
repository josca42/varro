<fact tables>
<table>
id: hfudd16
description: Befolkningens højest fuldførte uddannelse (15-69 år) efter bopælsområde, højest fuldførte uddannelse, socioøkonomisk status, branche, alder, køn og tid
columns: bopomr, uddannelsef, socio, erhverv, alder, koen, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: laby19
description: Befolkningens højest fuldførte uddannelse (15-69 år) (antal) efter kommunegruppe, højest fuldførte uddannelse, alder og tid
columns: komgrp, hfudd2, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: laby19a
description: Befolkningens højest fuldførte uddannelse (15-69 år) (andel i procent)) efter kommunegruppe, højest fuldførte uddannelse og tid
columns: komgrp, hfudd2, tid (time), indhold (unit Andel i pct.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ligeub1
description: Befolkningens højeste fuldførte uddannelse (15-69 år) efter bopælsområde, herkomst, højest fuldførte uddannelse, alder, køn og tid
columns: bopomr, herkomst, hfudd, alder, kon, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ligeui1
description: Ligestillingsindikator for befolkningens højeste fuldførte uddannelse (15-69 år) efter højest fuldførte uddannelse, indikator, alder, bopælsområde, herkomst og tid
columns: uddannelsef, indikator1, alder1, bopomr, herkams, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ligeui0
description: Ligestillingsindikator for befolkningens højeste fuldførte uddannelse efter højest fuldførte uddannelse, indikator, alder og tid
columns: hfudd, indikator, alder, tid (time), indhold (unit -)
tid range: 1986-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables cover ages 15-69. Education levels use a shared H10-H90 classification (H10=Grundskole, H20=Gymnasial, H30=Erhvervsfaglig, H35=Adgangsgivende, H40=KVU, H50=MVU, H60=Bachelor, H70=LVU, H80=Ph.d., H90=Uoplyst). None of these join dim.ddu_udd — treat them as inline coded values.
- For counts with rich breakdowns (socio, industry, region, age, sex): use hfudd16 (2008-2023). Has bopomr joining dim.nuts (regioner+kommuner), socio (4 employment status groups, no total row), erhverv (filter to 'TOT' to avoid overcounting), uddannelsef.
- For counts by municipality with detailed education subcategories: use laby19 (2008-2024). hfudd2 has 92 codes across multiple hierarchy levels — filter WHERE LENGTH(hfudd2)=3 for the 10 top-level categories. komgrp includes both the 5 kommunegruppe types (1-5) and individual kommuner (101-860).
- For kommunegruppe percentages only (no municipality detail): use laby19a (2008-2024). Values are shares in pct., not counts.
- For counts with herkomst (origin) breakdown: use ligeub1 (2005-2024, the longest count series). herkomst uses inline codes (0/10/21/24/25/31/34/35) — filter to one hierarchy level. bopomr joins dim.nuts.
- For gender gap indicators (% men, % women, procentpoint difference): use ligeui1 (2005-2024, with region+herkomst) or ligeui0 (1986-2024, national only). Both have indikator/indikator1 as a MEASUREMENT SELECTOR — always filter to one value (LA1/LA2/LA3) or results are tripled.
- herkomst dimension: ligeub1.herkomst and ligeui1.herkams use the same inline coding (0/10/21/24/25/31/34/35) but do NOT join dim.herkomst (which uses codes 1/2/3/9).
- Map: hfudd16, ligeub1, ligeui1 support choropleth via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) on bopomr=dim_kode. laby19 supports kommune-level maps on komgrp=dim_kode (filter komgrp > 100).