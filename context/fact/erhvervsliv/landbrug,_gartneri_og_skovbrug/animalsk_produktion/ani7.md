table: fact.ani7
description: Mælkeproduktion og anvendelse efter enhed og tid
measure: indhold (unit -)
columns:
- enhed: values [MALKEKOER=Malkekøer, antal (1000 stk.), MALKEKO=Malkekobesætninger, antal (1000 stk.), MAELK1=Mælk ab landmand i alt (mio. kg), MAELK11=Indvejet mælk på mejerier (mio. kg), OKO=Indvejet økologisk mælk på mejerier (mio. kg.) ... PROD8=Produktion af mælkekonserves (mio. kg), PROD9=Produktion af fedtholdigt mælkepulver i alt (mio. kg), PROD10=Produktion af skummetmælkspulver i alt (mio. kg), PROD11=Produktion af skummetmælkspulver, eksport i alt (mio. kg), RTAL=Prisrelation af mælk/kvægfoderblanding (relationstal)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- `enhed` has 27 distinct values — a pure measurement selector. Every enhed is a different metric with its own unit. Never sum or aggregate across enhed values.
- Measures span: cow and herd counts (MALKEKOER, MALKEKO), milk volumes (MAELK1=ab landmand total, MAELK11=indvejet på mejerier, OKO=organic indvejet), fat% and protein% of intake milk (FMAELK, PMAELK), farm-gate prices (MAELK2, MAELK21), total value (MAELK3 mio.kr), and dairy product output — smør (PROD4), ost (PROD6), mælkekonserves (PROD8), fedtholdigt mælkepulver (PROD9), skummetmælkspulver total/eksport (PROD10, PROD11). RTAL = prisrelation mælk/kvægfoderblanding.
- Annual data (1990-2024). For monthly data from 1995 with 15 of these measures, use ani71.