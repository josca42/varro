table: fact.phd1
description: Tilgang af studerende, phd uddannelserne efter hovedområder, køn og tid
measure: indhold (unit Antal)
columns:
- homr: values [SUM=I alt, 1=Naturvidenskab, 2=Teknisk videnskab, 3=Sundhedsvidenskab, 4=Jordbrugs- og veterinærvidenskab, 5=Samfundsvidenskab, 6=Humaniora]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 1996-01-01 to 2024-01-01

notes:
- No dimension joins — all columns are inline coded.
- homr includes SUM (I alt, all fields combined) alongside the 6 individual fields (1–6). Never sum across all homr values — either filter to homr='SUM' for a total or filter to homr IN ('1','2','3','4','5','6') and group.
- koen includes TOT (I alt) alongside M and K. Same pattern — filter to koen='TOT' for a gender-neutral total or use M/K individually.
- To get annual new enrolments by subject: WHERE koen='TOT' AND homr != 'SUM'
- To get a single national total for a year: WHERE koen='TOT' AND homr='SUM'