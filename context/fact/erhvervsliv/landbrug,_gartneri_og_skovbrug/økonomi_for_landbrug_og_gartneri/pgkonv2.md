table: fact.pgkonv2
description: Konventionelt landbrug - Dækningsbidrag og nettooverskud efter produktionsgrene, regnskabsposter for husdyr og tid
measure: indhold (unit -)
columns:
- prodgren1: values [4005=Malkekøer, 4010=Malkekøer, 1-300 køer, 4015=Malkekøer, mindst 300 køer, 4020=Malkekøer, stor race, 4025=Malkekøer, jersey ... 4120=Slagtesvin, egne smågrise, 4125=Slagtesvin, egne smågrise, færre end 20.000 produceret, 4130=Slagtesvin, egne smågrise, 20.000 eller flere produceret, 4135=Høns, 4140=Slagtekyllinger]
- regnh: values [0=Population, antal bedrifter, 5=Stikprøve, antal bedrifter, 6=Enheder, antal, 30=Mælk, kg EKM pr. ko, 35=Mælkepris, kr. pr. 100 kg EKM ... 245=Rentebelastning, bygninger, 250=OMKOSTNINGER I ALT, 260=Nettooverskud, 265=Lønningsevne, 270=LØNNINGSEVNE, KR. PR. TIME]
- tid: date range 2021-01-01 to 2023-01-01
notes:
- regnh mixes many different metrics per livestock branch: antal enheder, mælk (kg EKM pr. ko), mælkepris (kr. pr. 100 kg), and various cost items. Units differ by code — always filter to a specific regnh.
- prodgren1 has size-bracketed sub-categories (e.g., 4010=Malkekøer 1–300 køer, 4015=Malkekøer mindst 300 køer) alongside totals (4005=Malkekøer). Don't sum totals and sub-categories.
- Covers konventionelt landbrug husdyr (livestock). For afgrøder (crops) use pgkonv1. For organic livestock use pgoeko2.
- pgkonv2 has more prodgren1 options than pgoeko2 (e.g., mink, sopolte, Slagtesvin egne smågrise breakdowns not in organic).
