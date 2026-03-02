table: fact.off12
description: Offentlig forvaltning og service, skatter og afgifter efter skattetype og tid
measure: indhold (unit Mio. kr.)
columns:
- skatter: values [I.1=I.1. Produktions- og importskatter (DK), I.1.1=I.1.1. Produktskatter, I.1.2=I.1.2. Andre produktionsskatter, I.2=I.2. Løbende indkomst- og formueskatter (DK), I.3=I.3. Obligatoriske bidrag til sociale ordninger (DK) ... 6.1=6.1.  Afgifter af spildevand, 6.2=6.2.  Afgifter i forbindelse med kontrol og bevillinger, 6.2.1=6.2.1.  Heraf EU-ordninger, 6.3=6.3. Indbetalinger til Garantiformuen og Afviklingsfonden, 6.4=6.4. Indbetalinger til Landsbyggefonden]
- tid: date range 1971-01-01 to 2024-01-01

notes:
- skatter: 47 categories in a deep hierarchy mixing two classification schemes — Roman numeral top-levels (I.1=Produktions- og importskatter, I.2=Indkomstskat, I.3=Sociale bidrag, I.4, I.5, I.6, I.7) and numbered sub-codes. Use ColumnValues("off12", "skatter") to browse all 47 values. Don't sum parent and child codes.
- Annual (1971–2024). For quarterly + seasonal adjustment, use off12k. For revision comparisons, use voff12.