table: fact.auh05
description: Offentligt forsørgede (støttet beskæftigelse, fuldtidsmodtagere) efter ydelsestype, sektor, køn, alder og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [TOT=I alt, LT=Løntilskud, FL=Fleksjob, SK=Skånejob]
- sektor: values [1000=Sektorer i alt, 1016=Stat (inklusiv sociale kasser og fonde), 1020=Regioner, 1025=Kommuner, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- Annual version of auk05 (støttet beskæftigelse). Latest to 2024-01-01.
- ydelsestype: TOT = FL + LT + SK (additive). sektor=1000 = national total; individual sectors are additive parts.
- No regional breakdown. Starts 2008-01-01.
