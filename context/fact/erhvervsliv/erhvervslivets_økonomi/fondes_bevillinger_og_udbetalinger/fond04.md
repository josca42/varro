table: fact.fond04
description: Bevilligede fondsmidler efter fondstype, modtagernationalitet, formål og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- modtager: values [1400=Alle modtagere, 1440=Indenlandske modtagere, 1445=Udenlandske modtagere, 1450=Modtagere med ukendt geografi, 1435=Ikke fordelt]
- formal: values [1200=Alle formål, 1205=Videnskabelige formål, 1210=Kulturelle formål, 1215=Sociale formål, 1220=Natur og miljøformål, 1225=Sundhedsformål, 1230=Uddannelse og folkeoplysningsformål, 1235=Erhvervsfremme- og regionaludviklingsformål, 1240=Internationale humanitære formål, 1245=Religiøse formål, 1250=Andre formål]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- modtager=1400 is the aggregate total across all nationaliteter. Filter it out when summing across modtager.
- formal=1200 is the aggregate total across all formål. Filter it out when summing across formål.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.
- Use this table for questions about domestic vs. international grant recipients. Note that 1440+1445+1450+1435 sums to the 1400 total — all four sub-codes are leaf values.