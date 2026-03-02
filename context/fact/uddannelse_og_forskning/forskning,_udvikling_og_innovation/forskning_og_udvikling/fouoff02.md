table: fact.fouoff02
description: FoU-årsværk i den offentlige sektor efter sektor, fag, personalekategori, køn og tid
measure: indhold (unit Årsværk)
columns:
- sekvid: values [1000=Sektorer i alt, 1100=Højere læreanstalter, 1200=Øvrige offentlige forskningsinstitutioner, 1300=Sektorforskningsinstitutioner, 1400=Private ikke-erhvervsdrivende institutioner]
- vidomr: values [10=Naturvidenskab, 20=Teknisk videnskab, 30=Sundhedsvidenskab, 40=Jordbrugs- og veterinærvidenskab, 50=Samfundsvidenskab, 60=Humaniora]
- personkat: values [100=Teknisk/administrativt personale, 110=Videnskabeligt personale]
- koen: values [0=Køn i alt, 2=Mænd, 1=Kvinder]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- Identical structure to fouoff01 — same sekvid, vidomr, personkat, koen columns with the same coding. See fouoff01 notes for details on how to filter to avoid overcounting.
- This measures FTE (årsværk). For headcount (Antal), use fouoff01.
- To get total public-sector FoU FTE: WHERE sekvid='1000' AND koen='0', SUM over vidomr and personkat.
