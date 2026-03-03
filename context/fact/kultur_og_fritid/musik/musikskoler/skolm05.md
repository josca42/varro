table: fact.skolm05
description: Musikskolernes økonomi efter kommune, økonomiske nøgletal og tid
measure: indhold (unit Kr.)
columns:
- komk: join dim.nuts on komk=kode; levels [3]
- oeknogl: values [2500=Lederløn, 2505=Lærerløn, 2510=Kørsel, 2515=Statsligt tilskud, 2520=Elevbetaling]
- tid: date range 2012 to 2025
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau 3 (99 kommuner). komk='0' is the national total, not in the dim. This is the only table in this subject using nuts niveau 3 for municipalities — note dim.nuts uses different municipality codes than dim.kommunegrupper (nuts kode e.g. 101 for København vs kommunegrupper also 101, but hierarchy differs).
- oeknogl is a financial metric selector — each code is a distinct line item (lederløn, lærerløn, kørsel, statsligt tilskud, elevbetaling). Never SUM across oeknogl; always filter to one value.
- Longest time series in this subject: 2012–2025. Use for historical trend analysis of school finances.
- Map: /geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.