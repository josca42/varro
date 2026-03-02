table: fact.fond03
description: Bevilligede fondsmidler efter fondstype, modtagertype, formål og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- modtag: values [1400=Alle modtagere, 1405=Offentlige institutioner, 1410=Individuelle personer, 1415=Private virksomheder mv, 1420=Non-profit organisationer, 1425=Interne donationer, 1430=Andet, 1435=Ikke fordelt]
- formal: values [1200=Alle formål, 1205=Videnskabelige formål, 1210=Kulturelle formål, 1215=Sociale formål, 1220=Natur og miljøformål, 1225=Sundhedsformål, 1230=Uddannelse og folkeoplysningsformål, 1235=Erhvervsfremme- og regionaludviklingsformål, 1240=Internationale humanitære formål, 1245=Religiøse formål, 1250=Andre formål]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- modtag=1400 is the aggregate total across all modtagertyper. Filter it out when summing across modtag.
- formal=1200 is the aggregate total across all formål. Filter it out when summing across formål.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr.
- Use this table to break down who receives fund grants: public institutions, individuals, private firms, non-profits, or internal donations.