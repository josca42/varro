table: fact.byg43
description: Byggeomkostningsindeks for boliger efter hovedindeks, delindeks, art, enhed og tid
measure: indhold (unit -)
columns:
- hindeks: values [1=Byggeomkostningsindeks for boliger, 2=Byggeomkostningsindeks for enfamiliehuse, 3=Byggeomkostningsindeks for etageboliger]
- dindeks: values [10000=Byggeomkostningsindeks i alt, 10010=Jord- og betonarbejde, 10020=Betonelementarbejdet, 10030=Murerarbejdet, 10045=Tømrer- og snedkerarbejde (2015 -), 10060=Malerarbejdet, 10070=VVS-arbejdet, 10080=El-arbejdet, 10090=Undergrund, 10100=Råhus, 10110=Bygningskomplettering, 10115=Overflader (2015 -), 10120=VVS-anlæg, 10130=El- og mekaniske anlæg]
- art: values [1002=I alt, 1004=Materialer, 1006=Arbejdsomkostninger]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2003-01-01 to 2025-04-01

notes:
- `tal` is a measurement selector — every hindeks×dindeks×art×tid combination appears three times (100=Indeks, 210=kvartal-over-kvartal pct, 310=år-over-år pct). Always filter `tal = 100` or the specific change code. Forgetting this triples row counts.
- Quarterly frequency (months 1, 4, 7, 10). Most current and most detailed bolig cost index: quarterly to 2025-Q2.
- 5 dimension columns. To get the top-level quarterly index: `WHERE hindeks = 1 AND dindeks = 10000 AND art = 1002 AND tal = 100`.
- `hindeks`: 1=Boliger i alt (total), 2=Enfamiliehuse, 3=Etageboliger. Do not sum across hindeks.
- `dindeks`: 10000=I alt (total of all sub-components). Do not sum across dindeks — they are subcategories of the total cost. Two codes only exist from 2015: 10045 (Tømrer- og snedkerarbejde) and 10115 (Overflader).
- `art`: 1002=I alt, 1004=Materialer, 1006=Arbejdsomkostninger. 1002 is the total; do not sum across art.