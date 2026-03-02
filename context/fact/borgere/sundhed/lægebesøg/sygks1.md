table: fact.sygks1
description: Lægebesøg mv. med offentlig tilskud (detaljeret) efter område, ydelsesart, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- ydelsesart: values [1=Anæsthesiologi, 4=Dermato-venerologi, 5=Diagnost. radiologi, 6=Reumatologi, 7=Gynækologi/obstetrik ... 82=Kak vagtlægehjælp 82, 83=Vagtlægehjælp 83, 89=KFA-vagtordning 89, 44=København Praktiserende Lægers Laboratorium (KPPL), 85=Lægehjælp (prak.læge amb. Vejle)]
- alerams: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9099=90 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- "Detaljeret" version: ydelsesart lists individual medical specialties (numeric codes 1-89) instead of grouped categories. There is no grand-total ydelsesart row — sum across all codes to get totals, or use sygk1 instead.
- omrade joins dim.nuts with niveau 1 (5 regioner, kode 81-85) and niveau 3 (98 kommuner). omrade=0 is "Hele landet" (total, not in dim) and omrade=98 is uoplyst — exclude both when joining.
- alerams uses 5-year groups plus IALT. cf. sygks2 which has single-year ages but region-only breakdown.
- Use this table when you need visits broken down by individual medical specialty with commune-level geography.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
