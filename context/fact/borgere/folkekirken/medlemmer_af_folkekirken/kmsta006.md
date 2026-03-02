table: fact.kmsta006
description: Befolkningen 1. januar (15 år+) efter provsti, socioøkonomisk status, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- provsti: values [101=1-01 Københavns Vor Frue Provsti, 102=1-02 Københavns Holmens Provsti, 103=1-03 Østerbro Provsti, 104=1-04 Nørrebro Provsti, 105=1-05 Vesterbro Provsti ... 1004=10-04 Fredericia Provsti, 1005=10-05 Kolding Provsti, 1006=10-06 Vejle Provsti, 1007=10-07 Hedensted Provsti, 9999=99-99 Uoplyst provsti]
- socio: join dim.socio on socio=kode; levels [1]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/socio.md

notes:
- Provsti-level equivalent of kmsta005 (15+ population by socioeconomic status). Same socio join and caveats apply.
- socio joins dim.socio cleanly (100% match, 4 codes): 1=Erhvervsaktive, 2=Midlertidigt ikke erhvervsaktive, 3=Ikke erhvervsaktive, 4=Andre og børn.
- Covers only 15+ population — sum of all socio rows does NOT equal total provsti population.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination.
