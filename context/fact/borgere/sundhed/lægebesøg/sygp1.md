table: fact.sygp1
description: Personer med kontakt til læge mv. med offentlig tilskud efter område, ydelsesart, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- alerams: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9099=90 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Counts distinct persons who had contact, not number of visits (cf. sygk1 which counts visits). A person visiting the GP three times counts as 1 here but 3 in sygk1.
- omrade has niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is "Hele landet" and omrade=98 is uoplyst — exclude both when joining to dim.nuts.
- ydelsesart is hierarchical: 120=I ALT is the grand total, 130=ALMEN LÆGE I ALT is GP sub-total. Do not sum all ydelsesart values.
- alerams uses 5-year groups plus IALT. cf. sygp2 for single-year ages at region level only.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
