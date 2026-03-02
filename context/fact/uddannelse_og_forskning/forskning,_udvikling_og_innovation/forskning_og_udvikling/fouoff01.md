table: fact.fouoff01
description: FoU-personale i den offentlige sektor efter sektor, fag, personalekategori, køn og tid
measure: indhold (unit Antal)
columns:
- sekvid: values [1000=Sektorer i alt, 1100=Højere læreanstalter, 1200=Øvrige offentlige forskningsinstitutioner, 1300=Sektorforskningsinstitutioner, 1400=Private ikke-erhvervsdrivende institutioner]
- vidomr: values [10=Naturvidenskab, 20=Teknisk videnskab, 30=Sundhedsvidenskab, 40=Jordbrugs- og veterinærvidenskab, 50=Samfundsvidenskab, 60=Humaniora]
- personkat: values [100=Teknisk/administrativt personale, 110=Videnskabeligt personale]
- koen: values [0=Køn i alt, 2=Mænd, 1=Kvinder]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- This table has 4 classification dimensions (sekvid, vidomr, personkat, koen). To get a single total: WHERE sekvid='1000' AND koen='0', then sum over all vidomr and personkat (no total codes for those two columns).
- sekvid='1000' = Sektorer i alt (total across all public sectors). sekvid 1100–1400 are sub-sectors.
- vidomr has 6 field codes (10–60), no total code — sum all six if you want the combined figure.
- personkat has 2 codes (100=tech/admin, 110=scientific), no total code — sum both if you want combined.
- koen='0' = total; never sum koen=1 and koen=2 and expect to equal koen=0 if some combinations have suppressed gender detail.
- This counts headcount (Antal). For FTE (årsværk), use fouoff02 (identical structure).
