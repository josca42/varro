table: fact.auk01
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige i alt, DP=Nettoledige dagpengemodtagere ... RE=Revalideringsydelse i øvrigt, LY=Ledighedsydelse, SY=Sygedagpenge mv., RES=Ressourceforløb, JA=Jobafklaringsforløb]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts. Use ColumnValues("nuts", "titel", for_table="auk01") to see available codes. Three hierarchy levels: niveau 1 = 5 regioner, niveau 2 = 11 landsdele, niveau 3 = 98 kommuner. Filter WHERE d.niveau = N to pick a single level and avoid double-counting across levels.
- omrade='0' = Hele landet (national total), omrade='997' = Uoplyst/unknown municipality. Neither is in dim.nuts — handle them separately or exclude from region analysis.
- ydelsestype has 41 codes with hierarchical subtotals (TOT, TOTUSU, TOTLE, TOTAN, TOTSB, TOTTB, TOTVO, TOTYD are aggregates). Never sum across all values. Pick one level.
- This table has 5 dimension columns (omrade, ydelsestype, kon, alder, tid). For a simple national total: omrade='0', kon='TOT', alder='TOT', ydelsestype='TOT'. Forgetting any one of these inflates the sum.
- alder groups: TOT, then 5-year bands from 16-24 through 55-59, plus 6099 (60+). No individual ages.
- Quarterly data (tid steps Jan/Apr/Jul/Oct). Latest to 2025-04-01. For annual data use auh01.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 997).
