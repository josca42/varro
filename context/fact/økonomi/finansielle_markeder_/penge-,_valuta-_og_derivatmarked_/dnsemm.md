table: fact.dnsemm
description: Bankers sikrede indlån og udlån i DKK opdelt på modpartssektor, løbetid eller sikkerhedsstillelse efter transaktionstype, dimension og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt1: values [SEBORR=Sikrede indlån i DKK, SELEND=Sikrede udlån i DKK]
- dimension: values [ALL=Samlet, CPSALL=Modpartssektor - Alle, CPSDBA=Modpartssektor - Indenlandske banker, CPSCCP=Modpartssektor - Centrale modparter (CCP), CPSSOT=Modpartssektor - Øvrig, MATALL=Løbetid - Alle, MAT1DA=Løbetid - Op til og med 1 bankdag, MAT1D5=Løbetid - Over 1 bankdag op til og med 5 bankdage, MAT520=Løbetid - Over 5 bankdage op til og med 20 bankdage, MATO20=Løbetid - Over 20 bankdage, COLALL=Sikkerhedsstillelse - Alle, COLDMB=Sikkerhedsstillelse - Danske realkreditobligationer, COLDGB=Sikkerhedsstillelse - Danske statsobligationer, COLOTH=Sikkerhedsstillelse - Øvrig]
- tid: date range 2023-04-01 to 2025-09-01

notes:
- Same stacked `dimension` structure: CPS*=modpartssektor, MAT*=løbetid, COL*=sikkerhedsstillelse. ALL=CPSALL=MATALL=COLALL. Pick one group per query.
- COL* breakdown: COLDMB=danske realkreditobligationer, COLDGB=danske statsobligationer, COLOTH=øvrig. COLOTH/SEBORR has 29 observations vs 30 for the rest — one missing month in the data.
- `transakt1` SEBORR=sikrede indlån (borrowing), SELEND=sikrede udlån (lending). Counterparty sector for SEBORR includes CCP (centrale modparter), unlike dnfx/dnfxswap.