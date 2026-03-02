table: fact.pboern1
description: Fuldtidsomregnet pædagogisk personale i private dagtilbudsinstitutioner efter område, stillingskategori, uddannelse og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- overens: values [TOT=I alt, 7=Pædagog, 9=Pædagogisk leder, 92=Pædagogmedhjælper, 93=Pædagogisk assistent, 94=Pædagogisk assistentstuderende, 95=Pædagogstuderende]
- uddannelse: values [TOT=I alt, 46=Pædagoguddannelse, 47=Pædagogisk assistentuddannelse, 48=Anden pædagogisk uddannelse, 49=Ingen pædagogisk uddannelse, 497=Pædagogstuderende, 499=Pædagogisk assistentstuderende]
- tid: date range 2021-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner), and niveau 3 (98 kommuner).
- overens and uddannelse are cross-classified: use overens='TOT' to analyse by uddannelse, or uddannelse='TOT' to analyse by overens. TOT x TOT = all FTE private institution staff.
- Short time range only: 2021-2023. For kommunale og selvejende institutions use boern1 (2015-2024).
- NOTE: overens codes differ from boern1. pboern1 uses 92/93/94/95 (2-digit); boern1 uses 920/930/940/950 (3-digit) for the same categories from 2019. Do not join or compare raw codes directly.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
