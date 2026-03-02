table: fact.kv2nyh1
description: Forbrug af nyheder efter adgang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- adgang: values [40260=TV, pc, tablet eller smartphone, 40270=Trykte aviser, 40280=Sociale medier, 40290=Netaviser eller nyhedsapps, 40300=Radio, 40310=Podcast, 40320=Via venner, bekendte eller familie, 40330=Fra influencere eller blogs, 41880=Andre adgange]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder1: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is Pct. of people who access news via each channel.
- adgang values are NOT mutually exclusive — a person can use multiple channels. The 9 adgang values sum to 293% for koen='10'/alder1='TOT'. Never sum across adgang; each row is an independent percentage.
- koen='10' = Køn i alt (total); alder1='TOT' = Alder i alt (total). Filter to these for overall rates.
- Note: the age column is named alder1 here (not alder as in kv2nyh2-4).