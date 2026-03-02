table: fact.kubs08
description: Kulturministeriet udbetalinger til virksomheder efter beliggenhed, kulturemne, virksomhedsform, virksomhedsstørrelse og tid
measure: indhold (unit 1.000 kr.)
columns:
- kubsbeli: join dim.nuts on kubsbeli=kode; levels [1, 2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler, 99=Uoplyst]
- virktyp2: values [TOT1=Alle virksomhedsformer, 1=Enkeltmandsfirma, 2=Interessentskab mv., 4=Aktieselskab, 6=Fond, forening mv., 3=Anpartsselskab, 5=Andelsforening, 7=Offentlig myndighed, 9=Anden ejer]
- virkstr: values [TOT1=Alle virksomhedsstørrelser, 11=0-1 ansat, 12=2-4 ansatte, 13=5-9 ansatte, 14=10-19 ansatte, 15=20-49 ansatte, 16=50-99 ansatte, 17=100 ansatte og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as kubs07 but measures disbursements (1.000 kr.) rather than workplace count (Antal). See kubs07 notes for join and filter guidance.
- `kubsbeli=0` is national aggregate (not in dim). Filter `d.niveau` for geographic granularity.
- `virktyp2=TOT1` and `virkstr=TOT1` are aggregate totals.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on kubsbeli=dim_kode. Exclude kubsbeli=0.