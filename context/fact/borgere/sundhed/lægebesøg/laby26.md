table: fact.laby26
description: Overvægt blandt børn efter kommunegruppe, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- kon: values [00=Køn i alt, D=Drenge, P=Piger]
- alder: values [TOT=Alder i alt, 6-7IND=6-7 år, 14-15UD=14-15 år]
- tid: date range 2012-01-01 to 2018-01-01
dim docs: /dim/kommunegrupper.md
notes:
- indhold is a percentage (Pct.) — do not sum across rows. Compare groups directly.
- komgrp joins dim.kommunegrupper with niveau 1 (5 kommunegrupper: Hovedstad, Storby, Provinsby, Opland, Land) and niveau 2 (individual kommuner). komgrp=0 is a national total not in the dim — exclude when joining.
- Very limited data: only 2012-2018 and only two age points (6-7 year school starters, 14-15 year school leavers). Not a general health table — specific to BMI screenings.
- kon uses 00/D/P (not TOT/M/K). kon=00 is total.
