table: fact.kryds1
description: Befolkningen 1. januar efter Hovedpersons herkomst, Hovedpersons fødeland, Hovedpersons statsborgerskab, Moders fødeland, moders statsborgerskab, Faders fødeland, faders statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- hoher: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere]
- hofod: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land]
- hostat: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land]
- mofod: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land, UOP=Uoplyst fødeland]
- mostat: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land, UOPL=Uoplyst statsborgerskab]
- fafod: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land, UOP=Uoplyst fødeland]
- fastat: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land, UOPL=Uoplyst statsborgerskab]
- tid: date range 2019-01-01 to 2025-01-01

notes:
- 7 dimension columns (hoher, hofod, hostat, mofod, mostat, fafod, fastat). Aggregate code is 0000 for geographic dims and TOT for hoher. Filter all to aggregate when only one dimension is of interest.
- All dimensions use coarse geographic coding (Danmark=5100, V=vestlig, IV=ikke-vestlig, plus UOP/UOPL for unknowns). No country-level detail — use folk2/folk1c for that.
- Use for cross-tabulations like "efterkommere (hoher=3) whose fathers were born in non-western country (fafod=IV)". This is the only table supporting simultaneous parent-level filtering.
- Good for investigating how parent background interacts with person's herkomst classification.