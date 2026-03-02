table: fact.auks01
description: Offentligt forsørgede (fuldtidsmodtagere, sæsonkorrigeret) efter ydelsestype og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere, TOTLE=Nettoledige i alt, DP=Nettoledige dagpengemodtagere ... RE=Revalideringsydelse i øvrigt, LY=Ledighedsydelse, SY=Sygedagpenge mv., RES=Ressourceforløb, JA=Jobafklaringsforløb]
- tid: date range 2007-01-01 to 2025-04-01
notes:
- ydelsestype has 41 codes including hierarchical subtotals (TOT, TOTUSU, TOTLE, TOTAN, TOTSB, TOTTB, TOTVO, TOTYD are aggregates; remaining codes are leaf benefit types). Never sum across all ydelsestype values. Use TOT for national total or pick one hierarchy level.
- Quarterly, seasonally adjusted. No regional, gender, or age breakdown — only ydelsestype × tid. For disaggregated seasonal data use auks02 (adds kon, alder, but only 3 ydelsestype values).
- Seasonal adjustment makes values comparable across quarters without holiday distortion — preferred for trend analysis. For raw quarterly counts use auk01.
