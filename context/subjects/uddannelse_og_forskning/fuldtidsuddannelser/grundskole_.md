<fact tables>
<table>
id: uddakt20
description: Uddannelsesaktivitet i grundskolen efter uddannelse, alder, herkomst, national oprindelse, køn, grundskoleinstitutionstype, bopælsområde, status og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, grundskol, bopomr, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: special1
description: Elever, grundskolen efter klassetrin, skoletype, specialundervisning, herkomst, køn og tid
columns: klasse, sktpe, elev, herkomst, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: special2
description: Elever, grundskolen efter klassetrin, specialundervisning, herkomst, køn og tid
columns: klasse, elev, herkomst, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: special3
description: Elever, grundskolen (efterskoler) efter specialundervisning og tid
columns: elev, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2023-01-01
</table>
<table>
id: kvotien
description: Klassekvotienter i grundskolen efter område, klassetrin, skoletype og tid
columns: omrade, klasse, sktpe, tid (time), indhold (unit Kvotienter)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: laby23
description: Uddannelsesaktivitet i grundskolen (antal) efter status, uddannelse, grundskoleinstitutionstype, kommunegruppe og tid
columns: fstatus, uddannelse, grundskol, komgrp, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: laby23a
description: Uddannelsesaktivitet i grundskolen pr. 1. oktober (andel i procent) efter kommunegruppe, grundskoleinstitutionstype og tid
columns: komgrp, grundskol, tid (time), indhold (unit Andel i pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: laby47
description: Andel af børn i grundskolen, som har mindre end 2 km til skole efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Pct.)
tid range: 2008-01-01 to 2021-01-01
</table>
<table>
id: ligeui4
description: Ligestillingsindikator for modtagere af specialundervisning i grundskolen (offentlige skoler og specialområdet) efter indikator, klassetrin, herkomst og tid
columns: indikator, klasse, herkomst, tid (time), indhold (unit -)
tid range: 2011-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For elever by klassetrin, herkomst, køn, skoletype, and bopælsregion/kommune: use uddakt20 (2005–2024). Most comprehensive — covers all dimensions. Always filter fstatus (B/F/T) and all other non-target dimensions to totals.
- For specialundervisning breakdown: special1 has both skoletype and specialundervisning intensity (0/2/3/4/5/6 timer), special2 is simpler (all skoler, fewer elev categories), special3 covers only efterskoler. All three start 2011.
- For class sizes (kvotienter): use kvotien (2009–2024). indhold is a ratio — do not sum, use AVG or report per area.
- For kommunegruppe-level counts by status/uddannelse/skoletype: use laby23 (2007–2024). For the equivalent as percentages: use laby23a (also 2007–2024, simpler).
- For school proximity (share of children within 2 km of school): use laby47 (2008–2021, kommunegrupper only, ends 2021).
- For gender gap in specialundervisning rates: use ligeui4 (2011–2024). Values are percentages/percentage-points — never sum. Covers only public schools.
- fstatus='B' (elever pr. 1. oktober) is the standard headcount. fstatus='F' and 'T' are completions and new entrants. Most questions want fstatus='B'.
- Map: uddakt20 (bopomr) and kvotien (omrade) support choropleth maps via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1). Merge on column=dim_kode. Exclude code 0.
- herkomst coding is inconsistent across tables: uddakt20/special1/2 use 5=dansk, 4=indvandrere, 3=efterkommere; ligeui4 uses 10/20/30. Check before joining or comparing.
- Totals for grundskol use different codes: '0' in uddakt20/kvotien, 'TOT' in laby23/laby23a. Check the column values before filtering.