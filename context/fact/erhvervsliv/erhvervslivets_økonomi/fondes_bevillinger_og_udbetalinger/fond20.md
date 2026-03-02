table: fact.fond20
description: Bevilligede fondsmidler til forskning efter fondstype, fagområde, fondsmidler og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- fagomr: values [1500=Naturvidenskab, 1505=Sundhedsvidenskab, 1510=Teknisk videnskab, 1515=Samfundsvidenskab, 1520=Humaniora, 1525=Jordbrugs- og veterinærvidenskab, 1530=Tværvidenskab]
- fondsmidler: values [4000=Fondsmidler i alt (Mio. kr.), 4005=Konkurrenceudsatte midler (Mio. kr.)]
- tid: date range 2022-01-01 to 2023-01-01

notes:
- fondsmidler is a measurement selector — always filter to one value. Critically: 4005=konkurrenceudsatte midler is a SUBSET of 4000=fondsmidler i alt (verified: 4005 is always smaller than 4000). NEVER sum them — they are not additive.
- fagomr has 7 leaf-level codes with no aggregate total. All can be summed freely.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.
- Only 2 years of data (2022-2023). For a longer research funding series, use fond01 with formal=1205 (videnskabelige formål) back to 2016 — but note fond01 has no fagomr breakdown.