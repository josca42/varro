table: fact.affald
description: Affaldsproduktion efter branche, behandlingsform, affaldsfraktion og tid
measure: indhold (unit Ton)
columns:
- erhverv: values [ETOT=Brancher og husholdninger, EHUSHOLD=Husholdninger, EV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering, SPEC=Særlig behandling, MIDOP=Midlertidig oplagring]
- afffrak: values [TOTAFFALD=Affald i alt (inkl. jord), TOTAFFALDX=Affald i alt (ekskl. jord), A=DAGRENOVATION OG LIGNENDE, 101=Dagrenovation og lignende, B=ORGANISK AFFALD, INKL. HAVEAFFALD ... 151=Restprodukter fra forbrænding, 152=Deponeringsegnet, 124=Tekstiler, 125=Blandet emballage, 199=Andet affald]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- Three dimensions with hierarchical codes — all three need careful filtering to avoid double-counting.
- erhverv (226 codes): ETOT=total (industries+households), EHUSHOLD=households, EV=industries total, VA/VB/...=sector letters, V01000/V010000/...=specific NACE codes at two sub-levels. For top-level splits use ETOT, EHUSHOLD, EV; for sector breakdown use sector letters (VA, VB...); avoid mixing levels.
- afffrak (47 codes): TOTAFFALD=total incl. soil, TOTAFFALDX=total excl. soil, letter codes A–X=major categories, numeric 101–199=sub-fractions. Major categories are sums of their numeric sub-fractions — don't mix levels.
- behandling (6 values): TOT=total, GENANV, FORBRND, DEPOT, SPEC, MIDOP. Filter behandling=TOT for total waste produced; filter to individual method for treatment-type breakdown.
- Most complete affald table (all 3 dimensions). Use affald01/02/03 if you only need 2 dimensions and want simpler queries.
