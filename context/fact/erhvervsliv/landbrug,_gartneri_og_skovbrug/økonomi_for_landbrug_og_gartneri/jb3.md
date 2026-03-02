table: fact.jb3
description: Jordbrugets renteudgifter og gæld efter udgiftstype og tid
measure: indhold (unit Mio. kr.)
columns:
- fui6: values [2000=1. Finansieringsomkostninger i alt , 2005=1.1 Renteudgifter, realkreditlån, 2010=1.2 Renteudgifter, pengeinstitut, 2015=1.3 Renteudgifter, andet, 2020=1.4 Realiseret tab ved swap mv., 2100=2. Gæld i alt, 2200=2.1 Realkreditinstitut i alt, 2205=2.1.1 Alm. realkreditlån, 2210=2.1.2 Rentetilpasningslån, 2215=2.1.3 EURO-lån, 2300=2.2 Pengeinstitut i alt, 2305=2.2.1 Lån i danske kroner, 2310=2.2.2 Lån i udenlandsk valuta, 2315=2.2.3 Markedsværdi, SWAP, 2400=2.3 Anden gæld, 2500=Gennemsnitlig rente i pct.]
- tid: date range 2006-01-01 to 2024-01-01
notes:
- fui6 mixes two incompatible types of values: financial flows/costs (codes 2000–2020, Mio. kr.) and debt stocks (codes 2100–2400, Mio. kr.), plus one percentage (2500=Gennemsnitlig rente i pct.). Never sum across fui6 — cost flows and debt stocks are different metrics, and 2500 is a rate.
- Code 2000=Finansieringsomkostninger i alt sums 2005+2010+2015+2020. Code 2100=Gæld i alt sums 2200+2300+2400.
