table: fact.ligeai3
description: Ligestillingsindikator for beskæftigede efter branche (DB07), indikator og tid
measure: indhold (unit -)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- indhold is a gender indicator, NOT a count. LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). Never sum across indikator values — each row for a given branche07/tid gives three separate indicator values.
- branche07 uses 6-digit detailed codes (same as ras309). Use ColumnValues("ligeai3", "branche07") for labels. TOT = all industries.
- To find sectors with high gender imbalance: filter indikator='LA3' and look for large absolute values.
