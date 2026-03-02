table: fact.idrfu16
description: Idrætsforbrug efter forbrugsgruppe, region og tid
measure: indhold (unit -)
columns:
- konsumgrp: values [213=Husstande i undersøgelsen (Antal), 214=Hustande i Danmark (1.000 stk.), 1000=FORBRUG I ALT (kr.), SPORT=IDRÆTSFORBRUG I ALT (kr.)]
- cl_region: values [2001=Gennemsnitshusstand, 6010=Region Hovedstaden, 6020=Region Sjælland, 6030=Region Syddanmark, 6040=Region Midtjylland, 6050=Region Nordjylland]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- konsumgrp mixes incompatible value types — always filter to a single value. Available: 213=antal husstande i undersøgelsen, 214=husstande i Danmark (1.000 stk.), 1000=samlet forbrug i alt (kr.), SPORT=idrætsforbrug i alt (kr.).
- cl_region=2001 is Gennemsnitshusstand (the national average, not a region). Actual regions are 6010-6050 (5 regions). Exclude 2001 when summing or comparing regions.
- For regional sports expenditure: filter konsumgrp='SPORT', then GROUP BY cl_region WHERE cl_region != '2001'.
