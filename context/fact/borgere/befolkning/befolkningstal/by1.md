table: fact.by1
description: Befolkningen 1. januar efter byområder og landdistrikter, alder, køn og tid
measure: indhold (unit Antal)
columns:
- byer: values [1100=000-01100 Hovedstadsområdet, 10100101=101-00101 Københavns Kommune, 10101100=101-01100 København (del af Hovedstadsområdet), 10199999=101-99999 Landdistrikter, 14700147=147-00147 Frederiksberg Kommune ... 86018377=860-18377 Lørslev, 86018378=860-18378 Tårs, 86018403=860-18403 Rakkeby, 86099997=860-99997 Uden fast bopæl, 86099999=860-99999 Landdistrikter]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- kon: values [1=Mænd, 2=Kvinder]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- byer uses a compound coding scheme: codes like 10101100 encode municipality (101) + urban area (01100). Codes like 1100 are aggregate summaries (Hovedstadsområdet). Summing all byer values will double-count since aggregate codes overlap with their constituent urban areas.
- No total rows for alder (individual years 0–125) or kon (only 1=Mænd, 2=Kvinder, no TOT). Sum both kon values for total; sum alder range for age groups.
- 1843 distinct byer codes. Use ColumnValues("by1", "byer") to browse. For population of specific city areas, filter to the named byer code.
- Use for sub-municipality urban area detail. For municipality-level data use folk1a or by2.