<fact tables>
<table>
id: neet1
description: Befolkningen (16-24 år) efter NEET-status, køn, bopælsområde, socioøkonomisk status og tid
columns: statusneet, kon, bopomr, socio, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: neet2
description: Befolkningen (16-24 år) efter NEET-status, bopælsområde, køn, alder og tid
columns: statusneet, bopomr, kon, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: laby10
description: Andel af unge (16-24 år) uden for beskæftigelse og uddannelse (NEET) efter kommunegruppe, alder og tid
columns: komgrp, alder, tid (time), indhold (unit Pct.)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: ligeai6
description: Ligestillingsindikator for NEET efter indikator, bopælsområde, alder og tid
columns: indikator, bopomr, alder, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For NEET counts (Antal) with socioøkonomisk breakdown: use neet1 (has statusneet, kon, bopomr, socio — 27 socio categories).
- For NEET counts (Antal) with individual age breakdown (16-24): use neet2 (has statusneet, bopomr, kon, alder — no socio).
- For NEET percentage at municipality level: use laby10 (Pct., has komgrp joining dim.kommunegrupper at both kommunegruppe-type and individual-kommune level).
- For gender gap analysis (% mænd vs. % kvinder vs. forskel i procentpoint): use ligeai6.
- All four tables cover 2008–2023 (annual, tid in Jan-01 format).
- All tables with bopomr join dim.nuts — but bopomr='0' (national total) is NOT in dim.nuts and is dropped on join. Three geographic levels: niveau=1 (5 regioner), niveau=2 (11 landsdele), niveau=3 (99 kommuner). Always filter d.niveau to avoid double-counting.
- In neet1/neet2, statusneet='0' is the all-persons total (active + NEET). Filter to statusneet='10' for NEET-only counts. Similarly, kon='TOT' and socio='TOT'/alder='IALT' are row totals — filter all of them to avoid inflated counts.
- laby10 contains percentages — do not sum rows. neet1/neet2 contain counts (Antal) — these can be summed within a single hierarchy level.
- Map: neet1, neet2, ligeai6 support choropleth maps via context/geo/kommuner.parquet (niveau 3), landsdele.parquet (niveau 2), or regioner.parquet (niveau 1) — merge on bopomr=dim_kode. laby10 supports commune-level maps via context/geo/kommuner.parquet — merge on komgrp=dim_kode (niveau=2 only).