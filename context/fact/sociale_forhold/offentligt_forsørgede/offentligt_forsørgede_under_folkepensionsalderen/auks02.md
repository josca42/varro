table: fact.auks02
description: Offentligt forsørgede (fuldtidsmodtagere, sæsonkorrigeret) efter ydelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [TOT=I alt, TOTUSU=I alt uden SU-modtagere, SU=SU-modtagere]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- tid: date range 2007-01-01 to 2025-04-01
notes:
- Only 3 ydelsestype values: TOT (alle offentligt forsørgede), TOTUSU (without SU recipients), SU (SU recipients only). Very coarse — use auks01 for full ydelsestype breakdown.
- Quarterly, seasonally adjusted. Has kon and alder breakdowns that auks01 lacks.
- alder groups: TOT, 16-24, 25-29, 30-39, 40-49, 50-59, 60+ (broader groupings than the non-seasonally-adjusted auk01/auk02 which go to 5-year bands).
- Filter kon=TOT and alder=TOT when you want a national aggregate to avoid overcounting.
