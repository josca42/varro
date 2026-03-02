table: fact.magasin2
description: Magasiner efter nøgletal, udgivelsesfrekvens, emne, læsertalsinterval og tid
measure: indhold (unit Antal)
columns:
- aktp: values [DB140=Læsertal (Bruttodækning 1.000), DB170=Magasiner (antal)]
- udgivfrek: values [DB154=Ugentligt, DB155=Sjældnere end ugentligt]
- boger: values [DB156=Bil, båd og mc, DB158=Privatøkonomi og populær videnskab, DB159=Mad, bolig og -indretning, DB160=Kultur, storby og forlystelser, DB161=Mode, design og livsstil, DB162=Elektronik, foto og underholdning, DB163=Fritid, sport og hobby, DB164=Sundhed, velvære, familie og børn, DB165=Rejser, geografi og turisme]
- laesinterval: values [DB145=Alle læsere, DB146=under 20.000 læsere, DB147=20.000-49.999 læsere, DB148=50.000-99.999 læsere, DB149=100.000-199.999 læsere, DB152=200.000-499.999 læsere, DB153=500.000 læsere og derover]
- tid: date range 2018-01-01 to 2024-01-01

notes:
- aktp is a measurement selector: DB140=Læsertal (Bruttodækning 1.000), DB170=Magasiner (antal). Always filter to exactly one.
- laesinterval=DB145 (Alle læsere) is the total for a given combination. Filter WHERE laesinterval='DB145' for simple queries; DB146-DB153 are size buckets.
- boger (emne/topic) has 9 categories, no total row. To get a total across all emner, SUM WHERE laesinterval='DB145'. Each magazine belongs to exactly one topic category so summing is valid.
- udgivfrek has no total row: DB154=Ugentligt, DB155=Sjældnere end ugentligt. Not all boger categories appear in both — some topics only exist in DB155 (sjældnere). Do not assume all 9×2 combinations are present.
- To get all magasiner total: SUM(indhold) WHERE aktp='DB170' AND laesinterval='DB145'.