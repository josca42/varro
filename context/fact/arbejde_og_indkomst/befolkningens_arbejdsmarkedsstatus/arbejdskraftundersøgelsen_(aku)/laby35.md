table: fact.laby35
description: Beskæftigede med hjemmearbejde efter kommunegruppe, hyppighed, køn og tid
measure: indhold (unit 1.000 personer)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1]
- hyp: values [TOT=I alt, 1=Ja, mindst en gang inden for de sidste fire uger, 3=Nej, ikke inden for de sidste fire uger, 9=Uoplyst]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2021-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at niveau 1 only (5 groups: 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner). Code 0 = national total, not in dim. Filter komgrp != '0' for group-level analysis.
- dim.kommunegrupper has a niveau 2 (individual municipalities by kommunenummer) but this table only uses niveau 1 group codes.
- Limited time range: annual data 2021-2024 only. For longer homeworking time series use aku280a (2008-2024) or aku280k (quarterly 2008-2025).
- hyp=TOT groups all responses — filter hyp='TOT' for total (did/didn't work from home combined), or filter to hyp='1' for those who worked from home at least once in last 4 weeks.