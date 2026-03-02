<fact tables>
<table>
id: phd1
description: Tilgang af studerende, phd uddannelserne efter hovedområder, køn og tid
columns: homr, koen, tid (time), indhold (unit Antal)
tid range: 1996-01-01 to 2024-01-01
</table>
<table>
id: phd2
description: Tildelte phd grader efter hovedområder, køn og tid
columns: homr, koen, tid (time), indhold (unit Antal)
tid range: 1996-01-01 to 2024-01-01
</table>
<table>
id: phd3
description: Bestand af studerende, phd uddannelserne efter hovedområder, køn og tid
columns: homr, koen, tid (time), indhold (unit Antal)
tid range: 1996-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Three tables covering the same 1996–2024 annual series with the same dimensions (homr, koen) but measuring different things: phd1=new enrolments (tilgang), phd2=degrees awarded (tildelte grader), phd3=enrolled headcount at year-end (bestand). Pick based on the question.
- All three tables share the same homr coding: SUM=I alt, 1=Naturvidenskab, 2=Teknisk videnskab, 3=Sundhedsvidenskab, 4=Jordbrugs- og veterinærvidenskab, 5=Samfundsvidenskab, 6=Humaniora.
- Always filter both homr and koen to avoid double-counting aggregate rows. Use homr='SUM' AND koen='TOT' for a national total, or restrict homr to individual fields (1–6) and koen to M/K when breaking down by subject or gender.