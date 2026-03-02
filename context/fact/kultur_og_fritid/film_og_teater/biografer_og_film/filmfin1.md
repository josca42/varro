table: fact.filmfin1
description: Finansiering af danske spillefilm efter finansieringstype, nøgletal og tid
measure: indhold (unit -)
columns:
- finanstype: values [FI01=Finansiering i alt, DK, FI02=Offentlig finansiering ekskl. tv-støtte, DK, FI03=Offentlig tv-støtte, DK, FI04=Privat finansiering ekskl. salg af distributionsrettigheder, DK, FI05=Salg af distributionsrettigheder, privat finansiering, DK, FI06=Finansiering i alt, udland, FI07=Offentlig finansiering, udland, FI08=Privat finansiering ekskl. salg af distributionsrettigheder, udland, FI09=Salg af distributionsrettigheder, udland]
- aktp: values [N03=Film (antal), N04=Finansiering (mio. kr.)]
- tid: date range 2010-01-01 to 2023-01-01

notes:
- aktp is a measurement selector. Filter to one: N03=Film (antal), N04=Finansiering (mio. kr.). Never sum across aktp.
- finanstype has two parallel totals — FI01 and FI06 are NOT part of the same hierarchy:
  - FI01 = total DK financing (= FI02+FI03+FI04+FI05)
  - FI06 = total udland financing (= FI07+FI08+FI09)
  FI01+FI06 = grand total (all financing). Do not also include FI02–FI09 when you include FI01 or FI06.
- Use filmfin1 for DK-vs-abroad financing breakdown. Use filmfin2 for breakdown by financing type + audience group (filmfin2 covers the combined total).