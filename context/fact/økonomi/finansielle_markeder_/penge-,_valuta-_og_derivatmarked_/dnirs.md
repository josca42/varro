table: fact.dnirs
description: Bankers køb og salg af renteswaps i DKK opdelt på modpartssektor, løbetid eller referencerente efter transaktionstype, dimension og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt1: values [ISRECE=Modtaget af fast rente i DKK, ISPAID=Betalt af fast rente i DKK]
- dimension: values [ALL=Samlet, CPSALL=Modpartssektor - Alle, CPSCCP=Modpartssektor - Centrale modparter (CCP), CPSIOT=Modpartssektor - Øvrig, MATALL=Løbetid - Alle, MAT2YE=Løbetid - Op til og med 480 bankdage, MAT2Y5=Løbetid - Over 480 bankdage op til og med 1.200 bankdage, MATO5Y=Løbetid - Over 1.200 bankdage, REFALL=Referencerente - Alle, REFC3M=Referencerente - CIBOR3M, REFC6M=Referencerente - CIBOR6M, REFDES=Referencerente - DESTR, REFOTH=Referencerente - Øvrig]
- tid: date range 2023-04-01 to 2025-09-01

notes:
- Same stacked `dimension` structure: CPS*=modpartssektor, MAT*=løbetid, REF*=referencerente. ALL=CPSALL=MATALL=REFALL. Pick one group per query.
- Maturity is in bankdays, not calendar days: MAT2YE (≤480 bankdage, ~2 år), MAT2Y5 (480–1200, ~2–5 år), MATO5Y (>1200, >5 år).
- REF*: REFC3M=CIBOR3M, REFC6M=CIBOR6M, REFDES=DESTR, REFOTH=øvrig. REFOTH has fewer observations (36 vs 60) — data gaps for some months.
- `transakt1` ISRECE (modtaget fast rente) and ISPAID (betalt fast rente) are the two sides of the same swap; summing them would double-count notional traded.