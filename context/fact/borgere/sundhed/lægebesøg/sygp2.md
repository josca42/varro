table: fact.sygp2
description: Personer med kontakt til læge mv. med offentlig tilskud efter område, ydelsesart, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- alerams: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Counts distinct persons who had contact (not visit count). cf. sygp1 for regional+commune breakdown.
- omrade joins dim.nuts niveau 1 only (5 regioner). omrade=0 is "Hele landet" and omrade=86 is uoplyst — exclude both when joining.
- ydelsesart is hierarchical: 120=I ALT is the grand total. Do not sum all ydelsesart values.
- alerams has single-year ages (0, 1, 2, ... 99-=99+) plus IALT. Use sygp2 when single-year age granularity is needed at regional level.
- Map: context/geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
