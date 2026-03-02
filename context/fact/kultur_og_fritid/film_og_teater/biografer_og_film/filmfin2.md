table: fact.filmfin2
description: Finansiering af danske spillefilm efter finansieringstype, målgruppe, nøgletal og tid
measure: indhold (unit -)
columns:
- finanstype: values [F00=Finansiering i alt, F01=Offentlig finansiering ekskl. tv-støtte, F02=Privat finansiering ekskl. salg af distributionsrettigheder, F03=Offentlig tv-støtte, F04=Salg af distributionsrettigheder]
- mlgrp: values [M00=Alle publikumsgrupper, M01=Børn/unge/familie, M02=Voksne]
- aktp: values [N03=Film (antal), N04=Finansiering (mio. kr.)]
- tid: date range 2010-01-01 to 2023-01-01

notes:
- aktp is a measurement selector. Filter to one: N03=Film (antal), N04=Finansiering (mio. kr.).
- finanstype: F00 = total (= F01+F02+F03+F04). Single-level hierarchy — F01–F04 do not nest further.
- mlgrp: M00=Alle as total; M01+M02 add up to M00.
- filmfin2 covers combined DK+udland financing (F00 ≈ filmfin1's FI01+FI06 grand total) split by financing type and audience group. filmfin1 instead splits by DK-vs-abroad origin within each financing type.