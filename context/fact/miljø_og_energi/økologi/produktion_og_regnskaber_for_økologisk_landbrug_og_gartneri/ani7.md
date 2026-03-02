table: fact.ani7
description: Mælkeproduktion og anvendelse efter enhed og tid
measure: indhold (unit -)
columns:
- enhed: values [MALKEKOER=Malkekøer, antal (1000 stk.), MALKEKO=Malkekobesætninger, antal (1000 stk.), MAELK1=Mælk ab landmand i alt (mio. kg), MAELK11=Indvejet mælk på mejerier (mio. kg), OKO=Indvejet økologisk mælk på mejerier (mio. kg.) ... PROD8=Produktion af mælkekonserves (mio. kg), PROD9=Produktion af fedtholdigt mælkepulver i alt (mio. kg), PROD10=Produktion af skummetmælkspulver i alt (mio. kg), PROD11=Produktion af skummetmælkspulver, eksport i alt (mio. kg), RTAL=Prisrelation af mælk/kvægfoderblanding (relationstal)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a measurement selector with 27 different metrics — never sum across enhed values. Each represents a completely different quantity with different units (1000 stk. for animal counts, mio. kg for milk volumes, relationstal for RTAL). Always filter to a single enhed per query.
- OKO (indvejet økologisk mælk på mejerier) starts from 1993, not 1990. 3 years of data are missing at the start of the series.
- RTAL (prisrelation mælk/kvægfoderblanding) is a ratio index, not a volume — do not sum. Also has some missing years (33 of 35 expected observations).
- PROD2, PROD5, PROD7 have only ~26 observations instead of 35 — gaps in those dairy product series.
- For organic milk volume use enhed='OKO'. No separate organic milk price series exists in this table.