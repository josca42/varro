table: fact.selsk3
description: Selskabsskat fordelt - DB07 efter branche, indkomst og skat og tid
measure: indhold (unit -)
columns:
- branche: values [501=I alt, 502=Landbrug, skovbrug og fiskeri, 503=Råstofindvinding, 504=Industri, 505=Føde-, drikke- og tobaksvareindustri ... 541=Kultur og fritid, 542=Andre serviceydelser, 543=Private husholdninger med ansat medhjælp, 544=Internationale organisationer og ambassader, 545=Uoplyst aktivitet]
- indskat: values [301=Antal selskaber, 302=Skattepligtig indkomst (mio. kr.), 303=Selskabsskat (mio. kr.)]
- tid: date range 1996-01-01 to 2023-01-01

notes:
- indskat has 3 values with completely different units (same as selsk2): 301=count, 302=income in mio. kr., 303=tax in mio. kr. Always filter to exactly one indskat per query.
- branche=501 (I alt) is the national total across all industries. branche codes follow DB07 (Danish industry classification). Use ColumnValues("selsk3","branche") to browse the ~45 industry codes with labels.
- Same coverage as selsk2 (only skatteydende selskaber), but broken down by DB07 industry instead of company type. Combine with indskat='303' for selskabsskat by industry.
