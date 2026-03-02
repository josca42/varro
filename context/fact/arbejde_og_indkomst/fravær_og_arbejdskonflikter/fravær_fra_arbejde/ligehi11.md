table: fact.ligehi11
description: Ligestillingsindikator for anmeldte arbejdsulykker efter indikator, branche og tid
measure: indhold (unit -)
columns:
- indikator: values [M111=Mænd (pr. mio. præsterede arbejdstimer), K111=Kvinder (pr. mio. præsterede arbejdstimer), F111=Forskel mellem mænd og kvinder (point, pr. mio. præsterede arbejdstimer)]
- branche: join dim.db on branche=kode::text [approx]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- indikator has 3 values: M111=Mænd (pr. mio. præsterede arbejdstimer), K111=Kvinder (pr. mio. præsterede arbejdstimer), F111=Forskel (point). Filter to one value — these are independent rates.
- indhold = accident rate per million working hours, not a raw count. Use ligehb11 for raw counts.
- branche uses letter-based DB07 codes (B, CA, CB, ..., S, X, TOT) — does NOT join dim.db (0% match). Use ColumnValues("ligehi11", "branche") for labels. Same coding as ligehb11 except ligehb11 also has 'A' (Landbrug).
