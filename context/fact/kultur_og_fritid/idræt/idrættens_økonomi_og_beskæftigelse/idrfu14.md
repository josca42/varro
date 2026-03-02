table: fact.idrfu14
description: Idrætsforbrug efter forbrugsgruppe, samlet indkomst og tid
measure: indhold (unit -)
columns:
- konsumgrp: values [213=Husstande i undersøgelsen (Antal), 214=Hustande i Danmark (1.000 stk.), 1000=FORBRUG I ALT (kr.), SPORT=IDRÆTSFORBRUG I ALT (kr.)]
- samind: values [2001=Gennemsnitshusstand, 4015=Under 250.000 kr., 4025=250.000 - 449.999 kr., 4035=450.000 - 699.999 kr., 4045=700.000 - 999.999 kr., 4055=1.000.000 kr. og derover]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- konsumgrp mixes incompatible value types — always filter to a single value. Available: 213=antal husstande i undersøgelsen, 214=husstande i Danmark (1.000 stk.), 1000=samlet forbrug i alt (kr.), SPORT=idrætsforbrug i alt (kr.).
- The second dimension includes a 2001=Gennemsnitshusstand category which is the cross-group average (same values as idrfu11). For a breakdown by category, exclude 2001 or compare it as a reference.
- For sports expenditure per household type: filter konsumgrp='SPORT' and pick the relevant second-dimension categories.
