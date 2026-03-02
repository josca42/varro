table: fact.knatio3
description: Kreative erhvervs nationaløkonomiske betydning efter kreative erhverv, aktivitet, sektor, nøgletal, effekter, prisenhed og tid
measure: indhold (unit -)
columns:
- kreativeerhverv: values [TOT=Alle kreative erhverv, C05=Arkitektur, C10=Industrielt og strategisk design, C15=Kommunikationsdesign, C20=Forlag og udgivelse, C25=Teater og scenekunst, C30=Musik og lyd, C35=Film, TV og animation, C40=Digitale spil og XR, C45=Mode, C50=Interiørdesign, C55=Kunst og galleri]
- aktivitet: values [TOT1=Aktivitet i alt, DET=Detailhandel, ENG=Engroshandel, AND=Øvrig aktivitet]
- sektor: values [TOT2=Sektor i alt, PRI=Markedsmæssig sektor, OFF=Ikke markedsmæssig sektor]
- aktp: values [PRO=Produktion (1.000 kr.), IMP=Import (1.000 kr.), EKS=Eksport (1.000 kr.), BVT=Bruttoværditilvækst (BVT) (1.000 kr.), BES=Beskæftigelse (antal), ARS=Fuldtidsbeskæftigede (antal)]
- effekter: values [TOT3=Effekter i alt, DIR=Direkte effekter, IND=Indirekte effekter]
- prisenhed: values [V=Løbende priser, Y=2020-priser (kædede værdier)]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- Same three mandatory selector columns as knatio1: filter `aktp`, `prisenhed`, and `effekter` before aggregating.
- `kreativeerhverv` has TOT plus 11 individual creative industries (C05–C55). Filter to TOT for an overall figure. No dim join needed — codes are fully described inline.
- `aktivitet` and `sektor` have aggregate totals (TOT1, TOT2). Filter to totals for a Denmark-wide figure.
