table: fact.affald02
description: Affaldsproduktion efter branche, behandlingsform og tid
measure: indhold (unit Ton)
columns:
- erhverv: values [ETOT=Brancher og husholdninger, EHUSHOLD=Husholdninger, EV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering, SPEC=Særlig behandling, MIDOP=Midlertidig oplagring]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- Two-dimension version of affald (no afffrak). Use when you need waste by industry and treatment method without fraction detail.
- erhverv is hierarchical — filter to a consistent level (ETOT/EV/EHUSHOLD for totals, sector letters for breakdown).
- behandling=TOT is aggregate. Filter to individual methods (GENANV, FORBRND, DEPOT, SPEC, MIDOP) for treatment breakdown, or use TOT for total waste only.
