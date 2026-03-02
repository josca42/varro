table: fact.bil85
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, uddannelse, rådighedsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 70=Andel af den totale bilrådighed]
- uddannelse: values [0=Uddannelse i alt, 10=10 GRUNDSKOLE                                               , 20=20 ALMENGYMNASIAL UDDANNELSER                               , 25=25 ERHVERVSGYMNASIAL UDDANNELSER                            , 30=30 ERHVERVSFAGLIGE GRUNDFORLØB                              , 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 50=50 MELLEMLANGE VIDEREGÅENDE UDDANNELSER                     , 60=60 BACHELOR                                                 , 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 70=70 FORSKERUDDANNELSER                                       , 99=99       UDEN FOR NIVEAU]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2024-01-01
notes:
- maengde4 doubles all rows — always filter to one value: 50=Procentfordelingen, 70=Andel af den totale bilrådighed. Values are Pct.; do not SUM.
- uddannelse=0 is the total. See bil84 notes.
- raadmoens is hierarchical — pick one level.
