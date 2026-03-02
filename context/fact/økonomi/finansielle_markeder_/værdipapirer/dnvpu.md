table: fact.dnvpu
description: Papirer udstedt i udlandet efter papirtype, kupon, valuta, løbetid, udstedersektor, udstedelsesland, værdiansættelse, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- papir: values [20A=Obligationer, i alt]
- kupon: values [N=Alle papirer med og uden kupon, 0=Kupon <= 2%, A=2% < kupon <= 3%, B=3% < kupon <= 4%, C=4% < kupon <= 5%, D=5% < kupon <= 6%, E=Kupon > 6%]
- valuta: values [Z01=Alle valutaer, DKK=Danske kroner, EUR=Euro, Z02=Anden valuta end DKK og EUR]
- lobetid: values [A=Alle løbetider/uspecificeret, F=Restløbetid<=1 år, K=Restløbetid > 1 år]
- udstedsektor: join dim.esa on udstedsektor::text=kode [approx]
- udstland: values [Z9=Udlandet, i alt, EU=Eurolande, RW=Resten af verden (ex DK og Eurolande)]
- vaerdian: values [B=Markedsværdi, N=Nominel værdi]
- data: values [1=Beholdning, 2=Nettotilgang, 3=Kursreguleringer (omvurderinger)]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/esa.md

notes:
- udstedsektor uses numeric codes (1000, 1100, 1200, 1212, 1256, 1300) — these do NOT join to dim.esa (S.xxx notation). 0% match rate confirmed. Treat as inline coded values.
- vaerdian and data are measurement selectors. Filter both: vaerdian='B' (markedsværdi), data=1 (beholdning). data=2 is nettotilgang, data=3 is kursreguleringer — incompatible with beholdning.
- papir only has one value: 20A=Obligationer, i alt. No filtering needed on papir.
- valuta: Z01=alle valutaer and Z02=anden valuta are aggregate codes only — no dim join. DKK and EUR are specific currencies.
- udstland has only 3 values: Z9=udlandet i alt, EU=eurolande, RW=resten. Filter to one; Z9 is the sum of EU and RW.
- This table covers securities issued abroad by Danish entities — the foreign issuance complement to domestic VP tables.