table: fact.kryds3
description: Befolkningen 1. januar efter Hovedpersons herkomst, Hovedpersons fødeland, Moders fødeland, Faders fødeland og tid
measure: indhold (unit Antal)
columns:
- hoher: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere]
- hofod: values [0=I alt, 5100=Danmark, 5122=Albanien, 5124=Andorra, 5706=Belarus ... 5532=Østtimor, 5599=Øer i Stillehavet, 5103=Statsløs, 5999=Uoplyst, 9999=Uoplyst land]
- mofod: values [0=I alt, 5100=Danmark, 5122=Albanien, 5124=Andorra, 5706=Belarus ... 5532=Østtimor, 5599=Øer i Stillehavet, 5103=Statsløs, 5999=Uoplyst, 9999=Uoplyst land]
- fafod: values [0=I alt, 5100=Danmark, 5122=Albanien, 5124=Andorra, 5706=Belarus ... 5532=Østtimor, 5599=Øer i Stillehavet, 5103=Statsløs, 5999=Uoplyst, 9999=Uoplyst land]
- tid: date range 2019-01-01 to 2025-01-01

notes:
- 4 dimension columns (hoher, hofod, mofod, fafod). All geographic dims use level-3 country codes matching lande_psd. Aggregate is 0 for hofod/mofod/fafod and TOT for hoher.
- To query total population by person's birth country: filter hoher='TOT', mofod=0, fafod=0, then group by hofod.
- Use for: "how many indvandrere (hoher=4) were born in Syria (hofod=5486) and have a mother also born in Syria (mofod=5486)?" — this is the unique capability of this table vs folk2.
- Very sparse at the 3-way country cross: most cells will be zero or small. Aggregate to continent or use simpler tables for totals.