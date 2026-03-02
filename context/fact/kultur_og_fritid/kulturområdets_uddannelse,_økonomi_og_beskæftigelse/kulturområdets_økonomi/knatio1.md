table: fact.knatio1
description: Kulturelle og kreative erhvervs nationaløkonomiske betydning efter aktivitet, sektor, nøgletal, effekter, prisenhed og tid
measure: indhold (unit -)
columns:
- aktivi: values [TOT1=Aktivitet i alt, DET=Detailhandel, ENG=Engroshandel, AND=Øvrig aktivitet]
- sektor: values [TOT2=Sektor i alt, PRI=Markedsmæssig sektor, OFF=Ikke markedsmæssig sektor]
- aktp: values [PRO=Produktion (1.000 kr.), IMP=Import (1.000 kr.), EKS=Eksport (1.000 kr.), BVT=Bruttoværditilvækst (BVT) (1.000 kr.), BES=Beskæftigelse (antal), ARS=Fuldtidsbeskæftigede (antal)]
- effekter: values [TOT3=Effekter i alt, DIR=Direkte effekter, IND=Indirekte effekter]
- prisenhed: values [V=Løbende priser, Y=2020-priser (kædede værdier)]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- Three selector columns MUST all be filtered: `aktp`, `prisenhed`, and `effekter`. Forgetting any one silently multiplies results.
- `aktp` selects between fundamentally different measures: PRO/IMP/EKS/BVT are monetary (1.000 kr.), BES/ARS are headcounts. Never mix in a sum.
- `prisenhed`: V=løbende priser, Y=2020-priser (kædede). For time series use Y. Pick exactly one.
- `effekter`: TOT3=total, DIR=direkte, IND=indirekte. TOT3 = DIR + IND, so filter to TOT3 to avoid double-counting.
- `aktivi` and `sektor` also have aggregate totals (TOT1, TOT2). Filter to totals for a Denmark-wide figure.
- Typical simple query: `WHERE aktp='BVT' AND prisenhed='V' AND effekter='TOT3' AND aktivi='TOT1' AND sektor='TOT2'`
