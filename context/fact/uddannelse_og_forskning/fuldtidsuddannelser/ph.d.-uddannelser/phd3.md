table: fact.phd3
description: Bestand af studerende, phd uddannelserne efter hovedområder, køn og tid
measure: indhold (unit Antal)
columns:
- homr: values [SUM=I alt, 1=Naturvidenskab, 2=Teknisk videnskab, 3=Sundhedsvidenskab, 4=Jordbrugs- og veterinærvidenskab, 5=Samfundsvidenskab, 6=Humaniora]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 1996-01-01 to 2024-01-01

notes:
- No dimension joins — all columns are inline coded. Same structure as phd1 and phd2.
- homr: SUM=I alt (total), 1–6 are individual scientific fields. Filter homr='SUM' for a national total or restrict to individual fields to avoid double-counting.
- koen: TOT=I alt, M=Mænd, K=Kvinder. Filter koen='TOT' unless breaking down by gender.
- indhold counts enrolled PhD students at a point in time (bestand/stock), not intake or degrees — phd3 values are substantially larger than phd1/phd2 for the same year.