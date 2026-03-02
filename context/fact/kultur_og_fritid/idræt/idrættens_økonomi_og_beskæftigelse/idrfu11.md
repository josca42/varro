table: fact.idrfu11
description: Idrætsforbrug for en gennemsnitshusstand efter forbrugsgruppe og tid
measure: indhold (unit -)
columns:
- konsumgrp: values [213=Husstande i undersøgelsen (Antal), 214=Hustande i Danmark (1.000 stk.), 1000=FORBRUG I ALT (kr.), SPORT=IDRÆTSFORBRUG I ALT (kr.), IDRFU1=Tøj og sko (kr.), IDRFU2=Sportsudstyr (kr.), IDRFU3=Tipning, odds og spil (kr.), IDRFU4=Medlemskab og entre (kr.)]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- konsumgrp mixes incompatible value types — do not sum across it. Values: 213=antal husstande i undersøgelsen, 214=husstande i Danmark (1.000 stk.), 1000=samlet forbrug i alt (kr.), SPORT=idrætsforbrug i alt (kr.), IDRFU1-4 are subcategories of SPORT (tøj/sko, sportsudstyr, tipning/spil, medlemskab/entre).
- IDRFU1+IDRFU2+IDRFU3+IDRFU4 sums to SPORT. SPORT is a subcategory of 1000. Filter to a single konsumgrp per query.
- This table has no demographic breakdown — it covers the average household (gennemsnitshusstand). For demographic breakdowns use idrfu12 (socioøkonomisk status), idrfu13 (husstandstype), idrfu14 (indkomst), idrfu15 (boligform), idrfu16 (region), idrfu17 (alder).
- The idrfu12-17 tables only have top-level konsumgrp values (213, 214, 1000, SPORT) — subcategory breakdown (IDRFU1-4) is only in idrfu11.
