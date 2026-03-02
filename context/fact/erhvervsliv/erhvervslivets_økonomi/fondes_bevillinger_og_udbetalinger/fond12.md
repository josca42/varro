table: fact.fond12
description: Bevilligede fondsmidler til sociale formål efter fondstype, målgruppe, hovedområder og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- mlgrp: values [1800=Indsatser rettet mod børn, 1805=Indsatser rettet mod voksne, 1810=Indsatser rettet mod ældre, 1812=Indsatser rettet mod familier, 1815=Ikke fordelt]
- homr: values [1900=Målrettet personer med handikap, 1905=Målrettet socialt udsatte, 1920=Øvrige hovedområder, 1925=Andre sociale formål]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- mlgrp and homr are two independent classification dimensions. Neither has a total/aggregate row.
- The mlgrp × homr cross is SPARSE — not all combinations exist. For example, mlgrp=1815 (ikke fordelt) only appears with homr=1925 (andre sociale formål); mlgrp=1800/1805 only appear with homr=1900/1905/1920. Do not assume a full cross-product.
- Some mlgrp/homr combinations also have partial time coverage (fewer years), so GROUP BY tid may produce uneven series.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.