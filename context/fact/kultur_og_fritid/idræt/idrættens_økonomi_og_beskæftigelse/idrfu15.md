table: fact.idrfu15
description: Idrætsforbrug efter forbrugsgruppe, boligform og tid
measure: indhold (unit -)
columns:
- konsumgrp: values [213=Husstande i undersøgelsen (Antal), 214=Hustande i Danmark (1.000 stk.), 1000=FORBRUG I ALT (kr.), SPORT=IDRÆTSFORBRUG I ALT (kr.)]
- bolform: values [2001=Gennemsnitshusstand, 5010=Eget hus, 5020=Egen ejerlejlighed, 5030=Lejet hus, 5040=Lejet lejlighed, 5050=Andelsbolig, 5060=Lejet værelse]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- konsumgrp mixes incompatible value types — always filter to a single value. Available: 213=antal husstande i undersøgelsen, 214=husstande i Danmark (1.000 stk.), 1000=samlet forbrug i alt (kr.), SPORT=idrætsforbrug i alt (kr.).
- The second dimension includes a 2001=Gennemsnitshusstand category which is the cross-group average (same values as idrfu11). For a breakdown by category, exclude 2001 or compare it as a reference.
- For sports expenditure per household type: filter konsumgrp='SPORT' and pick the relevant second-dimension categories.
