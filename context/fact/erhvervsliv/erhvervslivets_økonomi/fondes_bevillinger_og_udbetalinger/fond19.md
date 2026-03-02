table: fact.fond19
description: Bevilligede fondsmidler til natur-, klima- og miljøformål efter fondstype, hovedområder og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- homr: values [4010=Forebyggelse af klimaforandringer i form af CO2 reducerende formål, 4015=Øvrige forbyggende formål af klimaforandringer, 4020=Klimatilpasning, 4025=Affaldshåndtering, 4030=Beskyttelse af vandressourcer, 4035=Naturbeskyttelse, 4040=Andre formål]
- tid: date range 2022-01-01 to 2023-01-01

notes:
- homr has 7 leaf-level codes with no aggregate total (verified: sum ≈ fond01 natur og miljøformål total). All codes can be summed freely.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.
- Only 2 years of data (2022-2023). Use fond01 formal=1220 for longer natur og miljø series back to 2016.