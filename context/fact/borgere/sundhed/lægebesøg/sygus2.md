table: fact.sygus2
description: Offentlige udgifter ved lægebesøg mv. (detaljeret) efter område, ydelsesart, alder, køn og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- ydelsesart: values [1=Anæsthesiologi, 4=Dermato-venerologi, 5=Diagnost. radiologi, 6=Reumatologi, 7=Gynækologi/obstetrik ... 82=Kak vagtlægehjælp 82, 83=Vagtlægehjælp 83, 89=KFA-vagtordning 89, 44=København Praktiserende Lægers Laboratorium (KPPL), 85=Lægehjælp (prak.læge amb. Vejle)]
- alerams: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Expenditure version of sygks2 (detailed specialty, region-only, single-year ages, indhold = 1.000 kr.).
- omrade joins dim.nuts niveau 1 only. omrade=0 is "Hele landet" and omrade=86 is uoplyst — exclude both when joining.
- ydelsesart lists individual specialties (no grand-total row).
- alerams has single-year ages (0, 1, ... 99-=99+) plus IALT.
- Map: /geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
