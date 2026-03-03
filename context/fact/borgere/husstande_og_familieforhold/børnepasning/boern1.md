table: fact.boern1
description: Fuldtidsomregnet pædagogisk personale i kommunale og selvejende daginstitutioner, institutionslignende puljeordninger og dagpleje efter område, stillingskategori, uddannelse og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- overens: values [TOT=I alt, 25=Dagpleje, 7=Pædagog, 9=Pædagogisk leder, 8A=Pædagogmedhjælper, pædagogisk assistent (-2018), 920=Pædagogmedhjælper (2019-), 930=Pædagogisk assistent (2019-), 940=Pædagogisk assistentstuderende (2019-), 950=Pædagogstuderende (2019-)]
- uddannelse: values [TOT=I alt, 460=Pædagoguddannelse (2019-), 470=Pædagogisk assistentuddannelse (2019-), 480=Anden pædagogisk uddannelse (2019-), 485=Ingen pædagogisk uddannelse (2019-), 490=Pædagogstuderende (2019-), 495=Pædagogisk assistentstuderende (2019-), 50=Pædagogisk assistent og grunduddannelse (PAU/PGU) (-2018), 51=Pædagog, professions bachelor (-2018), 52=Pædagog, MVU (ekskl. professions bachelor) (-20218, 53=Pædagogiske uddannelser uden nærmere angivelse (-2018), 54=Pædagogik, MVU (-2018), 55=Pædagogik, BACH, LVU og Ph.d. (-2018), 56=Ingen erhvervskompetencegivende uddannelse (-2018), 57=Anden uddannelse (-2018), 58=Uoplyst uddannelsesniveau (-2018)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner), and niveau 3 (98 kommuner).
- overens and uddannelse are cross-classified. Use overens='TOT' to analyse by uddannelse, or uddannelse='TOT' to analyse by overens. TOT x TOT = all FTE staff (62,795 nationally in 2024). Never sum non-TOT rows across both dimensions.
- CODING DISCONTINUITY in 2019: overens code 8A was split into 920 (pædagogmedhjælper), 930 (pædagogisk assistent), 940 (assistentstuderende), 950 (pædagogstuderende). uddannelse codes 50-58 were replaced by 460-495. Cross-year comparison at the sub-total level requires mapping old to new codes.
- overens=25 (Dagpleje) only appears with uddannelse sub-codes, not uddannelse=TOT — it has its own TOT row.
- Covers kommunale og selvejende institutions. For private institutions use pboern1 (2021-2023, different overens codes: 92/93/94/95 vs 920/930/940/950).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
