table: fact.pgoeko2
description: Økologisk landbrug - Dækningsbidrag og nettooverskud efter produktionsgrene, regnskabsposter for husdyr og tid
measure: indhold (unit -)
columns:
- prodgren1: values [4005=Malkekøer, 4010=Malkekøer, 1-300 køer, 4015=Malkekøer, mindst 300 køer, 4020=Malkekøer, stor race, 4025=Malkekøer, jersey, 4030=Slagtekalve, 4035=Ammekøer, 4040=Ammekøer, opdræt, 4045=Søer med smågrise, 4090=Slagtesvin, 4135=Høns, 4140=Slagtekyllinger]
- regnh: values [0=Population, antal bedrifter, 5=Stikprøve, antal bedrifter, 6=Enheder, antal, 30=Mælk, kg EKM pr. ko, 35=Mælkepris, kr. pr. 100 kg EKM ... 245=Rentebelastning, bygninger, 250=OMKOSTNINGER I ALT, 260=Nettooverskud, 265=Lønningsevne, 270=LØNNINGSEVNE, KR. PR. TIME]
- tid: date range 2021-01-01 to 2023-01-01
notes:
- Same structure as pgkonv2 (same regnh codes). Same cautions: filter to specific regnh; don't sum totals and sub-categories.
- Fewer prodgren1 options than pgkonv2: organic livestock excludes mink and some conventional svin subtypes. Available: malkekøer (with size and race splits), slagtekalve, ammekøer, søer, slagtesvin, høns, slagtekyllinger.
- Covers økologisk landbrug husdyr. For organic crops use pgoeko1. For conventional livestock use pgkonv2.
