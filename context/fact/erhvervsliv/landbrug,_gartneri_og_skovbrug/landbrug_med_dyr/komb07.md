table: fact.komb07
description: Besætningskombinationer med kvæg og svin efter område, type, enhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- type: values [KS10=Bedrifter med kvæg, ikke svin, KS20=Bedrifter med svin, ikke kvæg, KS30=Bedrifter med både kvæg og svin, KS40=Bedrifter i alt med kvæg, KS50=Bedrifter i alt med svin, KS60=Bedrifter hverken med kvæg eller svin, KS70=I alt med husdyr (også andre end kvæg og svin), KS80=Alle bedrifter]
- enhed: values [ANTAL=Bedrifter (antal), AK=Kvæg, AS=Svin]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector with 3 values: ANTAL (bedrifter count), AK (kvæg count for those farms), AS (svin count for those farms). Always filter to one. AK/AS return 0 for farm types that don't hold that animal (e.g. type=KS20 (svin only) has AK=0).
- type has 8 overlapping categories. KS10 (kvæg only) + KS20 (svin only) + KS30 (both) are mutually exclusive and add up to KS70. KS40=KS10+KS30 (all with kvæg), KS50=KS20+KS30 (all with svin), KS70=KS10+KS20+KS30+others, KS80=all bedrifter. Never sum KS40+KS10 or KS50+KS20 — that double-counts. Use KS10/KS20/KS30/KS60 for non-overlapping breakdown.
- omrade has 12 values but only 10 join to dim.nuts: 5 regioner (81-85, niveau 1) and 5 landsdele (4,7,8,9,10, niveau 2). Code 0=Hele landet and code 15=merged Copenhagen-area landsdel are not in dim.nuts. Same pattern as hdyr07.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 15).