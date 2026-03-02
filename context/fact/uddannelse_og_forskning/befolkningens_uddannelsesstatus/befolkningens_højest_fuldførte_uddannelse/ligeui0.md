table: fact.ligeui0
description: Ligestillingsindikator for befolkningens højeste fuldførte uddannelse efter højest fuldførte uddannelse, indikator, alder og tid
measure: indhold (unit -)
columns:
- hfudd: join dim.ddu_udd on hfudd=kode [approx: H prefix needs stripping]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år]
- tid: date range 1986-01-01 to 2024-01-01
dim docs: /dim/ddu_udd.md

notes:
- indikator is a MEASUREMENT SELECTOR — always filter to exactly one value: LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mænd-kvinder (procentpoint). All dimension combinations repeat 3 times. Never sum across indikator values.
- hfudd does NOT join dim.ddu_udd — inline H10-H90 + TOT (11 codes). Same education classification as ligeub1.hfudd and hfudd16.uddannelsef.
- No geographic breakdown — national level only. Use ligeui1 for regional/herkomst breakdowns.
- Longest time series in the subject: back to 1986. Good for long-run gender gap trends in education.