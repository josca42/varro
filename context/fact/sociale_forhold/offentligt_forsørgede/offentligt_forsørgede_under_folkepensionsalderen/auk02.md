table: fact.auk02
description: Offentligt forsørgede (fuldtidsmodtagere) efter type, ydelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- type: values [FTM=Fuldtidsmodtagere, DEL=Modtagere]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige i alt, DP=Nettoledige dagpengemodtagere ... RE=Revalideringsydelse i øvrigt, LY=Ledighedsydelse, SY=Sygedagpenge mv., RES=Ressourceforløb, JA=Jobafklaringsforløb]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-04-01
notes:
- CRITICAL: type is a measurement selector that doubles every row. Always filter to one value: type='FTM' (fuldtidsmodtagere — full-time equivalent, the standard measure) or type='DEL' (modtagere — headcount of individuals). Summing across both types silently doubles all counts.
- ydelsestype has 41 codes with hierarchical subtotals. Never sum all values.
- alder: 5-year bands 16-24 through 55-59, plus TOT and 6099 (60+). Filter alder='TOT' unless analyzing by age.
- Quarterly data to 2025-04-01. For annual data use auh02.
