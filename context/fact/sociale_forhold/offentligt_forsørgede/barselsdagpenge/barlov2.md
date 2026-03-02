table: fact.barlov2
description: Samboende forældre på barselsorlov i barnets første leveår (børn født 2. august - 31. december) efter enhed, berettigelse, mors uddannelse, fars uddannelse, uger og tid
measure: indhold (unit Antal)
columns:
- tal: values [225=Mor - i alt, 226=Mor - øremærket orlov, 227=Mor - ikke øremærket orlov, 228=Mor - uspecificeret orlov, 325=Far - i alt, 326=Far - øremærket orlov, 327=Far - ikke øremærket orlov, 328=Far - uspecificeret orlov]
- beret: values [203=Far holdt barselsorlov, 330=Mor holdt barselsorlov, 633=Både mor og far holdt barseslsorlov, 635=Mor holdt barselsorlov, far holdt ikke barselsorlov, 639=Mor holdt barselsorlov, far er ikke berettiget til barselsdagpenge, 653=Mor holdt ikke barselsorlov, far holdt barselsorlov, 793=Mor er ikke berettiget, far holdt barselsorlov]
- morud: values [2=Alle mødre uanset uddannelse, 120=Mor har ingen ungdomsuddannelse, 130=Mor har ungdomsuddannelse, 150=Mor har kort videregående uddannelse (KVU), 160=Mor har mellemlang videregående uddannelse (MVU), 170=Mor har lang videregående uddannelse (LVU)]
- farud: values [4=Alle fædre uanset uddannelse, 220=Far har ingen ungdomsuddannelse, 230=Far har ungdomsuddannelse, 250=Far har kort videregående uddannelse (KVU), 260=Far har mellemlang videregående uddannelse (MVU), 270=Far har lang videregående uddannelse (LVU)]
- uger: values [U00=Uge 0, U01=Uge 1, U02=Uge 2, U03=Uge 3, U04=Uge 4 ... U48=Uge 48, U49=Uge 49, U50=Uge 50, U51=Uge 51, U52=Uge 52]
- tid: date range AUG - DEC 2019 to AUG - DEC 2023

notes:
- `tal` is a measurement selector (8 values: mor/far × i alt/øremærket/ikke-øremærket/uspecificeret). Always filter to one value. Do not mix mor-values and far-values.
- `uger` (U00–U52) shows the week of the child's first year the leave was taken. `U00` = week 0 (birth week). To get the total (regardless of which week), filter `uger='U00'` only if that column stores cumulative totals — otherwise sum across all `uger` values. Use `ColumnValues("barlov2", "uger")` to verify structure.
- `beret` has no "all parents" total — only codes for parents who actually took leave. Sum across beret codes will double-count (codes overlap).
- `morud` total is `'2'`, `farud` total is `'4'`. No regional breakdown — use barlov3 for region by week.
- Coverage same as barlov1: Aug–Dec birth cohorts, 2019–2023.