table: fact.ligedi13
description: Ligestillingsindikator for bestyrelsesmedlemmer og direktører efter indikator, type, branche (DB07 19-grp) og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- type: values [20=Bestyrelse, 30=Direktører]
- branchedb0721: join dim.db on branchedb0721=kode::text [approx]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- indhold is a percentage or procentpoint (same as ligedi11/12). Never sum across indikator. Select one: LA1=mænd pct, LA2=kvinder pct, LA3=forskel.
- type only has 20=Bestyrelse and 30=Direktører — no I alt type.
- branchedb0721 uses DB07 letter codes (A–S, X, TOT) — dim.db join does not work. Use ColumnValues("ligedi13", "branchedb0721"). TOT = Erhverv i alt.