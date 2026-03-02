table: fact.paaroe50
description: Personer visiteret til hjemmehjælp (andel af 65-84-årige) efter indikator, område, alder, relation og tid
measure: indhold (unit Pct.)
columns:
- indikator: values [LATOT=Køn, i alt (pct.), LA1=Mænd (pct.), LA2=Kvinder (pct.)]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [TOT85=Alder (65-84 år) i alt, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år]
- parorendeforhold: values [PR810=Har en partner og ingen andre pårørende, PR820=Har en partner og andre pårørende, PR830=Har ingen partner, men har andre pårørende, PR840=Har hverken partner eller andre pårørende]
- tid: date range 2019-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Covers only 65-84 age range (no 85+). For broader age coverage use aed06/aed12.
- indikator: LATOT/LA1/LA2 are independent percentages; LA1 and LA2 are never added together. Filter to LATOT for gender-neutral share.
- parorendeforhold has 4 mutually exclusive categories (no total row). There is no "pårørende i alt" — if you need the overall rate regardless of family situation, use alder=TOT85 and omit the parorendeforhold filter while summing is not correct; rather, do not filter on parorendeforhold and restrict to the indikator and alder of interest with omrade as the grouping dimension (the rows will span all 4 parorendeforhold values, so you'd need to pick one or average appropriately).
- omrade joins dim.nuts with niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 or d.niveau=1. omrade=0 is national total (not in dim).
- Pair with paaroe51 for hours per person per parorendeforhold.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
