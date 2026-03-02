<fact tables>
<table>
id: genmf10
description: Gennemførsel af uddannelsesgrupper efter startuddannelse i gruppen, herkomst, køn, status ved 1 og 5 år, alder ved start på gruppe og tid
columns: startud, herkomst, kon, stat, startald, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ligeub5
description: Gennemførsel af uddannelsesgrupper efter startuddannelse i gruppen, herkomst, køn, status ved 1 og 5 år, alder ved start på gruppe og tid
columns: startud, herkomst, kon, stat, startald, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ligeui5
description: Ligestillingsindikator for frafald inden for 5 år efter startuddannelse i gruppen, indikator, alder, herkomst og tid
columns: startud, indikator, alerams, herkomst, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2019-01-01
</table>
</fact tables>

notes:
- All three tables track 5-year cohort outcomes (fuldførelse/frafald) for students starting a sequence of education. The shared stat column is key: 1-year statuses (0–4) and 5-year statuses (5–8) each independently sum to TOT. Never sum all stat values — use stat='TOT' for cohort size, or filter to one group.
- For detailed education breakdown (down to individual programmes): use genmf10. startud has 3 hierarchy levels (TOT → H21/H31/... → 5-char sub-types → 7-char programmes). Filter to one level by LENGTH(startud). genmf10 is the only clean table (no duplicate rows).
- For western/non-western herkomst split: use ligeub5 or ligeui5. genmf10 only distinguishes dansk/indvandrere/efterkommere at the top level. Note that ligeub5 has ~35k duplicate rows — always aggregate with MAX(indhold).
- For pre-computed gender gap in dropout rates: use ligeui5 (LA3 = dropout gap in percentage points between men and women). But ligeui5 only goes to 2019. For current data (to 2024), compute the gap yourself from genmf10 or ligeub5.
- herkomst total codes differ across tables: 'TOT' in genmf10, '0' (integer) in ligeub5 and ligeui5. kon total also differs: '10' in genmf10, 'TOT' in ligeub5.
- ligeub5 startud is top-level only (H21–H80). For sub-level education breakdown, genmf10 is the only option.
- ligeui5 data quality: ~4k duplicate rows with conflicting values; use aggregation.