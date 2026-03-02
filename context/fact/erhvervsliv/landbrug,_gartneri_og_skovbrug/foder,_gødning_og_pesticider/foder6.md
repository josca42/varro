table: fact.foder6
description: Værdiberegning for foderstoffer efter foder, enhed og tid
measure: indhold (unit -)
columns:
- foder: values [6=Foderstoffer i alt, 8=Enkeltfoderstoffer i alt, 9=Korn i alt, 22=Hvede i alt, 26=Rug i alt ... 310=Andre foderblandinger i alt, 315=Mineralstoffoderblandinger i alt, 325=Mineralstoffoderblandinger til kvæg, 320=Mineralstoffoderblandinger til svin, 330=Diverse foderblandinger]
- maengde4: values [10=Mængde (mio. kg), 20=Pris pr. 100 kg, 30=Mio. kr.]
- tid: date range 2000-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector with three semantically incompatible values: 10=Mængde (mio. kg), 20=Pris pr. 100 kg (unit price), 30=Mio. kr. (total value). Every foder×tid combination appears 3 times — once per maengde4. Always filter to exactly one.
- foder has a hierarchy. Top-level aggregates (foder=6 Foderstoffer i alt, foder=8 Enkeltfoderstoffer i alt) only appear for 25 time points — fewer years than the detailed codes (75 rows). Do not mix aggregate and detail codes in a sum.
- Use this table when you need price or value data for feed; for quantity-only questions use foder1 (which goes back to 1990 and has origin/unit options).