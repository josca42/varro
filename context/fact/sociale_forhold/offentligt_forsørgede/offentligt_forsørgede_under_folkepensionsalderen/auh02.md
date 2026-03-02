table: fact.auh02
description: Offentligt forsørgede (fuldtidsmodtagere) efter type, ydelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- type: values [FTM=Fuldtidsmodtagere, DEL=Modtagere]
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige i alt, DP=Nettoledige dagpengemodtagere ... RE=Revalideringsydelse i øvrigt, LY=Ledighedsydelse, SY=Sygedagpenge mv., RES=Ressourceforløb, JA=Jobafklaringsforløb]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- Annual version of auk02 (same columns and measurement selector). Latest to 2024-01-01.
- CRITICAL: type is a measurement selector — filter to one value. type='FTM' (fuldtidsmodtagere, full-time equivalent) or type='DEL' (headcount of individual recipients). Every row exists twice, once per type. Summing without filtering silently doubles all counts.
- ydelsestype has 41 codes with hierarchical subtotals. Use TOT for grand total or pick a single hierarchy level.
