table: fact.ligeki3a
description: Ligestillingsindikator for elever på musikskoler efter indikator, kommune, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- alder1: values [TOT=Alder i alt, 0003=0-3 år, 0406=4-6 år, 0709=7-9 år, 1014=10-14 år, 1519=15-19 år, 2024=20-24 år, 2500=25 år og derover]
- tid: date range 2021 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a percentage or percentage-point difference, not a count. Never SUM across indikator values.
- indikator must always be filtered: LA1=% male students, LA2=% female students, LA3=difference (male minus female, in pp — negative means more women). LA1+LA2 ≈ 100 (except for uoplyst).
- komk joins dim.kommunegrupper at niveau 2. komk='0' is national total, not in the dim.
- alder1='TOT' for all ages combined. No uoplyst row (unlike skolm02a/02b). Age groups are the same as in skolm02a/02b.
- Map: /geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.