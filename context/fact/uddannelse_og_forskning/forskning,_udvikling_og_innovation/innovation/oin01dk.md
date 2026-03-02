table: fact.oin01dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), innovationstype og tid
measure: indhold (unit Pct.)
columns:
- oin01: values [1000=Offentlig forvaltning og service, 1010=Kommune, 1020=Region, 1030=Stat, 2000=DELSEKTORER (Brancher (DB07)) ... 4200=Museer, 4210=Teater- og koncertvirksomhed,  drift af teater- og koncertsale, arkiver, sportsanlæg, 4220=Andre rengøringsydelser, landskabspleje, 4230=Eventcatering og anden restaurationsvirksomhed, almindelig rengøring, 4240=Øvrige brancher]
- inno: values [10=Innovative i alt, 20=Har indført nye eller væsentligt ændrede produkter, 30=Har indført nye eller væsentligt ændrede serviceydelser, 40=Har indført nye eller væsentligt ændrede processer eller måder at organisere arbejdet på, 50=Har indført nye eller væsentligt ændrede måder at kommunikere med omverdenen på]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- oin01 mixes two independent hierarchies in one column: sector view (1000=Offentlig forvaltning og service total, 1010=Kommune, 1020=Region, 1030=Stat) and DB07 branch view (2000=DELSEKTORER total, 4000-4240=individual branches). Pick one view — never mix rows from both. For sector-level analysis use 1000-1030; for branch breakdown use 2000 as total and 4000-4240 as subcategories.
- inno is multi-select: a workplace can have multiple innovation types simultaneously. inno=10 (Innovative i alt) is the total; the sub-values (20,30,40,50) sum to ~202%, confirming they're not additive. Always use inno=10 as the denominator/total, not the sum of subcategories.
- All indhold values are percentages (share of innovative workplaces). Never sum across oin01 or inno categories.