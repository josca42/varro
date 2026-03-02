table: fact.filmomk1
description: Omkostninger til produktion af danske spillefilm efter nøgletal, målgruppe og tid
measure: indhold (unit -)
columns:
- aktp: values [N00=Alle omkostninger (mio. kr.), N01=Lønomkostninger (mio. kr.), N02=Øvrige omkostninger (mio. kr.), N03=Film (antal)]
- mlgrp: values [M00=Alle publikumsgrupper, M01=Børn/unge/familie, M02=Voksne]
- tid: date range 2010-01-01 to 2023-01-01

notes:
- aktp is a measurement selector. Filter to one. N00=N01+N02 (all costs = salary + other). N03=Film count is a separate metric. Never sum across aktp.
- mlgrp: M00=Alle as total; M01+M02 add up to M00.