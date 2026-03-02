table: fact.idrres02
description: Idrætsresultater i OL-discipliner efter disciplin, land, relativ præstation og tid
measure: indhold (unit -)
columns:
- diciplin: values [OLSOM=Discipliner ved Sommer-OL , OLVIN=Discipliner ved Vinter-OL]
- land: values [TOT=Hele verden, 5100=Danmark, 5706=Belarus, 5126=Belgien, 5128=Bulgarien ... 372=Nordamerika, 374=Asien, 375=Oceanien, 373=Syd-og Mellemamerika, 5999=Uoplyst]
- relativ: values [WIN018=Andel af samtlige guldmedaljer (pct.), WIN019=Andel af samtlige medaljer (pct.), WIN020=Andel af samlet top-8-placeringer (pct.), WIN024=Guld medaljer (pr. mio. indbyggere), WIN025=Medaljer (pr. mio. indbyggere), WIN026=Top-8-placeringer (pr. mio. indbyggere)]
- tid: date range 2016-01-01 to 2024-01-01

notes:
- relativ contains 6 distinct metrics at different scales — some are percentages (WIN018–WIN020: andel af samtlige medaljer), some are per-million-inhabitants rates (WIN024–WIN026). Never sum across relativ values; always filter to one.
- land TOT = hele verden. Same continental aggregate codes as idrres01 — filter carefully.
- Use idrres02 for comparing countries adjusted for population size (per million metrics), use idrres01 for raw counts.