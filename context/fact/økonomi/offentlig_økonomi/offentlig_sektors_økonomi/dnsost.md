table: fact.dnsost
description: Statsfinanser og -gæld, transaktioner efter instrument og tid
measure: indhold (unit Mia. kr.)
columns:
- instrument: values [1000=Bruttofinansieringsbehov, 1100=Nettofinansieringsbehov, 1101=Indbetalinger til staten, 1102=Udbetalinger fra staten, 1110=Indenlandsk nettolåntagning - I alt, 1111=Indenlandsk nettolåntagning - Hos Nationalbanken og pengeinstitutter mv., 1112=Indenlandsk nettolåntagning - Hos øvrige långivere, 1120=Udenlandsk nettolåntagning - I alt, 1130=Formindskelse af statens indestående i Nationalbanken, 1200=Afdrag - Indenlandsk gæld, 1300=Afdrag - Udenlandsk gæld, 1400=Sikkerhedsstillelse, 1410=Sikkerhedsstillelse i EUR, netto]
- tid: date range 1987-01-01 to 2025-09-01

notes:
- Unit is Mia. kr. (billions), not Mio. kr.
- These are transaction (flow) values, not stocks. Complement to dnsosb (beholdninger).
- instrument: 13 codes covering financing needs and debt repayments. 1000=Bruttofinansieringsbehov (gross), 1100=Nettofinansieringsbehov (net). 1110 (indenlandsk nettolåntagning) + 1120 (udenlandsk) + 1130 (formindskelse af NB indestående) = net financing. Don't sum 1000+1100 or mix gross and net concepts.
- Monthly data (1987-2025).