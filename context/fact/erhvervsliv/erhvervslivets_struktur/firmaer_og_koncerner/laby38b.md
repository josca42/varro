table: fact.laby38b
description: Generel firmastatistik efter kommunegruppe, branche (DB07 10-grp), firmaets alder og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1]
- branchedb0710: values [TOT=TOT Erhverv i alt, 1=1 Landbrug, skovbrug og fiskeri, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice, 9=9 Offentlig administration, undervisning og sundhed, 10=10 Kultur, fritid og anden service, 11=11 Uoplyst aktivitet]
- firmaalder: values [TOT4=Alder i alt, 0004=0-4 år, 0509=5-9 år, 1000=10 år og derover]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper niveau 1 (5 groups: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). Unmatched: 0 = "Hele landet" (national aggregate) and 995 = "Uoplyst kommunegruppe". Filter `WHERE komgrp NOT IN (0, 995)` for clean group-level queries, or use komgrp=0 for national total.
- firmaalder has 4 values: TOT4 (total), 0004 (0–4 år), 0509 (5–9 år), 1000 (10+ år). Filter to TOT4 for totals; never sum all four.
- branchedb0710 is inline (TOT + 1–11). No dim join needed.
- indhold is always a firm count (Antal) — no separate enhed selector.