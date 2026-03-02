table: fact.affald01
description: Affaldsproduktion efter branche, affaldsfraktion og tid
measure: indhold (unit Ton)
columns:
- erhverv: values [ETOT=Brancher og husholdninger, EHUSHOLD=Husholdninger, EV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- afffrak: values [TOTAFFALD=Affald i alt (inkl. jord), TOTAFFALDX=Affald i alt (ekskl. jord), A=DAGRENOVATION OG LIGNENDE, 101=Dagrenovation og lignende, B=ORGANISK AFFALD, INKL. HAVEAFFALD ... 151=Restprodukter fra forbrænding, 152=Deponeringsegnet, 124=Tekstiler, 125=Blandet emballage, 199=Andet affald]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- Two-dimension version of affald (no behandling). Use when you need waste by industry and fraction without treatment breakdown.
- erhverv and afffrak are both hierarchical — filter to a consistent level. See affald notes for hierarchy details.
- TOTAFFALD includes soil; TOTAFFALDX excludes soil. Use TOTAFFALDX for typical waste statistics.
