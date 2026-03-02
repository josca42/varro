table: fact.oin04dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), opnået værdier og tid
measure: indhold (unit Pct.)
columns:
- oin01: values [1000=Offentlig forvaltning og service, 1010=Kommune, 1020=Region, 1030=Stat, 2000=DELSEKTORER (Brancher (DB07)) ... 4200=Museer, 4210=Teater- og koncertvirksomhed,  drift af teater- og koncertsale, arkiver, sportsanlæg, 4220=Andre rengøringsydelser, landskabspleje, 4230=Eventcatering og anden restaurationsvirksomhed, almindelig rengøring, 4240=Øvrige brancher]
- oin02: values [230=Forbedret kvalitet, 240=Forøget effektivitet, 250=Forøget medarbejdertilfredshed, 260=Borgerne har opnået større indsigt eller indflydelse, 265=Indfrielse af politiske mål, 270=Andet, 280=Ved ikke]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- oin01 mixes two independent hierarchies: sector view (1000=total, 1010=Kommune, 1020=Region, 1030=Stat) and DB07 branch view (2000=total, 4000-4240=individual branches). Choose one view per query.
- oin02 (opnået værdier) is multi-select: a workplace can report multiple achieved outcomes. Values sum to ~229% for oin01=1000, confirming these are independent rates. Never sum across oin02 categories.
- Each row is "% of innovative workplaces that achieved this outcome." Useful for ranking which outcomes are most commonly achieved, but not additive.