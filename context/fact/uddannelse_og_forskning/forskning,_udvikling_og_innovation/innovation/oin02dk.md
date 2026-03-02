table: fact.oin02dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), nyhedsgrad og tid
measure: indhold (unit Pct.)
columns:
- oin01: values [1000=Offentlig forvaltning og service, 1010=Kommune, 1020=Region, 1030=Stat, 2000=DELSEKTORER (Brancher (DB07)) ... 4200=Museer, 4210=Teater- og koncertvirksomhed,  drift af teater- og koncertsale, arkiver, sportsanlæg, 4220=Andre rengøringsydelser, landskabspleje, 4230=Eventcatering og anden restaurationsvirksomhed, almindelig rengøring, 4240=Øvrige brancher]
- nyhedsgrad: values [60=Arbejdspladsen var den første til at udvikle innovationen, 70=Innovationen i vidt omfang inspireret af andres løsninger, 80=Innovationen i vidt omfang en kopi af andres løsninger, men tilpasset arbejdspladsen, 90=Ved ikke]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- oin01 mixes two independent hierarchies: sector view (1000=total, 1010=Kommune, 1020=Region, 1030=Stat) and DB07 branch view (2000=total, 4000-4240=individual branches). Choose one view per query.
- nyhedsgrad has 4 mutually exclusive categories that sum to ~100% (only innovative workplaces respond): 60=first-mover, 70=inspired by others, 80=copy/adapted, 90=don't know. These can be compared directly; code 90 (Ved ikke) is usually excluded from analysis.
- All indhold values are percentages. Never sum across oin01 categories.