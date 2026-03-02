table: fact.oin03dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), igangsætter og tid
measure: indhold (unit Pct.)
columns:
- oin01: values [1000=Offentlig forvaltning og service, 1010=Kommune, 1020=Region, 1030=Stat, 2000=DELSEKTORER (Brancher (DB07)) ... 4200=Museer, 4210=Teater- og koncertvirksomhed,  drift af teater- og koncertsale, arkiver, sportsanlæg, 4220=Andre rengøringsydelser, landskabspleje, 4230=Eventcatering og anden restaurationsvirksomhed, almindelig rengøring, 4240=Øvrige brancher]
- oin03: values [100=Medarbejdere på arbejdspladsen, 110=Ledere på arbejdspladsen, 120=Borgere, 130=Private virksomheder, 140=Arbejdspladsens nærmeste politiske ledelelse, 150=Frivillige foreninger / organisationer, 155=Fonde, 160=Videregående uddannelses- eller forskningsinstitutioner, 170=Ny lovgivning eller andre nationale politiske krav, 180=Ny teknologi, 190=Innovation eller andre aktiviteter hos andre offentlige arbejdspladser, 200=Økonomisk pres på arbejdspladsen, 202=Organisationsforandringer, 207=Inspiration fra udlandet, 209=COVID-19, 210=Andet, 220=Ved ikke]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- oin01 mixes two independent hierarchies: sector view (1000=total, 1010=Kommune, 1020=Region, 1030=Stat) and DB07 branch view (2000=total, 4000-4240=individual branches). Choose one view per query.
- oin03 (igangsætter) is multi-select: a workplace can attribute its innovation to multiple initiators. Values sum to ~217% for oin01=1000, confirming these are independent rates. Never sum across oin03 categories.
- Each row is "% of innovative workplaces that cited this initiator." Compare individual initiator values against each other, but do not add them.