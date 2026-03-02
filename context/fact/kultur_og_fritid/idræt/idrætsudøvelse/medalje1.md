table: fact.medalje1
description: Danske vindere af internationale sportsmedaljer efter mesterskab, idrætsgrene, medalje og tid
measure: indhold (unit Antal)
columns:
- mester: values [K1=Alle Mesterskaber, K2=Verdensmesterskaber, K3=Europamesterskaber, K4=Olympiske lege, K5=Paralympics, K6=European Games]
- idraet: values [A01=Alle idrætsgrene, A02=Amerikansk fodbold, A03=Atletik, A05=Automobilsport (4 hjul), A06=Badminton ... A76=Standup Paddleboarding, A77=Rope Skipping, A78=Motorsport, A79=Kickboxing, A80=Surfing]
- medalje: values [M1=Alle Medaljer, M2=Guld, M3=Sølv, M4=Bronze]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- All three categorical columns have aggregate "all" values: mester K1 = alle mesterskaber, idraet A01 = alle idrætsgrene, medalje M1 = alle medaljer (= M2+M3+M4). Never mix totals with specific values in a sum.
- medalje M1 is the sum of M2+M3+M4, so do not SUM across all medalje values — pick one category or filter to M1 for the aggregate.
- Data goes back to 1980, useful for long-term historical medal trends.
- To get Danish gold medals at World Championships in athletics: `WHERE mester='K2' AND idraet='A03' AND medalje='M2'`.