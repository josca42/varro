table: fact.fond16
description: Bevilligede fondsmidler til erhvervsfremme- og regionaludviklingsformål efter fondstype, hovedområder og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- homr: values [2012=Erhvervsfremme, 2017=Regionaludvikling, 2020=Byudvikling]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- homr has 3 leaf-level codes with no aggregate total (verified: sum ≈ fond01 erhvervsfremme total). All three can be summed freely.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.