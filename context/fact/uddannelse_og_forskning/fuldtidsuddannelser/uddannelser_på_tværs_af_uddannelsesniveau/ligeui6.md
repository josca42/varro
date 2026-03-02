table: fact.ligeui6
description: Ligestillingsindikator for uddannelsesaktivitet på STEM-uddannelser efter uddannelse, indikator og tid
measure: indhold (unit -)
columns:
- uddannelse: values [TOT=I alt, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- indhold is a rate, not a count. Never sum across rows. LA1=share of men (%), LA2=share of women (%), LA3=LA1−LA2 (percentage points). For 2024 STEM total: LA1=41.2%, LA2=17%, LA3=24.2pp.
- Covers only STEM higher education (H40–H80). For all education levels use ligeui3.
- Only two dimensions (uddannelse and indikator) — no alder, geography, or herkomst breakdown.