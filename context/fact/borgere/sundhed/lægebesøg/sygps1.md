table: fact.sygps1
description: Modtagere af ydelser i forbindelse med lægebesøg mv. efter område, ydelsesart, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- ydelsesart: values [1=Anæsthesiologi, 4=Dermato-venerologi, 5=Diagnost. radiologi, 6=Reumatologi, 7=Gynækologi/obstetrik ... 82=Kak vagtlægehjælp 82, 83=Vagtlægehjælp 83, 89=KFA-vagtordning 89, 44=København Praktiserende Lægers Laboratorium (KPPL), 85=Lægehjælp (prak.læge amb. Vejle)]
- alerams: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9099=90 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Counts distinct persons who received specific specialist services. Matches the structure of sygks1 but measures unique recipients rather than visit counts.
- omrade has niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is "Hele landet" and omrade=98 is uoplyst — exclude both when joining.
- ydelsesart lists individual specialties (no grand-total row); sum all codes or use sygp1 for totals.
- alerams uses 5-year groups plus IALT.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
