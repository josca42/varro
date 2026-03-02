table: fact.laby40
description: Kulturministeriets gennemsnitlige udbetalinger til personlige modtagere efter kommunegruppe, kulturemne og tid
measure: indhold (unit kr. pr. modtager)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 12=KULTURARV, 1=MEDIER, BIBLIOTEKER OG LITTERATUR, 20=SCENE OG MUSIK, 23=VISUEL KUNST OG DESIGN, 29=ANDEN KULTUREL AKTIVITET, 99=Uoplyst]
- tid: date range 2018-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- `indhold` is kr. per recipient (average), not total. Do not sum across komgrp codes — that would average the averages, not produce a meaningful total.
- `komgrp` joins dim.kommunegrupper at niveau 1 only: 5 types (Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). Code 0 is national aggregate (not in dim).
- `kulturemne` here uses broad-category codes only (0, 1, 8, 12, 20, 23, 29, 99) — no sub-categories. These do not overlap, so summing across categories (excluding 0) is safe.
- Only available from 2018. For longer disbursement trends use kubs05/kubs06.