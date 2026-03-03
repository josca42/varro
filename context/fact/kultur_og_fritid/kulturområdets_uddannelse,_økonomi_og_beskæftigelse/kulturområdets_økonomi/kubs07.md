table: fact.kubs07
description: Virksomheder (arbejdssteder), der modtager udbetalinger fra Kulturministeriet efter beliggenhed, kulturemne, virksomhedsform, virksomhedsstørrelse og tid
measure: indhold (unit Antal)
columns:
- kubsbeli: join dim.nuts on kubsbeli=kode; levels [1, 2, 3]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler, 99=Uoplyst]
- virktyp2: values [TOT1=Alle virksomhedsformer, 1=Enkeltmandsfirma, 2=Interessentskab mv., 4=Aktieselskab, 6=Fond, forening mv., 3=Anpartsselskab, 5=Andelsforening, 7=Offentlig myndighed, 9=Anden ejer]
- virkstr: values [TOT1=Alle virksomhedsstørrelser, 11=0-1 ansat, 12=2-4 ansatte, 13=5-9 ansatte, 14=10-19 ansatte, 15=20-49 ansatte, 16=50-99 ansatte, 17=100 ansatte og derover]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `kubsbeli=0` is national aggregate (not in dim). Three hierarchy levels in dim.nuts: niveau 1=regioner, 2=landsdele, 3=kommuner — filter d.niveau to pick one.
- `virktyp2=TOT1` and `virkstr=TOT1` are aggregate totals. Filter to these for an overall count of recipient workplaces.
- `kulturemne=0` is all topics aggregate. Broad category codes (uppercase) include sub-codes, so don't sum across levels.
- Parallel to kubs08 which measures disbursement amounts (1.000 kr.) rather than workplace count.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on kubsbeli=dim_kode. Exclude kubsbeli=0.