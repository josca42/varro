table: fact.dnunmm
description: Bankers usikrede indlån og udlån i DKK opdelt på modpartssektor eller løbetid efter dimension og tid
measure: indhold (unit Mio. kr.)
columns:
- dimension: values [ALLBOR=Samlede usikrede indlån i DKK, CPSALL=Modpartssektor - Alle (usikrede indlån i DKK), CPSDFC=Modpartssektor - Indenlandske finansielle selskaber (usikrede indlån i DKK), CPSUOD=Modpartssektor - Øvrig indland (usikrede indlån i DKK), CPSUFO=Modpartssektor - Udland (usikrede indlån i DKK), MATALL=Løbetid - Alle (usikrede indlån i DKK), MATU1D=Løbetid - Op til og med 1 bankdag (usikrede indlån i DKK), MATO1D=Løbetid -  Over 1 bankdag (usikrede indlån i DKK), ALLLEN=Samlede usikrede udlån i DKK (Modpartsektor - Indenlandske finansielle selskaber)]
- tid: date range 2023-04-01 to 2025-09-01

notes:
- No `transakt1` column — transaction type is encoded inside `dimension`. ALLBOR=samlede usikrede indlån; ALLLEN=samlede usikrede udlån.
- CPS* and MAT* codes all refer to the **deposit (indlån)** side only. ALLBOR=CPSALL=MATALL (same total, different labels). For deposits by counterparty: `WHERE dimension IN ('CPSDFC','CPSUOD','CPSUFO')`.
- Lending (udlån) is only available as a single aggregate: `WHERE dimension = 'ALLLEN'`. No counterparty or maturity breakdown for lending.
- The deposit counterparty codes here differ from other tables: CPSDFC=indenlandske finansielle selskaber, CPSUOD=øvrig indland, CPSUFO=udland (no split between domestic banks and others).