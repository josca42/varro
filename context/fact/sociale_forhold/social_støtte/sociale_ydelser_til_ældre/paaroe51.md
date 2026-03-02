table: fact.paaroe51
description: Visiteret hjemmehjælp, tid pr. person efter indikator, område, alder, relation og tid
measure: indhold (unit Gns. antal timer pr. uge)
columns:
- indikator: values [LA1T=Mænd (timer), LA2T=Kvinder (timer), LATT=Køn, i alt (timer)]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [TOT85=Alder (65-84 år) i alt, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år]
- parorendeforhold: values [PR810=Har en partner og ingen andre pårørende, PR820=Har en partner og andre pårørende, PR830=Har ingen partner, men har andre pårørende, PR840=Har hverken partner eller andre pårørende]
- tid: date range 2019-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is average hours per week per person — do not sum across rows.
- Covers only 65-84 age range (no 85+). For broader age coverage use aed021/aed02.
- indikator: LATT is the gender-total average; LA1T=mænd, LA2T=kvinder. Never add LA1T+LA2T.
- parorendeforhold has 4 mutually exclusive categories with no total. Each row represents a different family-relation group.
- omrade joins dim.nuts with niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is national total (not in dim).
- Pair with paaroe50 for the share (pct.) receiving home help by parorendeforhold.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
