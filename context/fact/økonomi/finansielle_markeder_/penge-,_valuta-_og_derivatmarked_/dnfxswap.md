table: fact.dnfxswap
description: Bankers køb og salg af FX swaps i DKK opdelt på valuta, modpartssektor eller løbetid efter transaktionstype, dimension og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt1: values [FSBUYI=Køb af DKK (korte ben), FSSELL=Salg af DKK (korte ben)]
- dimension: values [ALL=Samlet, FCCALL=Valuta - Alle, FCCEUR=Valuta - EUR, FCCUSD=Valuta - USD, FCCOTH=Valuta - Øvrig, CPSALL=Modpartssektor - Alle, CPSDBA=Modpartssektor - Indenlandske banker, CPSOFC=Modpartssektor - Øvrige indenlandske finansielle selskaber, CPSODO=Modpartssektor - Øvrig indland, CPSFOR=Modpartssektor - Udland, MATALL=Løbetid - Alle, MAT5DA=Løbetid - Op til og med 5 bankdage, MAT520=Løbetid - Over 5 bankdage op til og med 20 bankdage, MATU60=Løbetid - Over 20 bankdage op til og med 60 bankdage, MATO60=Løbetid - Over 60 bankdage]
- tid: date range 2023-04-01 to 2025-09-01

notes:
- Same stacked `dimension` structure as dnfx: FCC*=valuta, CPS*=modpartssektor, MAT*=løbetid. Pick one group per query; ALL=FCCALL=CPSALL=MATALL.
- Maturity buckets differ from dnfx: MAT5DA (≤5 bankdage), MAT520 (5–20 bankdage), MATU60 (20–60 bankdage), MATO60 (>60 bankdage) — reflecting longer typical maturities for FX swaps vs. spot.
- `transakt1` FSBUYI/FSSELL refers to the near leg (korte ben) of the swap: køb/salg af DKK på valutatidspunktet.