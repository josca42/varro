table: fact.dnvpstrh
description: Strukturerede obligationer fordelt på underliggende aktivtype og investorsektor efter underliggende aktivtype, investorsektor, værdiansættelse, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- uakt: values [T=Alle aktivtyper, A=Aktier, V=Valuta, I=Rente, R=Råvarer, X=Andet, M=Multi (kombination af de nævnte aktivtyper), Z=ikke oplyst]
- invsektor: join dim.esa on invsektor=kode [approx]
- vaerdian: values [B=Markedsværdi, N=Nominel værdi]
- data: values [8=Beholdning, 4=Nettotilgang, 9=Kursreguleringer]
- tid: date range 1999-12-01 to 2025-08-01
dim docs: /dim/esa.md

notes:
- invsektor uses numeric codes (0000, 1000, 1100, 1212, etc.) — these do NOT join to dim.esa (S.xxx notation). 0% match rate confirmed. Treat as inline coded values.
- vaerdian and data are measurement selectors. Filter both: vaerdian='B' (markedsværdi), data=8 (beholdning). Note data codes are 8/4/9, not 1/2/3.
- uakt='T' is the aggregate for all underlying asset types. To avoid double-counting don't mix T with subtypes.
- For investor-sector breakdown of structured bonds. For product characteristics breakdown see dnvpstrs.