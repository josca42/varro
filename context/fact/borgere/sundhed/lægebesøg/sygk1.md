table: fact.sygk1
description: Lægebesøg mv. med offentlig tilskud efter område, ydelsesart, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- alerams: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9099=90 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts with niveau 1 (5 regioner, kode 81-85) and niveau 3 (98 kommuner, 3-digit kode). omrade=0 is "Hele landet" (total, not in dim) and omrade=98 is uoplyst (not in dim) — exclude both when joining to dim.nuts.
- ydelsesart is hierarchical: 120=I ALT contains everything. 130=ALMEN LÆGE I ALT is a sub-total of codes 140-180. Summing all ydelsesart values will massively overcount. Pick one level: 120 for grand total, 130 for GP total only, or individual codes for specific visit types.
- alerams uses 5-year age groups (0-4, 5-9, ... 9099=90+) plus IALT=total. Cf. sygk2 which has single-year ages.
- To get national total: filter omrade=0, ydelsesart=120, alerams='IALT', kon='TOT'.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.