table: fact.varer1
description: Industriens salg af egne varer (år) efter varegruppe, enhed og tid
measure: indhold (unit -)
columns:
- varegr: join dim.kn on varegr::text=kode [approx]
- enhed: values [V=Værdi (1000 kr.), M=Mængde]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/kn.md

notes:
- Annual counterpart to varer (quarterly). Same structure, same caveats.
- varegr is CN10 (10-digit), stored as integer — dim.kn join does NOT work (0% match). Use ColumnValues("varer1", "varegr") for labels.
- enhed is a measurement selector: V=Værdi (1000 kr.) or M=Mængde. Always filter to one value to avoid doubling counts.