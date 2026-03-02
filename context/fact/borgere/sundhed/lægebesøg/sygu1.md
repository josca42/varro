table: fact.sygu1
description: Offentlige udgifter ved lægebesøg mv. efter område, ydelsesart, alder, køn og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 310=LABORATORIER, 320=ØVRIGE YDELSER]
- alerams: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9099=90 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Expenditure version of sygk1 (same dimensions, indhold = 1.000 kr. instead of visit count). Use when you need cost data by area and visit type.
- omrade has niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is "Hele landet" and omrade=98 is uoplyst — exclude both when joining.
- ydelsesart is hierarchical: 120=I ALT is the grand total, 130=ALMEN LÆGE I ALT is GP sub-total. Do not sum all ydelsesart values. Note: sygu1 includes ydelsesart 310=LABORATORIER which is absent from sygk1.
- alerams uses 5-year groups plus IALT.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
