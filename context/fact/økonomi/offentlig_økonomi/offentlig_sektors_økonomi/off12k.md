table: fact.off12k
description: Offentlig forvaltning og service, skatter og afgifter efter skattetype, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- skatter: values [I.1=I.1. Produktions- og importskatter (DK), I.1.1=I.1.1. Produktskatter, I.1.2=I.1.2. Andre produktionsskatter, I.2=I.2. Løbende indkomst- og formueskatter (DK), I.3=I.3. Obligatoriske bidrag til sociale ordninger (DK) ... 6.1=6.1.  Afgifter af spildevand, 6.2=6.2.  Afgifter i forbindelse med kontrol og bevillinger, 6.2.1=6.2.1.  Heraf EU-ordninger, 6.3=6.3. Indbetalinger til Garantiformuen og Afviklingsfonden, 6.4=6.4. Indbetalinger til Landsbyggefonden]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- saeson is a measurement selector: every skatter×tid row appears twice (N and Y). Always filter: WHERE saeson='N' for unadjusted, saeson='Y' for seasonally adjusted.
- skatter: 47 hierarchical categories. Don't sum parent and child codes. See off12 notes.
- Quarterly (1999Q1–2025Q4).