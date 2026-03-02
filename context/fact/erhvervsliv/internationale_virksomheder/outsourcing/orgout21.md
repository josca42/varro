table: fact.orgout21
description: Outsourcede job fra Danmark til udlandet efter branche (DB07 10-grp.), jobtype og tid
measure: indhold (unit Antal)
columns:
- branche0710: values [TOT=TOT Erhverv i alt, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice]
- jobtyp: values [IS_LOST=Outsourcede job i alt, IS_LOST_HIGH=Outsourcede højtkvalificerede job]
- tid: date range 2009 to 2024

notes:
- tid is int4range (survey waves). The 4 periods are [2009,2012), [2014,2017), [2018,2021), [2021,2024). Filter with: WHERE tid = '[2021,2024)'::int4range
- jobtyp: IS_LOST_HIGH (high-skilled jobs) is a subset of IS_LOST (all outsourced jobs). Don't sum them — that would double-count high-skilled jobs.
- branche0710: sectors 2–8 sum to TOT. Filter to TOT for national total, or exclude TOT when grouping by sector.