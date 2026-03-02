table: fact.laby48
description: Gennemsnitlig afstand til ungdomsuddannelse efter kommunegruppe, uddannelse og tid
measure: indhold (unit Km)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- uddannelse: values [H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser]
- tid: date range 2008-01-01 to 2021-01-01
dim docs: /dim/kommunegrupper.md

notes:
- laby48 measures average distance in km to the nearest youth education institution — a geographic accessibility table, not enrollment counts. indhold = Km (kilometers).
- komgrp joins dim.kommunegrupper cleanly at niveau=1 (5 groups: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). No unmatched codes.
- uddannelse has only 3 values (H20=Gymnasiale, H29=Erhvervsfaglige grundforløb, H30=Erhvervsfaglige) — no TOT row, so summing or averaging across all three is safe if intended.
- Data covers 2008–2021 only; this table has not been updated past 2021.
- No overcounting risk: the table is already quite thin (5 groups × 3 uddannelser × 14 years = 210 rows total). Just join, filter, and read.