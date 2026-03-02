table: fact.ligedi3
description: Ligestillingsindikator for opstillede og valgte kandidater til regionalvalg efter kandidater, indikator og tid
measure: indhold (unit -)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 2005-01-01 to 2021-01-01

notes:
- Same as ligedi2 but for regionsråd elections — no geographic breakdown beyond the national level.
- indikator values (LA1=Mænd %, LA2=Kvinder %, LA3=Forskel pp) are independent measures — never sum them. Pick one per query.
- kandidat distinguishes OK (nominated) vs VK (elected). Pick one per query.
- For regional kommunalvalg data with geographic breakdown use ligedi2.