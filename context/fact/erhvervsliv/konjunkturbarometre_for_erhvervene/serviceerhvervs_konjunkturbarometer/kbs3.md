table: fact.kbs3
description: Kapacitetsudnyttelse i serviceerhverv (ultimo måneden før) efter branche (DB07) og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- tid: date range 2011-05-01 to 2025-10-01

notes:
- Simplest table in this subject: one capacity utilization % per branche07 per month. No extra selector columns to filter.
- branche07=0 (89% in Oct 2025) is the aggregate. Sector totals (uppercase branche07 labels) and their sub-sectors (lowercase) coexist — don't sum across all branche07 codes.
- indhold is a level (% of capacity used), not a share that sums to 100. Safe to compare across sectors or time.
- Note: measured "ultimo måneden før" (end of preceding month) — the tid label is one month ahead of the measurement date.