table: fact.idrfu13
description: Idrætsforbrug efter forbrugsgruppe, husstand og tid
measure: indhold (unit -)
columns:
- konsumgrp: values [213=Husstande i undersøgelsen (Antal), 214=Hustande i Danmark (1.000 stk.), 1000=FORBRUG I ALT (kr.), SPORT=IDRÆTSFORBRUG I ALT (kr.)]
- husstand: values [2001=Gennemsnitshusstand, 2010=Enlige under 60 år uden børn, 2020=Enlig 60 år og over uden børn, 2030=Enlige med børn, 2040=2 voksne, hovedperson under 60 år uden børn, 2050=2 voksne, hovedperson 60 år og over uden børn, 2060=2 voksne med børn, 2070=Husstande med mindst 3 voksne]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- konsumgrp mixes incompatible value types — always filter to a single value. Available: 213=antal husstande i undersøgelsen, 214=husstande i Danmark (1.000 stk.), 1000=samlet forbrug i alt (kr.), SPORT=idrætsforbrug i alt (kr.).
- The second dimension includes a 2001=Gennemsnitshusstand category which is the cross-group average (same values as idrfu11). For a breakdown by category, exclude 2001 or compare it as a reference.
- For sports expenditure per household type: filter konsumgrp='SPORT' and pick the relevant second-dimension categories.
