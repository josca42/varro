table: fact.kn8mest
description: Im- og eksport KN (EU Kombineret nomenklatur) efter im- og eksport, varer, land, enhed, datakilde og tid
measure: indhold (unit -)
columns:
- indud: values [1=Import, 2=Eksport]
- vare: join dim.kn on vare=REPLACE(kode, ' ', '') [approx: Fact uses no spaces (01012100), dimension uses spaces (0101 21 00)]
- land: join dim.lande_uhv on land=kode [approx: Aggregate codes missing from dimension]; levels [4]
- enhed: values [98=Kilo, 99=Kroner, 97=Anden enhed]
- datakilde: values [TOT=Samlet handel, IND=Handel fra indberettende virksomheder, EST=Beregnet EU-handel for virksomheder fritaget fra Intrastat]
- tid: date range 2016-01-01 to 2016-06-01
dim docs: /dim/kn.md, /dim/lande_uhv.md

notes:
- vare joins dim.kn with REPLACE(d.kode, ' ', '') — the dim stores codes with spaces (e.g. "0101 21 00") but the fact uses no spaces ("01012100"). Use: JOIN dim.kn d ON f.vare = REPLACE(d.kode, ' ', ''). All matched vare codes are niveau 5 (leaf-level 8-digit KN codes). Use ColumnValues("kn", "titel", for_table="kn8mest") or fuzzy match on titel to find product codes.
- enhed is a MEASUREMENT SELECTOR: every vare+land combination appears three times (98=Kilo, 99=Kroner, 97=Anden enhed). Always filter to a single enhed or counts are silently tripled.
- datakilde is a MEASUREMENT SELECTOR: every combination appears three times more (TOT=Samlet handel, IND=Intrastat-rapporterede, EST=Beregnet EU-handel). Always filter — typically TOT for totals. Not filtering triples counts again.
- land=TOT (world total) is not in dim.lande_uhv. Filter out when joining, or include explicitly for global aggregate.
- This table covers only 2016 (6 months). For longer time series use kn8y (1988–2024 annual).