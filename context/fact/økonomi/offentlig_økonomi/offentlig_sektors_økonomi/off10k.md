table: fact.off10k
description: Offentlig forvaltning og service, indkomstoverførsler (til husholdninger) efter indkomsttype, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- indkomsttype: values [TOTAL=Indkomstoverførsler i alt, 1=1. Sociale ydelser undtagen overførsler i naturalier i alt, 1.1=1.1. Tjenestemandspensioner, 1.2=1.2. Pensioner, 1.2.1=1.2.1. Folkepension ... 2=2. Andre løbende overførelser i alt, 2.1=2.1. Befordring, 2.2=2.2. Indekstillæg, 2.3=2.3. Fri proces og advokathjælp, 2.4=2.4. Øvrige overførsler]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- saeson is a measurement selector: every indkomsttype×tid row appears twice (N and Y). Always filter to one: WHERE saeson='N' for unadjusted, saeson='Y' for seasonally adjusted. Summing both doubles all values.
- indkomsttype hierarchy same as off10: TOTAL=grand total, hierarchical subcategories. Pick one level.
- Quarterly (1999Q1–2025Q4).