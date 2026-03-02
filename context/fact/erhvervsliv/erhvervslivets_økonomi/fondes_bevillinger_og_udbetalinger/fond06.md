table: fact.fond06
description: Bevilligede fondsmidler til kulturelle formål efter fondstype, hovedområder og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- homr: values [1600=Arkiver, 1605=Fredede bygninger, 1610=Fredede fortidsminder, 1615=Kulturmiljøer / landskaber, 1620=Museer ... 1690=Design, 1695=Kunsthåndværk, 1700=Anden visuel kunst og design (-2022), 1705=Byfester, messer og festivaler (-2022), 1710=Anden kulturel aktivitet]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- homr has 23 leaf-level codes with no aggregate total among them (verified: sum of all homr = fond01 kulturelle total). All codes can be summed freely.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.
- Two codes are marked (-2022): 1700=Anden visuel kunst og design and 1705=Byfester, messer og festivaler, indicating these categories were discontinued after 2022. Filter these out if comparing consistently across years.
- Use ColumnValues("fond06", "homr") to see the full list of 23 cultural sub-areas.