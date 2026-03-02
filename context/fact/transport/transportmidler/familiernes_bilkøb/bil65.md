table: fact.bil65
description: Familiernes bilkøb (andele og fordelinger) efter enhed, uddannelse, købsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 60=Andel af det totale bilkøb]
- uddannelse: values [0=Uddannelse i alt, 10=10 GRUNDSKOLE                                               , 20=20 ALMENGYMNASIAL UDDANNELSER                               , 25=25 ERHVERVSGYMNASIAL UDDANNELSER                            , 30=30 ERHVERVSFAGLIGE GRUNDFORLØB                              , 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 50=50 MELLEMLANGE VIDEREGÅENDE UDDANNELSER                     , 60=60 BACHELOR                                                 , 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 70=70 FORSKERUDDANNELSER                                       , 99=99       UDEN FOR NIVEAU]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- maengde4 is a MEASUREMENT SELECTOR: always filter to 50 (within-education-group %) OR 60 (share of all DK car purchases). Omitting doubles every row.
- koebtype splits series at 2006 same as bil64 (33=1999–2005, 34=2006–2023).
- uddannelse=0 is total; codes 10–70 are flat ISCED levels (safe to sum individually, not sum all).
