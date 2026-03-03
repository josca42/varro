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
- indikator is a gender measurement selector that triples every row: LATOT = both sexes (pct.), LA1 = mænd (pct.), LA2 = kvinder (pct.). These are percentages — never sum across indikator values. Filter to LATOT for the overall rate or LA1/LA2 for gender breakdown.
- indhold is a percentage (share of 65–84-year-olds who receive home care). Not a count — cannot be summed across regions without weighting.
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (98 kommuner). Code 0 is the national total and does not join. Use WHERE f.omrade != '0' when joining, or handle code 0 separately.
- alder covers only 65–84 years: TOT85 (65–84 i alt) plus 4 five-year bands. This table is not applicable for other age groups.
- parorendeforhold (PR810–PR840): same 4 adult family-structure categories as paaroe31 — mutually exclusive.
- Sample query — national home care rate by family type (total, 2024): SELECT parorendeforhold, indhold FROM fact.paaroe50 WHERE omrade='0' AND alder='TOT85' AND indikator='LATOT' AND tid='2024-01-01';
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.