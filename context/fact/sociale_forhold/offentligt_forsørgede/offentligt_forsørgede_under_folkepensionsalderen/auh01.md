table: fact.auh01
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige i alt, DP=Nettoledige dagpengemodtagere ... RE=Revalideringsydelse i øvrigt, LY=Ledighedsydelse, SY=Sygedagpenge mv., RES=Ressourceforløb, JA=Jobafklaringsforløb]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Annual version of auk01 (same columns, same dim joins). tid steps yearly (Jan 1). Latest to 2024-01-01 — use auk01 for 2024–2025 quarterly data.
- omrade joins dim.nuts: niveau 1 = 5 regioner, niveau 2 = 11 landsdele, niveau 3 = 98 kommuner. omrade='0' = Hele landet, omrade='997' = Uoplyst — neither is in dim.nuts. Filter WHERE d.niveau = N for a single level.
- ydelsestype has 41 codes with hierarchical subtotals (TOT, TOTUSU, TOTLE, TOTAN, TOTSB, TOTTB, TOTVO, TOTYD are aggregates). Never sum all values.
- For national total: omrade='0', kon='TOT', alder='TOT', ydelsestype='TOT'.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 997).
