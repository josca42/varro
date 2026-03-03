table: fact.ligefi1
description: Ligestillingsindikator for barselsdagpengedage til forældrepar (gennemsnit) efter indikator, moderens højest fuldførte uddannelse, faderens højeste fuldførte uddannelse, forældrenes uddannelsesniveau, område og tid
measure: indhold (unit Dage)
columns:
- indikator: values [LA111=Far (dage), LA222=Mor (dage), LA333=Forskel mellem far og mor (dage)]
- morudd: values [TOT=I alt, CC1=Ingen ungdomsuddannelse, CC2=Ungdomsuddannelse, CC3=Kort videregående uddannelse, CC4=Mellemlang videregående uddannelse, CC5=Lang videregående uddannelse]
- farudd: values [TOT=I alt, CC1=Ingen ungdomsuddannelse, CC2=Ungdomsuddannelse, CC3=Kort videregående uddannelse, CC4=Mellemlang videregående uddannelse, CC5=Lang videregående uddannelse]
- foraeldreudd: values [TOT=I alt, UU1=Far og mor har uddannelse på samme niveau, UU2=Far har uddannelse på højere niveau end mor, UU3=Mor har uddannelse på højere niveau end far]
- omrade: join dim.nuts on omrade=kode; levels [2]
- tid: date range 2016-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `indhold` is an average (gennemsnit dage), not a count. Never SUM across rows — aggregate only as a weighted average or just SELECT the pre-computed value.
- `indikator` has 3 values (LA111=Far, LA222=Mor, LA333=Forskel). Filter to one per query. LA333 (difference) is derived (Mor minus Far) — it's a signed number (positive = Mor took more days).
- `morudd` and `farudd` totals are `'TOT'`. `foraeldreudd` total is `'TOT'`. Filter all three to `'TOT'` unless specifically analysing education. The three education columns are partially redundant: `foraeldreudd` compares levels of morudd vs farudd.
- `omrade` joins dim.nuts. Code `0` = national total (not in dim). niveau 2 only (11 landsdele).
- For a simple national gender gap time series: `WHERE indikator='LA333' AND morudd='TOT' AND farudd='TOT' AND foraeldreudd='TOT' AND omrade='0'`.
- Use ligefb1 to get the underlying population counts (number of parent pairs) that correspond to these averages.
- Map: /geo/landsdele.parquet — merge on omrade=dim_kode. Exclude omrade=0.