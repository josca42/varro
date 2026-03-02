table: fact.varer
description: Industriens salg af egne varer (kvartal) efter varegruppe, enhed og tid
measure: indhold (unit -)
columns:
- varegr: join dim.kn on varegr::text=kode [approx]
- enhed: values [V=Værdi (1000 kr.), M=Mængde]
- tid: date range 1995-01-01 to 2024-10-01
dim docs: /dim/kn.md

notes:
- varegr is CN10 (10-digit Combined Nomenclature), stored as integer — leading zero dropped, so most codes appear as 9 digits (e.g., 201100000 = CN10 0201100000). dim.kn stores CN8 codes (e.g., "0101 21 00") — the documented dim.kn join does NOT work (0% match). Use ColumnValues("varer", "varegr") to get varegr labels directly.
- enhed is a measurement selector: V=Værdi (1000 kr.) and M=Mængde (quantity, unit varies by product). Every varegr×tid combination appears twice — once per enhed. Always filter to one: WHERE enhed='V' for money values. Omitting this silently doubles all figures.
- For a total industry sales value by product: filter enhed='V', then query by varegr. For quantity: filter enhed='M' (but note the unit for M is product-dependent and not labeled in the table).