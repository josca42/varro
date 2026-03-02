table: fact.auk05
description: Offentligt forsørgede (støttet beskæftigelse, fuldtidsmodtagere) efter ydelsestype, sektor, køn, alder og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [TOT=I alt, LT=Løntilskud, FL=Fleksjob, SK=Skånejob]
- sektor: values [1000=Sektorer i alt, 1016=Stat (inklusiv sociale kasser og fonde), 1020=Regioner, 1025=Kommuner, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2008-01-01 to 2025-04-01
notes:
- Covers only støttet beskæftigelse (supported employment): løntilskud (LT), fleksjob (FL), skånejob (SK). ydelsestype=TOT = FL + LT + SK (additive, no overlap). For broader public benefit data use auk01.
- sektor: 1000 = Sektorer i alt (total). Individual sectors (stat, regioner, kommuner, private, etc.) are additive sub-parts of sektor=1000. Filter sektor='1000' for national totals.
- No omrade column — no regional breakdown. National data only.
- Quarterly data starting 2008-01-01 (one year later than other auk tables). For annual data use auh05.
