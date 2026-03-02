table: fact.fond01
description: Bevilligede fondsmidler efter fondstype, nøgletal, formål og tid
measure: indhold (unit -)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- aktp: values [1100=Bevillinger (antal), 1105=Bevilgede midler (mio. kr.), 1110=Udbetalte midler (mio. kr.)]
- formal: values [1200=Alle formål, 1205=Videnskabelige formål, 1210=Kulturelle formål, 1215=Sociale formål, 1220=Natur og miljøformål, 1225=Sundhedsformål, 1230=Uddannelse og folkeoplysningsformål, 1235=Erhvervsfremme- og regionaludviklingsformål, 1240=Internationale humanitære formål, 1245=Religiøse formål, 1250=Andre formål]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- aktp is a measurement selector — always filter to one value: 1100=antal bevillinger, 1105=bevilgede midler (mio. kr.), 1110=udbetalte midler (mio. kr.). All three are present for every fondstype/formal/tid combination.
- formal=1200 is the aggregate total across all formål (verified ≈ sum of 1205+...+1250). Filter it out when summing across formål to avoid double-counting.
- fondstype=1000 is the aggregate total of 1005+1010.
- This is the broadest coverage table — the only one with all 11 formål in a single table with antal, bevilget, and udbetalt. Use it for cross-formål comparisons. The topic-specific tables (fond06/12/14/15/16/17/19) provide sub-area breakdowns within individual formål.