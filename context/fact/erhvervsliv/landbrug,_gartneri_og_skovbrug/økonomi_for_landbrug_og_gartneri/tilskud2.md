table: fact.tilskud2
description: Direkte tilskud til landbrugssektoren efter tilskudsart og tid
measure: indhold (unit Mio. kr.)
columns:
- tilskudsart: values [300=TILSKUD I ALT, 305=Direkte støtte i alt (1+2+3), 310=1 Basisindkomststøtte og grøn støtte, 315=2 Bio-ordninger i alt, 325=2.1 Biodiversitet og bæredygtighed ... 395=4.4 Vådområder, 400=4.5 Etableringsstøtte til unge landbrugere, 405=4.6 Miljøteknologi og moderniseringsstøtte, 410=4.7 Privat skovrejsning, 415=4.8 Øvrige tilskudsordninger]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- tilskudsart is hierarchical: 300=TILSKUD I ALT, 305=Direkte støtte i alt, 310–415 are sub-items. Never sum all tilskudsart rows — pick a specific level or filter to the aggregate (300).
- Only 4 years of data. No regional breakdown.