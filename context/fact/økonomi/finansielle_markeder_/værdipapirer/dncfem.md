table: fact.dncfem
description: Klimarelaterede indikatorer for danske realkreditobligationer baseret på energimærker efter investor, investering, udledningskategori, værdier og tid
measure: indhold (unit -)
columns:
- investor: values [MFI=- S.122 Penge- og realkreditinstitutter, IF=- S.124 Investeringsfonde, IFG=- - S.124 Investeringsfonde ekskl. S.128+S.129 Forsikrings- og pensionssektorens investeringer, FP=- S.128+S.129 Forsikrings- og pensionssektoren, FPG=- - S.128+S.129 Forsikrings- og pensionssektoren, hvor ejerandele i S.140 Investeringsfonde er gennemlyst]
- invest1: values [200=Danske realkreditobligationer]
- udlkat: values [300=Udledninger fra ejendomme finansieret af realkreditobligationer]
- vaerdi1: values [FE=Absolutte finansierede udledninger (tusinde ton CO2e, årsniveau), COV=Dækningsgrad (pct.)]
- tid: date range 2022-10-01 to 2025-04-01

notes:
- vaerdi1 has two incompatible metrics: FE (tusinde ton CO2e, absolutte udledninger) and COV (pct. dækningsgrad). Always filter to one — do not sum or average them.
- invest1 only has one value (200=Danske realkreditobligationer) and udlkat only one (300=udledninger fra ejendomme). No filtering decisions needed there.
- Very short time series (from late 2022) and covers only mortgage-backed emissions via energy labels. For broader climate indicators including equities and corporate bonds use dncfe.
- IFG and FPG are look-through variants of IF and FP — do not add to their parent category.