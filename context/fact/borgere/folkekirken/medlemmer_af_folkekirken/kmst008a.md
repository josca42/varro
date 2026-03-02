table: fact.kmst008a
description: Befolkningen 1. oktober (15 år+) efter provsti, folkekirkemedlemsskab, højest fuldførte uddannelse og tid
measure: indhold (unit Antal)
columns:
- provsti: values [101=1-01 Københavns Vor Frue Provsti, 102=1-02 Københavns Holmens Provsti, 103=1-03 Østerbro Provsti, 104=1-04 Nørrebro Provsti, 105=1-05 Vesterbro Provsti ... 1004=10-04 Fredericia Provsti, 1005=10-05 Kolding Provsti, 1006=10-06 Vejle Provsti, 1007=10-07 Hedensted Provsti, 9999=99-99 Uoplyst provsti]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- uddannelsef: values [H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- Provsti-level equivalent of kmst007a. Same October reference date and 15+ population caveats apply.
- uddannelsef has 9 inline codes (H10–H90), mutually exclusive, exhaustive within 15+ population.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination.
- Available 2015–2024 only.
