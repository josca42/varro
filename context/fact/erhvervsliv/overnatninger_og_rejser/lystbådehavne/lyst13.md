table: fact.lyst13
description: Lystbådehavne efter område, kapacitet og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2]
- kapacitet: values [3025=Lystbådehavne, 3030=Faste bådepladser, 3032=Gæstebådsovernatninger - I alt, 3034=Gæstebådsovernatninger - Betalte, 3036=Gæstebådsovernatninger - Frihavnsordning, 3040=Personovernatninger]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 2 only (11 landsdele). No regioner (niveau 1) in this table. omrade=0 is "Hele landet" — not in dim.
- kapacitet is a measure selector — 6 metrics, always filter to exactly one: 3025=antal lystbådehavne, 3030=faste bådepladser, 3032=gæstebådsovernatninger i alt, 3034=gæstebådsovernatninger betalte, 3036=gæstebådsovernatninger frihavnsordning, 3040=personovernatninger. Note: 3032 = 3034 + 3036 (total = paid + free harbour scheme), so never sum 3032+3034+3036.
- lyst13 has more kapacitet detail than lyst12 (splits guest boat nights into paid vs. free harbour scheme) but lacks the marina size breakdown.
- Example: regional breakdown of marinas: JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=2 AND f.kapacitet='3025'.
- Map: context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.