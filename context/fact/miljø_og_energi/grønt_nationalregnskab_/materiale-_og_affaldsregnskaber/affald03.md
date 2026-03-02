table: fact.affald03
description: Affaldsproduktion efter branche, farlighed og tid
measure: indhold (unit Ton)
columns:
- erhverv: values [ETOT=Brancher og husholdninger, EHUSHOLD=Husholdninger, EV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- farlig: values [FARLIG=Farligt affald, IKFARLIG=Ikke-farligt affald, TOTAFFALDX=Affald i alt (ekskl. jord)]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- Two-dimension version of affald: waste by industry and hazard classification.
- farlig has 3 values: FARLIG=hazardous, IKFARLIG=non-hazardous, TOTAFFALDX=total excl. soil. Always filter to one.
- erhverv is hierarchical — filter to consistent level. See affald notes for hierarchy details.
