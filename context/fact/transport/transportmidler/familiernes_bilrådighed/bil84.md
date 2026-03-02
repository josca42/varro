table: fact.bil84
description: Familiernes bilrådighed (faktiske tal) efter bestand, uddannelse, rådighedsmønster og tid
measure: indhold (unit Antal)
columns:
- bestand: values [53=Bestand (E-familier 2007 - ), 73=Bestand (C-familier 2000 - 2006)]
- uddannelse: values [0=Uddannelse i alt, 10=10 GRUNDSKOLE                                               , 20=20 ALMENGYMNASIAL UDDANNELSER                               , 25=25 ERHVERVSGYMNASIAL UDDANNELSER                            , 30=30 ERHVERVSFAGLIGE GRUNDFORLØB                              , 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 50=50 MELLEMLANGE VIDEREGÅENDE UDDANNELSER                     , 60=60 BACHELOR                                                 , 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 70=70 FORSKERUDDANNELSER                                       , 99=99       UDEN FOR NIVEAU]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2024-01-01
notes:
- bestand is a methodology selector: 53=E-familier (2007+), 73=C-familier (2000-2006). Filter to one value — never mix or aggregate across both.
- uddannelse=0 is the total ("Uddannelse i alt"). Individual education levels (10-99) sum to 0. Codes have trailing whitespace in the database.
- raadmoens is hierarchical — pick one level. See bil800 for hierarchy.
