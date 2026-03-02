table: fact.byg53
description: Byggeomkostningsindeks for boliger efter hovedindeks, delindeks, art, enhed og tid
measure: indhold (unit -)
columns:
- hindeks: values [1=Byggeomkostningsindeks for boliger, 2=Byggeomkostningsindeks for enfamiliehuse, 3=Byggeomkostningsindeks for etageboliger]
- dindeks: values [10000=Byggeomkostningsindeks i alt, 10010=Jord- og betonarbejde, 10020=Betonelementarbejdet, 10030=Murerarbejdet, 10045=Tømrer- og snedkerarbejde (2015 -), 10060=Malerarbejdet, 10070=VVS-arbejdet, 10080=El-arbejdet, 10090=Undergrund, 10100=Råhus, 10110=Bygningskomplettering, 10115=Overflader (2015 -), 10120=VVS-anlæg, 10130=El- og mekaniske anlæg]
- art: values [1002=I alt, 1004=Materialer, 1006=Arbejdsomkostninger]
- tal: values [100=Indeks, 315=Ændring i forhold til året før (pct.)]
- tid: date range 2003-01-01 to 2024-01-01

notes:
- `tal` is a measurement selector — every hindeks×dindeks×art×tid combination appears twice (100=Indeks, 315=år-over-år pct). Always filter `tal = 100` or `tal = 315`.
- Annual frequency (month 1 only). This is the annual companion to byg43 (quarterly). Same structure and codes — use byg43 if quarterly detail is needed or for current data (byg53 ends 2024).
- Same column hierarchy as byg43: `dindeks=10000` is the total; `hindeks=1` is boliger i alt; `art=1002` is I alt. Filter all three plus `tal` to get a single top-line figure.
- `dindeks` codes 10045 and 10115 only have data from 2015; earlier years will have NULLs for these sub-components.