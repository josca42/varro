table: fact.fond02
description: Bevilligede fondsmidler efter fondstype, virkemidler, formål og tid
measure: indhold (unit Mio. kr.)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- virke: values [1300=Alle virkemidler, 1305=Anlæg, 1310=Ikke øremærkede midler, 1315=Anskaffelser/Erhvervelser, 1320=Forskning, 1325=Innovation, 1330=Formidling, 1335=Andet, 1340=Ikke fordelt]
- formal: values [1200=Alle formål, 1205=Videnskabelige formål, 1210=Kulturelle formål, 1215=Sociale formål, 1220=Natur og miljøformål, 1225=Sundhedsformål, 1230=Uddannelse og folkeoplysningsformål, 1235=Erhvervsfremme- og regionaludviklingsformål, 1240=Internationale humanitære formål, 1245=Religiøse formål, 1250=Andre formål]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- virke=1300 is the aggregate total across all virkemidler (verified ≈ sum of 1305+...+1340). Filter it out when summing across virke.
- formal=1200 is the aggregate total across all formål. Filter it out when summing across formål.
- fondstype=1000 is the aggregate total of 1005+1010.
- indhold is always in Mio. kr. (unlike fond01 where unit varies by aktp). No measurement selector — one value type per row.
- Use this table to understand how grants are structured (e.g. how much goes to forskning vs. anlæg vs. innovation) across formål.