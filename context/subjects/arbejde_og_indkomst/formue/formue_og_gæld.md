<fact tables>
<table>
id: formue11
description: Formue efter formuetype, enhed, alder, køn, population og tid
columns: form1, enhed, alder, kon, popu, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: formue12
description: Formue efter formuetype, enhed, område, alder, population og tid
columns: form1, enhed, omrade, alder, popu, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: formue13
description: Formue efter formuetype, enhed, socioøkonomisk status, population og tid
columns: form1, enhed, socio, popu, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: formue14
description: Formue efter formuetype, enhed, alder, herkomst, population og tid
columns: form1, enhed, alder, herkomst, popu, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: formue15
description: Formue efter formue, definition, prisenhed, alder og tid
columns: formue, definition, prisenhed, alder, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2023-01-01
</table>
<table>
id: formue16
description: Formue efter percentil, prisenhed, alder og tid
columns: percentil, prisenhed, alder, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2023-01-01
</table>
<table>
id: formue17
description: Formue efter formuetype, enhed, alder, familietype, population og tid
columns: form1, enhed, alder, famtyp, popu, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: laby11
description: Median for Nettoformue, 18 år+ efter kommunegruppe, aldersstandardisering og tid
columns: komgrp, aldersstand, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: laby12
description: Nettoformue (median) efter kommunegruppe, alder og tid
columns: komgrp, alder, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: laby14
description: Negativ nettoformue (andel af befolkningen) efter kommunegruppe, alder og tid
columns: komgrp, alder, tid (time), indhold (unit Pct.)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: ligeii7
description: Ligestillingsindikator for median nettoformue efter indikator, alder, familietype og tid
columns: indikator, alder, famtyp, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: ligeii8
description: Ligestillingsindikator for median pensionsformue for personer efter indikator, alder og tid
columns: indikator, alder, tid (time), indhold (unit -)
tid range: 2014-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- formue11-17 share three mandatory selector columns that must always be filtered: form1 (46 wealth type codes in a hierarchy — totals + subtotals + line items, summing across them double-counts), enhed (9 measurement units: median/quartile/mean × fixed/nominal prices + count), and popu (5005=all persons vs 5025=only those holding that asset). Forgetting any one multiplies row counts.
- 2014 vs 2020 definition: FGNF2014/FGAK2014 use the older narrower definition (excludes unlisted equities and collection debt). FGNF2020/FGAK2020 use the broader 2020 definition. For consistent time series back to 2014 use the 2014-definition codes; for most current analysis use 2020. Note: FGF3 (gæld til inddrivelse) is missing for 2017-2019, affecting FGNF2014.
- Table selector by breakdown:
  - By gender: formue11 (finest age bands: 5-year groups from 18-24 to 90+)
  - By region/kommune: formue12 (nuts niveau 1=5 regioner, niveau 3=99 kommuner; coarser age groups)
  - By socioeconomic status: formue13 (19 socio codes; 3 are aggregates not in dim.socio — use ColumnValues)
  - By origin: formue14 (own 6-code west/non-west scheme, not dim.herkomst — use inline codes)
  - By wealth bracket (distribution): formue15 — 2020-2023 only, counts persons per bracket
  - By percentile: formue16 — 2020-2023 only, wealth threshold at each percentile P1-P99
  - By family type: formue17 — per-family measurement (not per-person); enhed=245 for family count
- laby11/12/14 are simpler pre-aggregated tables (kommunegrupper only, no form1/enhed/popu selectors). laby11 adds age standardization for fair cross-group comparison; laby12 breaks by age; laby14 shows share of population with negative nettoformue (Pct.). komgrp=0 in all three is the national total (not in dim).
- ligeii7/8 are pre-computed gender gap tables. ligeii7=nettoformue by family type; ligeii8=pensionsformue by age. Both mix units per indikator (kr. and pct.) — always filter to one indikator value.
- formue15 and formue16 only cover 2020-2023. All other tables cover 2014-2023.
- Map: formue12 supports choropleth via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) on omrade. laby11, laby12, laby14 support kommune-level choropleth via context/geo/kommuner.parquet — komgrp niveau=2 codes are identical to NUTS niveau=3 kommune codes.