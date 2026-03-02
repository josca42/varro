table: fact.kmsta002
description: Befolkningen 1. januar efter provsti, herkomst, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- provsti: values [101=1-01 Københavns Vor Frue Provsti, 102=1-02 Københavns Holmens Provsti, 103=1-03 Østerbro Provsti, 104=1-04 Nørrebro Provsti, 105=1-05 Vesterbro Provsti ... 1004=10-04 Fredericia Provsti, 1005=10-05 Kolding Provsti, 1006=10-06 Vejle Provsti, 1007=10-07 Hedensted Provsti, 9999=99-99 Uoplyst provsti]
- herkomst: join dim.herkomst on herkomst=kode [approx]; levels [1]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/herkomst.md

notes:
- Provsti-level equivalent of kmsta001. Same herkomst coding — do NOT join to dim.herkomst.
- herkomst uses 5 codes: 1=Dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande. Use ColumnValues("kmsta002", "herkomst") for labels.
- These 5 codes are exhaustive — sum all for total population by provsti.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination.
