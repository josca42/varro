table: fact.laby29
description: Beskæftigede lønmodtagere (ultimo november) efter kommunegruppe, branche (DB07), sektor og tid
measure: indhold (unit Antal)
columns:
- komgrp: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner, 950=Uden for Danmark]
- branche07: join dim.db on branche07=kode::text
- sektor: values [1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- komgrp is an inline dimension: 0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner, 950=Uden for Danmark. No TOT — filter to komgrp=0 for national total.
- branche07 uses DB07-37-group letter codes (A, B, CA...) — does NOT join dim.db. Use ColumnValues("laby29", "branche07") for labels.
- sektor: inline codes, same as ras305 (1015-1050). No total code.
- No gender or age breakdown in this table — use ras307 for sector×branche×gender.
