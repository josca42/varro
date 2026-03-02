table: fact.ani71
description: Mælkeproduktion og anvendelse efter enhed og tid
measure: indhold (unit -)
columns:
- maengde4: values [MAELK1=Mælk ab landmand i alt (mio. kg), MAELK11=Indvejet mælk på mejerier (mio. kg), OKO=Indvejet økologisk mælk på mejerier (mio. kg.), FMAELK=Gennemsnitligt fedtprocent i den indvejet mælk på mejerier (procent), PMAELK=Gennemsnitligt proteinprocent i den indvejet mælk på mejerier (procent), MAELK2=Mælk ab landmand i alt (øre pr. kg), MAELK21=Mælk ab landmand med 4,2% fedt og 3,4% protein (øre pr. kg), MAELK3=Mælk ab landmand i alt (mio. kr.), PROD4=Produktion af smør i alt (mio. kg), PROD6=Produktion af ost i alt (mio. kg), PROD8=Produktion af mælkekonserves (mio. kg), PROD9=Produktion af fedtholdigt mælkepulver i alt (mio. kg), PROD10=Produktion af skummetmælkspulver i alt (mio. kg), PROD11=Produktion af skummetmælkspulver, eksport i alt (mio. kg), RTAL=Prisrelation af mælk/kvægfoderblanding (relationstal)]
- tid: date range 1995-01-01 to 2025-08-01

notes:
- The dimension column is named `maengde4` (not `enhed` as in ani7). It functions identically as a measurement selector — always filter to exactly one maengde4.
- Contains 15 measures — a subset of ani7's 27 annual measures. Missing from ani71: cow counts (MALKEKOER, MALKEKO) and some less common series. Present: MAELK1, MAELK11, OKO, FMAELK, PMAELK, MAELK2, MAELK21, MAELK3, PROD4, PROD6, PROD8, PROD9, PROD10, PROD11, RTAL.
- Monthly data (1995-2025). For annual data back to 1990 or measures not in ani71, use ani7.