table: fact.bil64
description: Familiernes bilkøb (faktiske tal) efter købstype, uddannelse, købsmønster og tid
measure: indhold (unit Antal)
columns:
- koebtype: values [34=Nye biler (2006 - ), 33=Nye biler (1999 - 2005)]
- uddannelse: values [0=Uddannelse i alt, 10=10 GRUNDSKOLE                                               , 20=20 ALMENGYMNASIAL UDDANNELSER                               , 25=25 ERHVERVSGYMNASIAL UDDANNELSER                            , 30=30 ERHVERVSFAGLIGE GRUNDFORLØB                              , 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 50=50 MELLEMLANGE VIDEREGÅENDE UDDANNELSER                     , 60=60 BACHELOR                                                 , 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 70=70 FORSKERUDDANNELSER                                       , 99=99       UDEN FOR NIVEAU]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- koebtype splits the time series at a methodology break: 33=Nye biler (1999–2005), 34=Nye biler (2006–2023). Unlike bil62 the break is at 2006 (not 2007), and transition years 2005–2006 appear in both koebtype with very small values for the non-primary series (~59 rows) — these are incomplete/test data. Use 33 for 1999–2005 and 34 for 2006+ exclusively.
- uddannelse=0 is the total. Codes 10–70 are standard ISCED levels (grundskole through forsker). Code 99=uden for niveau (outside classification). These are mutually exclusive flat codes — no hierarchy, safe to sum a subset.
- koebmoens same hierarchy as bil600: use 10020 for "bought car".
