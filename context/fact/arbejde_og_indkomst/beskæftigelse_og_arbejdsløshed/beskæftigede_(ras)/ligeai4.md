table: fact.ligeai4
description: Ligestillingsindikator for beskæftigede (over 15 år) efter indikator, branche (DB07), forsikringskategori og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- branche07: join dim.db on branche07=kode::text [approx]
- fkategori: values [HF=Heltidsforsikrede, DF=Deltidsforsikrede, 980=Ikke forsikrede]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- indhold is a gender indicator, NOT a count. Same as ligeai3: LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). Never sum across indikator values.
- branche07 uses DB07-37-group letter codes (A, B, CA...) — does NOT join dim.db. Use ColumnValues("ligeai4", "branche07").
- fkategori has HF=Heltidsforsikrede, DF=Deltidsforsikrede, 980=Ikke forsikrede — no TOT code in this table. Cannot get aggregate across insurance categories directly.
