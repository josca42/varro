table: fact.off10
description: Offentlig forvaltning og service, indkomstoverførsler (til husholdninger) efter indkomsttype og tid
measure: indhold (unit Mio. kr.)
columns:
- indkomsttype: values [TOTAL=Indkomstoverførsler i alt, 1=1. Sociale ydelser undtagen overførsler i naturalier i alt, 1.1=1.1. Tjenestemandspensioner, 1.2=1.2. Pensioner, 1.2.1=1.2.1. Folkepension ... 2=2. Andre løbende overførelser i alt, 2.1=2.1. Befordring, 2.2=2.2. Indekstillæg, 2.3=2.3. Fri proces og advokathjælp, 2.4=2.4. Øvrige overførsler]
- tid: date range 1989-01-01 to 2024-01-01

notes:
- indkomsttype: TOTAL=grand total, then numbered hierarchy (1=sociale ydelser i alt, 1.1, 1.2, 1.2.1, ...; 2=andre løbende overførsler, 2.1–2.4). Don't sum TOTAL with its components, and don't mix hierarchy levels.
- Annual (1989–2024). For quarterly data with seasonal adjustment, use off10k.