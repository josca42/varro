table: fact.fond15
description: Bevilligede fondsmidler til uddannelses- og folkeoplysningsformål efter fondstype, hovedområder og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- homr: values [1975=Daginstitutioner, 1980=Grundskolen, 1985=Ungdomsuddannelser, 1995=Videregående uddannelser, 1997=Efteruddannelse, 2000=Folkehøjskoler, 2005=Folkeoplysning]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- homr has 7 leaf-level codes with no aggregate total (verified: sum of all homr ≈ fond01 uddannelse total). All codes can be summed freely.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.