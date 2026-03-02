table: fact.idrudd01
description: Elevtal på fuldtids idrætsuddannelser efter køn, uddannelsestype, status og tid
measure: indhold (unit Antal)
columns:
- konams: values [0=I alt, 1=Mænd, 2=Kvinder]
- uddtype: values [0=I alt, 30=Erhvervsfaglige uddannelser, 50=Bacheloruddannelser, 55=Professionsbacheloruddannelser, 70=Kandidatuddannelser]
- fstatus: values [0000=Alle elever, SLUT=Fuldført, START=Tilgang]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- No dim joins. All columns are inline coded values.
- fstatus values are not additive: 0000=Alle elever (total currently enrolled), START=Tilgang (new entrants), SLUT=Fuldført (completions). Always filter to a single fstatus. Summing across all three counts students multiple times.
- konams=0 is total gender, uddtype=0 is total across education types. Filter to 0 in non-target dimensions to avoid overcounting.
- uddtype has no explicit "I alt" code — code 0 is the all-types total. Individual types (30, 50, 55, 70) are subcategories that do not sum to 0 (they miss students in unlisted types).
