table: fact.ligedi1
description: Ligestillingsindikator for opstillede og valgte kandidater til folketingsvalg efter kandidater, indikator, alder og tid
measure: indhold (unit -)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [TOT=Alder i alt, U20=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 70OV=70 år og derover]
- tid: date range 2001-01-01 to 2022-01-01

notes:
- Same indikator semantics as ligedi0: LA1=mænd %, LA2=kvinder %, LA3=difference. Never sum across indikator.
- alder includes TOT (aggregate) and 13 age groups. Summing all alder values double-counts (TOT equals the sum of all groups). Always filter alder='TOT' for overall, or one specific age group.
- For the same indicators without age breakdown and going back to 1918, use ligedi0.
