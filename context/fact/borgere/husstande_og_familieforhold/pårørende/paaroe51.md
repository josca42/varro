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
- indikator is a gender measurement selector that triples every row: LATT = both sexes (hours), LA1T = mænd (hours), LA2T = kvinder (hours). Always filter to one value. Unlike paaroe50, the totals here are in hours (Gns. antal timer pr. uge) not percentages.
- indhold is an average (weekly hours per person), not a count. Cannot be summed across regions or age groups without weighting.
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (98 kommuner). Code 0 = national total, does not join dim.nuts. Same pattern as paaroe50.
- alder and parorendeforhold are identical to paaroe50. paaroe50 and paaroe51 are companion tables: paaroe50 = share receiving home care, paaroe51 = hours per person among recipients.
- To understand both penetration and intensity together, query paaroe50 (share) alongside paaroe51 (hours) with matching filters.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.