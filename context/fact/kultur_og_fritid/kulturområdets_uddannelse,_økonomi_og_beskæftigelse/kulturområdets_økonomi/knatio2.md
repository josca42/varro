table: fact.knatio2
description: Kulturelle erhvervs nationaløkonomiske betydning efter kulturemne, type, aktivitet, sektor, nøgletal, effekter, prisenhed og tid
measure: indhold (unit -)
columns:
- kulturemne: join dim.kulturemner on kulturemne=kode [approx]; levels [2]
- type: values [TOT=Type i alt, KER=Kernebranche, STO=Støttebranche]
- aktivitet: values [TOT1=Aktivitet i alt, DET=Detailhandel, ENG=Engroshandel, AND=Øvrig aktivitet]
- sektor: values [TOT2=Sektor i alt, PRI=Markedsmæssig sektor, OFF=Ikke markedsmæssig sektor]
- aktp: values [PRO=Produktion (1.000 kr.), IMP=Import (1.000 kr.), EKS=Eksport (1.000 kr.), BVT=Bruttoværditilvækst (BVT) (1.000 kr.), BES=Beskæftigelse (antal), ARS=Fuldtidsbeskæftigede (antal)]
- effekter: values [TOT3=Effekter i alt, DIR=Direkte effekter, IND=Indirekte effekter]
- prisenhed: values [V=Løbende priser, Y=2020-priser (kædede værdier)]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/kulturemner.md

notes:
- Same three mandatory selector columns as knatio1: filter `aktp`, `prisenhed`, and `effekter` before aggregating.
- `kulturemne` uses K-prefixed codes but with a different, more detailed classification than dim.kulturemner — only 37% match. Codes K12, K20, K23, K35, K36, K40–K42, K50–K53, K60–K63 exist in the fact table but not in the standard dim. Use ColumnValues("knatio2", "kulturemne") to see all codes with labels; do not rely on a dim.kulturemner join.
- `type` has TOT (total), KER (kernebranche), STO (støttebranche). Filter `type='TOT'` for overall kulturelle erhverv.
- `aktivitet` and `sektor` have aggregate totals (TOT1, TOT2).
