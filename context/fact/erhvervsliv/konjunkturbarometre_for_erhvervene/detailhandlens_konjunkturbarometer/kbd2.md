table: fact.kbd2
description: Vurdering af varelagre i detailhandlen efter branche (DB07), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [100=DETAILHANDEL I ALT, 105=BILHANDEL I ALT (45), 110=Bilhandel inkl. engroshandel (45,1), 115=Bilværksteder mv. (45,2-45,4), 120=DETAILHANDEL EKSKL. BILHANDEL I ALT (47), 125=Handel med fødevarer, drikke- og tobaks- varer (47,1;  47,2; 47,8), 130=Tankstationer (47,3), 135=Anden detailhandel (47,4-47,7; 47,9)]
- bedommelse: values [FST=For stor, PAS=Passende, FLI=For lille, NET=Nettotal]
- tid: date range 2011-05-01 to 2025-10-01

notes:
- Each (branche07, tid) has 4 bedommelse rows. Never SUM across bedommelse — FST, PAS, FLI are response-share percentages summing to 100. NET = FST minus FLI. To get the headline inventory imbalance figure, filter bedommelse='NET'.
- branche07 has the same hierarchy as kbd1: 100=total, 105=bilhandel total (contains 110, 115), 120=ekskl. bil total (contains 125, 130, 135). Avoid mixing aggregate and leaf codes in the same result.
- Data is monthly from May 2011.