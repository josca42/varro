table: fact.idrfu12
description: Idrætsforbrug efter forbrugsgruppe, socioøkonomisk status og tid
measure: indhold (unit -)
columns:
- konsumgrp: values [213=Husstande i undersøgelsen (Antal), 214=Hustande i Danmark (1.000 stk.), 1000=FORBRUG I ALT (kr.), SPORT=IDRÆTSFORBRUG I ALT (kr.)]
- socio: values [2001=Gennemsnitshusstand, 3010=Selvstændig, 3020=Lønmodtager på højeste niveau, 3030=Lønmodtager på mellemniveau, 3040=Lønmodtager på grundniveau, 3050=Arbejdsløs, 3060=Uddannelsessøgende, 3070=Pensionist,efterlønmodtager, 3080=Ude af erhverv i øvrigt]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- konsumgrp mixes incompatible value types — always filter to a single value. Available: 213=antal husstande i undersøgelsen, 214=husstande i Danmark (1.000 stk.), 1000=samlet forbrug i alt (kr.), SPORT=idrætsforbrug i alt (kr.).
- The second dimension includes a 2001=Gennemsnitshusstand category which is the cross-group average (same values as idrfu11). For a breakdown by category, exclude 2001 or compare it as a reference.
- For sports expenditure per household type: filter konsumgrp='SPORT' and pick the relevant second-dimension categories.
