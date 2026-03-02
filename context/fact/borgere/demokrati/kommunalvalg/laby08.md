table: fact.laby08
description: Valg til kommunalbestyrelser efter kommunegruppe, valgresultat og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1, 2]
- valres: values [STEMPCT=Stemmeprocent, UGYLPCT=Ugyldighedsprocent, BREVPCT=Brevstemmeprocent, BLANKPCT=Blank stemmeprocent, PERSPCT=Personlig stemmeprocent]
- tid: date range 2005-01-01 to 2021-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper approximately. Two levels present: niveau 1 = 5 type groups (Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner); niveau 2 = individual kommuner within each group. Code '0' = national aggregate, not in dim. Filter d.niveau to pick one level; mixing doubles data.
- valres has 5 percentage measures: STEMPCT (turnout), UGYLPCT (invalid), BREVPCT (postal), BLANKPCT (blank), PERSPCT (personal vote share). All are independent rates — never sum across valres values. Always filter to the rate you want.
- Use ColumnValues("kommunegrupper", "titel", for_table="laby08") to see which groups and kommuner are present.