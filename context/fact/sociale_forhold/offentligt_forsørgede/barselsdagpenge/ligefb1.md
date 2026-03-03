table: fact.ligefb1
description: Forældrepar efter barnets familieforhold, forældrenes dagpengeret, moderens højest fuldførte uddannelse, faderens højeste fuldførte uddannelse, område og tid
measure: indhold (unit Antal)
columns:
- barnfam: values [TOT=I alt, X1=Bor med begge forældre, X2=Bor med kun én eller ingen forælder]
- foraeldredagpenge: values [0=Alle forældrepar, uanset dagpengeret, 511=Både mor og far er berettigede til barselsdagpenge, 619=Mor er berettiget, men far er ikke berettiget til barselsdagpenge, 791=Mor er ikke berettiget, far er berettiget til barselsdagpenge, 899=Hverken mor eller far er berettigede til barselsdagpenge]
- morudd: values [TOT=I alt, CC1=Ingen ungdomsuddannelse, CC2=Ungdomsuddannelse, CC3=Kort videregående uddannelse, CC4=Mellemlang videregående uddannelse, CC5=Lang videregående uddannelse]
- farudd: values [TOT=I alt, CC1=Ingen ungdomsuddannelse, CC2=Ungdomsuddannelse, CC3=Kort videregående uddannelse, CC4=Mellemlang videregående uddannelse, CC5=Lang videregående uddannelse]
- omrade: join dim.nuts on omrade=kode; levels [2]
- tid: date range 2016-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `indhold` is a count of parent pairs (Antal). No measurement-selector column — each row is a distinct count.
- `barnfam` total is `'TOT'`. `X1`/`X2` are mutually exclusive and sum to `TOT`.
- `foraeldredagpenge` total is `'0'`. The four non-zero codes (511/619/791/899) are mutually exclusive combinations of mother's and father's entitlement — they sum to the total.
- `morudd` and `farudd` totals are both `'TOT'`. Education codes CC1–CC5 sum to TOT and are mutually exclusive for each parent.
- `omrade` joins dim.nuts. Code `0` = national total (not in dim). niveau 2 only (11 landsdele) — no kommune data in this table.
- This is a population count table (how many parent pairs exist), not a leave-days table. Pair it with ligefi1 for the leave-day averages.
- Map: /geo/landsdele.parquet — merge on omrade=dim_kode. Exclude omrade=0.