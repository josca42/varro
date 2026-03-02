table: fact.kn8y
description: Im- og eksport KN (EU Kombineret nomenklatur) efter im- og eksport, varer, land, enhed og tid
measure: indhold (unit -)
columns:
- indud: values [1=Import, 2=Eksport]
- vare: join dim.kn on vare=REPLACE(kode, ' ', '') [approx: Fact uses no spaces (01012100), dimension uses spaces (0101 21 00)]
- land: join dim.lande_uhv on land=kode [approx: Aggregate codes missing from dimension]; levels [4]
- enhed: values [98=Kilo, 99=Kroner, 97=Anden enhed]
- tid: date range 1988-01-01 to 2024-01-01
dim docs: /dim/kn.md, /dim/lande_uhv.md

notes:
- vare joins dim.kn with REPLACE(d.kode, ' ', '') — same as kn8mest. All matched vare codes are niveau 5 (leaf-level 8-digit codes). Use ColumnValues("kn", "titel", for_table="kn8y") to search by product name.
- Only 51% of distinct vare codes match dim.kn. This is because dim.kn only contains the current KN nomenclature, while kn8y goes back to 1988. Old historical codes (pre-~2010) have been reclassified or removed from the current dim. For recent years (2015+), match rate is near 100%. Don't filter to only matched codes if you need historical continuity.
- vare=TOT (all products) is an aggregate code not in dim. Include or exclude explicitly.
- enhed is a MEASUREMENT SELECTOR: every vare+land+tid combination appears up to 3 times (98=Kilo, 99=Kroner, 97=Anden enhed). Always filter to one enhed — use enhed='99' for value in DKK.
- Annual data (tid is year). For monthly data see kn8mest (but kn8mest only covers 2016).