table: fact.laby32
description: Huslejeindeks for boliger efter kommunegruppe, enhed og tid
measure: indhold (unit -)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2021-01-01 to 2025-07-01
dim docs: /dim/kommunegrupper.md

notes:
- `tal` is a measurement selector — every komgrp repeats 3 times (100=Indeks, 210=QoQ%, 310=YoY%). Always filter to one value; `tal=100` for index levels.
- `komgrp=0` is the national total and is NOT in dim.kommunegrupper. komgrp 1–5 correspond to niveau=1 groups in dim.kommunegrupper (1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner).
- dim.kommunegrupper also contains niveau=2 individual municipality codes, but laby32 only uses the 5 niveau=1 group codes — do not attempt to join at niveau=2.
- No ejendomskate breakdown — covers all boliger only. Use hus1 if you need to split by ejendomskategori.